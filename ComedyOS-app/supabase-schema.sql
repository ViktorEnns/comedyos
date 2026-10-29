-- =============================================================================
-- COMEDY OS — MULTI-TENANT SUPABASE POSTGRESQL SCHEMA + ROW LEVEL SECURITY (RLS)
-- Architecture:
--   • ComedyOS owns ONE central Supabase database.
--   • End-users NEVER see Supabase; they simply click "Continue with Apple" or
--     "Continue with Google" inside ComedyOS.
--   • Row Level Security (RLS) guarantees every comic can ONLY read/write their
--     own jokes, blocks, audio voice memos, and notebook scans (auth.uid() = user_id).
-- =============================================================================

create extension if not exists "pgcrypto";

-- -----------------------------------------------------------------------------
-- 1. COMEDYOS USER PROFILES (Auto-created on first Apple / Google sign-in)
-- -----------------------------------------------------------------------------
create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  email text,
  display_name text,
  avatar_url text,
  auth_provider text default 'oauth',
  baseline_wpm int not null default 130,
  next_bit_number int not null default 105,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

alter table public.profiles enable row level security;

create policy "Users can view their own profile"
  on public.profiles for select
  using (auth.uid() = id);

create policy "Users can update their own profile"
  on public.profiles for update
  using (auth.uid() = id);

-- Trigger: Automatically create a ComedyOS profile when a new user signs in with Apple/Google
create or replace function public.handle_new_comedyos_user()
returns trigger
language plpgsql
security definer set search_path = public
as $$
begin
  insert into public.profiles (id, email, display_name, avatar_url, auth_provider)
  values (
    new.id,
    new.email,
    coalesce(new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'name', split_part(new.email, '@', 1)),
    new.raw_user_meta_data->>'avatar_url',
    coalesce(new.raw_app_meta_data->>'provider', 'oauth')
  )
  on conflict (id) do nothing;
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_comedyos_user();

-- Revoke public HTTP execution of the trigger function (Satisfies Supabase Linter 0028 & 0029)
revoke execute on function public.handle_new_comedyos_user() from public, anon, authenticated;

-- -----------------------------------------------------------------------------
-- 2. JOURNAL ENTRIES (Unified Vault for Mobile Captures & Desktop Jokes)
-- -----------------------------------------------------------------------------
create table if not exists public.journal_entries (
  id uuid primary key default gen_random_uuid(),
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  display_code text not null default 'B-100',
  title text not null default '',
  raw_text text not null default '',
  modality text not null default 'quick_text'
    check (modality in ('quick_text', 'voice_memo', 'ocr_scan', 'set_tape', 'youtube')),
  status text not null default 'seed'
    check (status in ('seed', 'structured', 'stage_ready', 'retired')),
  version_label text not null default 'V1.0',
  transcript_segments jsonb not null default '[]'::jsonb,
  ocr_image_data_url text,
  is_archived boolean not null default false,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists idx_journal_entries_user_updated
  on public.journal_entries(user_id, updated_at desc);

alter table public.journal_entries enable row level security;

create policy "Users can read their own journal entries"
  on public.journal_entries for select
  using (auth.uid() = user_id);

create policy "Users can insert their own journal entries"
  on public.journal_entries for insert
  with check (auth.uid() = user_id);

create policy "Users can update their own journal entries"
  on public.journal_entries for update
  using (auth.uid() = user_id);

create policy "Users can delete their own journal entries"
  on public.journal_entries for delete
  using (auth.uid() = user_id);

-- -----------------------------------------------------------------------------
-- 3. SEQUENTIAL JOKE BLOCKS (Setup, Variable Bridges, Punchlines 1..N, Tags)
-- -----------------------------------------------------------------------------
create table if not exists public.joke_blocks (
  id uuid primary key default gen_random_uuid(),
  journal_entry_id uuid not null references public.journal_entries(id) on delete cascade,
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  sort_order int not null default 0,
  block_type text not null
    check (block_type in ('setup', 'bridge', 'punchline', 'tag')),
  bridge_category text default 'bridge'
    check (bridge_category in ('bridge', 'development', 'exploration')),
  bridge_subtype text default 'none'
    check (bridge_subtype in ('none', 'misdirect', 'exaggeration', 'repetition', 'reimagine', 'reenact', 'the_bend', 'list')),
  content text not null default '',
  punch_index int default 1,
  is_alt_variant boolean not null default false,
  is_stage_active boolean not null default true,
  word_count int not null default 0,
  syllable_count int not null default 0,
  updated_at timestamptz not null default now()
);

create index if not exists idx_joke_blocks_entry_order
  on public.joke_blocks(journal_entry_id, sort_order);

alter table public.joke_blocks enable row level security;

create policy "Users can read their own joke blocks"
  on public.joke_blocks for select
  using (auth.uid() = user_id);

create policy "Users can insert their own joke blocks"
  on public.joke_blocks for insert
  with check (auth.uid() = user_id);

create policy "Users can update their own joke blocks"
  on public.joke_blocks for update
  using (auth.uid() = user_id);

create policy "Users can delete their own joke blocks"
  on public.joke_blocks for delete
  using (auth.uid() = user_id);

-- -----------------------------------------------------------------------------
-- 4. MEDIA ATTACHMENTS (Voice Memo Audio & Handwritten Notebook Scan Photos)
-- -----------------------------------------------------------------------------
create table if not exists public.media_attachments (
  id uuid primary key default gen_random_uuid(),
  journal_entry_id uuid not null references public.journal_entries(id) on delete cascade,
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  media_type text not null check (media_type in ('voice_audio', 'handwriting_image')),
  storage_path text not null,
  extracted_text text,
  duration_seconds float,
  ocr_confidence float,
  created_at timestamptz not null default now()
);

alter table public.media_attachments enable row level security;

create policy "Users can manage their own media attachments"
  on public.media_attachments for all
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

-- -----------------------------------------------------------------------------
-- 5. JOKE VERSIONS (Milestone Snapshots)
-- -----------------------------------------------------------------------------
create table if not exists public.joke_versions (
  id uuid primary key default gen_random_uuid(),
  journal_entry_id uuid not null references public.journal_entries(id) on delete cascade,
  user_id uuid not null default auth.uid() references auth.users(id) on delete cascade,
  version_label text not null,
  snapshot_blocks jsonb not null,
  trigger_reason text not null,
  created_at timestamptz not null default now()
);

alter table public.joke_versions enable row level security;

create policy "Users can manage their own joke versions"
  on public.joke_versions for all
  using (auth.uid() = user_id)
  with check (auth.uid() = user_id);

-- -----------------------------------------------------------------------------
-- 6. ENABLE REALTIME SYNC BETWEEN MOBILE KEEP & DESKTOP WORKBENCH
-- -----------------------------------------------------------------------------
alter publication supabase_realtime add table public.journal_entries;
alter publication supabase_realtime add table public.joke_blocks;


-- -----------------------------------------------------------------------------
-- 7. COMEDIAN TESTER ONBOARDING & PROFILE METADATA (Added v1.1)
-- -----------------------------------------------------------------------------
alter table public.profiles
  add column if not exists stage_name text default '',
  add column if not exists home_scene text default '',
  add column if not exists years_performing text default '',
  add column if not exists social_handle text default '',
  add column if not exists primary_workflow text default 'hybrid',
  add column if not exists onboarding_completed boolean not null default false;

drop policy if exists "Users can insert their own profile" on public.profiles;
create policy "Users can insert their own profile"
  on public.profiles for insert
  with check (auth.uid() = id);
