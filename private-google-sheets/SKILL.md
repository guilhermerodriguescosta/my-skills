---
name: private-google-sheets
description: Send read or append requests to a Google Sheet through the local OAuth helper. Use when the user provides a Google Sheets URL and asks to view or add a row.
---

# Private Google Sheets Skill

Run the helper script directly. It only communicates with Google Sheets and does not create local files.

Read a sheet:
   ```powershell
   python private-google-sheets\scripts\fetch_sheet.py "<SPREADSHEET_URL_OR_ID>"
   ```

Append a row when the user explicitly asks to add one:
   ```powershell
   python private-google-sheets\scripts\fetch_sheet.py "<SPREADSHEET_URL_OR_ID>" --append "value1" "value2"
   ```

Update a cell or range:
   ```powershell
   python private-google-sheets\scripts\fetch_sheet.py "<SPREADSHEET_URL_OR_ID>" --update "Sheet1!D13" "DONE"
   ```

If Google asks for sign-in, complete the OAuth browser prompt, then retry once.
