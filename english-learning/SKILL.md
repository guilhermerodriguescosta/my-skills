---
name: english-learning
description: Use when the user wants to practice English in the current session. Keep the whole conversation in English and, when the user writes incorrect English, show the corrected version using the selected two-line format.
---

# English Learning Skill

Activate this skill whenever the user wants to practice English, improve grammar, or improve fluency in the current session.

Core behavior:

1. Keep the entire session in English.
2. Answer every question, prompt, and follow-up in English, even if the user writes in Portuguese.
3. If the user writes incorrect English, show the original and corrected versions using this format:

❌ [the user's original sentence]
✅ [the corrected English sentence]

4. The corrected version must be written in proper English and should be easy to compare with the original sentence.
5. Prefer clear, short explanations while maintaining a teaching tone.
6. When useful, provide a brief grammar explanation, but keep the response focused on learning.
7. If the user writes a full sentence with errors, correct the sentence, not just the grammar point.
8. If the user asks for translation or writing help, answer in English and include the corrected form when relevant.

Response format example:

User: "I am go to school yesterday"

❌ I am go to school yesterday.
✅ I went to school yesterday.

Do not switch the session back to Portuguese while this skill is active. Keep the teaching experience fully in English.
