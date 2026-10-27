## Active Objective
Replace developer Supabase URL/Key inputs in `ComedyOS-app/joke-writer.html` with a true consumer "Sign in to ComedyOS" flow (`Continue with Apple`, `Continue with Google`, plus Email Link fallback) backed by a single central ComedyOS Supabase project with Row Level Security (`RLS`).

## Completed Changes
- Updated `ComedyOS-app/supabase-schema.sql` with multi-tenant `public.profiles`, the automatic `on_auth_user_created` trigger (`handle_new_comedyos_user()`), and strict Row Level Security (`RLS`) policies (`auth.uid() = user_id`) on `journal_entries`, `joke_blocks`, `media_attachments`, and `joke_versions`.
- Updated `ComedyOS-app/FLASH_3_8_SEQUENTIAL_WRITER_AND_JOURNAL_PLAN.md` so Flash 3.8 removes all Supabase URL/Key input fields from the UI and replaces them with `Continue with Apple` and `Continue with Google` OAuth buttons, automatic guest-to-cloud vault migration on login, and invisible background sync (`● SYNCED`).

## Unresolved / Broken
- None.

## Immediate Next Step
User switches to Gemini 3.8 Flash and runs the prompt in `ComedyOS-app/FLASH_3_8_SEQUENTIAL_WRITER_AND_JOURNAL_PLAN.md` to update `ComedyOS-app/joke-writer.html`.
