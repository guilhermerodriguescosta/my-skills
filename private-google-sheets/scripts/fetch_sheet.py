import os
import re
import sys
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.readonly'
]

CREDENTIALS_FILE = r"C:\Estudo\Security\credentials.json"
TOKEN_FILE = r"C:\Estudo\Security\token.json"

def extract_spreadsheet_id(url_or_id: str) -> str:
    match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', url_or_id)
    if match:
        return match.group(1)
    return url_or_id

def get_authenticated_service():
    creds = None
    if os.path.exists(TOKEN_FILE):
        try:
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except Exception:
            creds = None

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                creds = None
        
        if not creds:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(
                    f"credentials.json not found at {CREDENTIALS_FILE}. "
                    "Please download OAuth client credentials from Google Cloud Console."
                )

            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            print("Opening browser for Google authentication...")
            creds = flow.run_local_server(port=0)

            with open(TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())
            print("Authentication successful! Token saved.")

    return build('sheets', 'v4', credentials=creds)

def fetch_sheet_data(spreadsheet_id_or_url: str, sheet_range: str = "A1:Z100"):
    sheet_id = extract_spreadsheet_id(spreadsheet_id_or_url)
    service = get_authenticated_service()

    # Get spreadsheet metadata to find first sheet name if not specified
    sheet_metadata = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
    sheets = sheet_metadata.get('sheets', '')
    title = sheet_metadata.get('properties', {}).get('title', 'Spreadsheet')
    first_sheet_title = sheets[0]['properties']['title'] if sheets else 'Sheet1'

    target_range = f"'{first_sheet_title}'" if not sheet_range else sheet_range
    result = service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range=target_range
    ).execute()

    rows = result.get('values', [])
    return title, first_sheet_title, rows

def append_row(spreadsheet_id_or_url: str, row_data: list):
    sheet_id = extract_spreadsheet_id(spreadsheet_id_or_url)
    service = get_authenticated_service()
    
    # Get first sheet name
    sheet_metadata = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
    first_sheet_title = sheet_metadata.get('sheets', '')[0]['properties']['title']
    
    body = {
        'values': [row_data]
    }
    
    result = service.spreadsheets().values().append(
        spreadsheetId=sheet_id,
        range=f"'{first_sheet_title}'!A:D",
        valueInputOption="USER_ENTERED",
        insertDataOption="INSERT_ROWS",
        body=body
    ).execute()
    
    return result

def update_range(spreadsheet_id_or_url: str, cell_range: str, values: list):
    sheet_id = extract_spreadsheet_id(spreadsheet_id_or_url)
    service = get_authenticated_service()
    return service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range=cell_range,
        valueInputOption="USER_ENTERED",
        body={"values": [values]}
    ).execute()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fetch_sheet.py <spreadsheet_url_or_id> [range] [--append values...] [--update range values...]")
        sys.exit(1)

    url_or_id = sys.argv[1]
    
    if len(sys.argv) > 2 and sys.argv[2] == "--append":
        row_data = sys.argv[3:]
        print(f"Appending row: {row_data}")
        try:
            result = append_row(url_or_id, row_data)
            print(f"Successfully appended row! Updated range: {result.get('updates', {}).get('updatedRange')}")
        except Exception as e:
            print(f"Error appending row: {e}")
            sys.exit(1)
    elif len(sys.argv) > 3 and sys.argv[2] == "--update":
        cell_range = sys.argv[3]
        values = sys.argv[4:]
        if not values:
            print("Error: provide at least one value to update.")
            sys.exit(1)
        try:
            result = update_range(url_or_id, cell_range, values)
            print(f"Successfully updated range: {result.get('updatedRange')}")
        except Exception as e:
            print(f"Error updating range: {e}")
            sys.exit(1)
    else:
        sheet_range = sys.argv[2] if len(sys.argv) > 2 else ""

        try:
            title, sheet_name, rows = fetch_sheet_data(url_or_id, sheet_range)
            print(f"Spreadsheet Title: {title}")
            print(f"Sheet Name: {sheet_name}")
            print(f"Total Rows: {len(rows)}")
            if rows:
                print("\nPreview (First 10 rows):")
                for row in rows[:10]:
                    print(" | ".join(row))
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
