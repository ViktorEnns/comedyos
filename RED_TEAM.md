# MISSION: RED TEAM (Comedy OS) (The Adversary)

**Role:** You are an expert penetration tester and QA engineer.
**Objective:** Break the application, find data leaks, and crash the system using the local Firebase Emulator. Do NOT run these tests against the production database.

## Test Suite 1: Database Security (Firestore Rules)

Attempt to write a script that performs the following malicious actions:

1. **The Peeping Tom:** Authenticate as `User A`. Attempt to read the `Notes` collection of `User B`.
2. **The Vandal:** Authenticate as `User A`. Attempt to edit or delete a joke owned by `User B`.
3. **The Ghost:** Attempt to read or write to the database without logging in at all.
*Action:* If any of these succeed, rewrite the `firestore.rules` file to block the exploit and run the test again.

## Test Suite 2: API & Cloud Function Abuse

Attempt to crash our backend services:

1. **The Talker:** Simulate uploading a corrupted audio file, or a massive 5-hour audio file, to the Firebase Storage bucket. Ensure the Gemini Cloud Function fails gracefully without crashing or causing an infinite billing loop.
2. **The Poisoner:** Inject malformed JSON or SQL-injection-style text into the Semantic Search vector generator. Ensure the system safely sanitizes it.

## Reporting

If you find a vulnerability, do not just fix it. Log the vulnerability in `PROGRESS.md` under the "Security" section and explain the fix.
