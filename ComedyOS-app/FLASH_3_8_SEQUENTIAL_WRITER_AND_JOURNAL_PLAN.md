# Master Implementation Plan for Gemini 3.8 Flash
## Consumer Apple/Google OAuth Sign-In, Invisible Background Sync & Sequential Workbench (`joke-writer.html`)

> **How to use this file:** Switch your model selector to **Gemini 3.8 Flash** and prompt:
> *"Read `ComedyOS-app/FLASH_3_8_SEQUENTIAL_WRITER_AND_JOURNAL_PLAN.md` and update `ComedyOS-app/joke-writer.html` so users never see Supabase URL/Key inputs and instead sign in directly to ComedyOS with Apple or Google OAuth with automatic invisible cloud sync."*

---

## 1. Critical Architectural Rule: Zero Database Config Shown to Users

1. **End-Users NEVER See the Word "Supabase" or API Key Inputs:**
   - Remove `#supabaseUrlInput`, `#supabaseKeyInput`, and all developer database configuration fields from the HTML UI.
   - ComedyOS owns a single central Supabase backend configured in a locked JavaScript constant at the top of `<script type="module">`:
     ```javascript
     const COMEDYOS_CLOUD_CONFIG = {
       // Founder pastes project URL & public anon key here once (or injected by Cloudflare build)
       supabaseUrl: window.__COMEDYOS_SUPABASE_URL__ || 'https://YOUR_PROJECT_ID.supabase.co',
       supabaseAnonKey: window.__COMEDYOS_SUPABASE_ANON_KEY__ || 'YOUR_PUBLIC_ANON_KEY',
       redirectUrl: window.location.origin + window.location.pathname
     };
     ```
2. **Consumer "Sign in to ComedyOS" Experience (Apple & Google OAuth):**
   - In the top context strip, replace the old `Supabase Sync` button with a clean consumer account indicator & button:
     - **When Logged Out (Guest Mode):**
       - Status badge: `LOCAL VAULT`
       - Button: **`[ Sign In · Sync ]`** (opens the sleek inline **ComedyOS Account Bar**).
     - **Inside the ComedyOS Account Bar (`#accountAuthBar`):**
       - Left label: `COMEDYOS CLOUD VAULT · AUTOMATIC SYNC ACROSS PHONE & DESKTOP`
       - Primary OAuth Buttons (using `.btn` contract with inline Apple & Google monoline SVG icons):
         - **`[  Continue with Apple ]`** $\rightarrow$ calls `signInWithProvider('apple')` (`supabase.auth.signInWithOAuth({ provider: 'apple', options: { redirectTo: COMEDYOS_CLOUD_CONFIG.redirectUrl } })`)
         - **`[ G Continue with Google ]`** $\rightarrow$ calls `signInWithProvider('google')` (`supabase.auth.signInWithOAuth({ provider: 'google', options: { redirectTo: COMEDYOS_CLOUD_CONFIG.redirectUrl } })`)
         - **Optional Magic Link Fallback:** Compact email input + **`[ Email Link ]`**.
     - **When Logged In:**
       - The top context strip displays:
         - Sync status: `● SYNCED` (updates to `SYNCING...` during writes, `● SYNCED` on completion)
         - User identity pill: e.g. `viktor@viktorenns.de` (or display name from Apple/Google profile)
         - **`[ Sign Out ]`** button (`.btn-compact .btn-ghost`).
3. **Automatic Guest-to-Cloud Vault Migration on First Login:**
   - If a comic writes 3 jokes while in Guest Mode (`localStorage`) and then clicks **`Continue with Apple`** or **`Continue with Google`**, the `onAuthStateChange` handler automatically uploads all local guest jokes into their authenticated account (`user_id = session.user.id`) before pulling down their existing cloud vault—ensuring **zero lost material**!
4. **Seamless Local Preview Fallback (When `YOUR_PROJECT_ID` Placeholder Is Still Present):**
   - If `COMEDYOS_CLOUD_CONFIG.supabaseUrl` still contains `'YOUR_PROJECT_ID'` (before the founder pastes their live project URL), clicking **`Continue with Google`** or **`Continue with Apple`** simulates an instant OAuth login as `comic@viktorenns.de` (`status: ● SYNCED (PREVIEW)`) so the entire consumer sign-in flow can be tested immediately in the browser!
   - As soon as real Supabase credentials are placed in `COMEDYOS_CLOUD_CONFIG`, it automatically uses real Supabase OAuth + Postgres + Realtime + Storage.

---

## 2. SVG Icons to Add to `ICONS` Dictionary

Add these two crisp `13×13` monoline icons to `ICONS` for the Apple and Google sign-in buttons:

```javascript
  apple: `<svg width="13" height="13" viewBox="0 0 16 16" fill="currentColor"><path d="M11.1 8.4c0-1.6 1.3-2.4 1.4-2.5-.8-1.1-2-1.3-2.4-1.3-1-.1-2 .6-2.5.6-.5 0-1.3-.6-2.1-.6-1.1 0-2.1.6-2.7 1.6-1.2 2-.3 5 .8 6.6.6.8 1.2 1.7 2.1 1.6.8 0 1.2-.5 2.2-.5 1 0 1.3.5 2.2.5.9 0 1.5-.8 2.1-1.6.7-.9.9-1.8.9-1.9-.1 0-2-.7-2-2.5zM9.6 3.9c.5-.6.8-1.4.7-2.2-.7 0-1.5.5-2 1-.4.5-.8 1.3-.7 2.1.8.1 1.5-.4 2-.9z"/></svg>`,
  google: `<svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M14 8.2H8.2V6.8H14.2C14.3 7.3 14.4 7.7 14.4 8.2C14.4 11.8 11.9 14.2 8.2 14.2C4.7 14.2 1.8 11.3 1.8 7.8C1.8 4.3 4.7 1.4 8.2 1.4C9.9 1.4 11.4 2 12.5 3.1"/></svg>`,
  user: `<svg width="13" height="13" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.25"><circle cx="8" cy="5.5" r="2.8"/><path d="M2.5 14C3.2 11.2 5.3 9.8 8 9.8C10.7 9.8 12.8 11.2 13.5 14"/></svg>`
```

---

## 3. Exact HTML Replacement for `#supabaseSyncBar` $\rightarrow$ `#accountAuthBar`

Replace the old `#supabaseSyncBar` section and top strip button with:

### Top Context Strip Account Control:
```html
<span class="mono" id="syncStatusIndicator">LOCAL VAULT</span>
<button type="button" class="btn btn-compact" id="accountAuthBtn" onclick="toggleAccountBar()">
  <span id="userIconSlot"></span> <span id="accountBtnLabel">Sign In · Sync</span>
</button>
```

### Inline Consumer Sign-In Bar (`#accountAuthBar`):
```html
<section class="supabase-sync-bar" id="accountAuthBar">
  <!-- Logged-Out Consumer View -->
  <div id="loggedOutAuthView">
    <div class="block-header-row">
      <span class="micro-label">SIGN IN TO COMEDYOS · AUTOMATIC CLOUD VAULT SYNC</span>
      <button type="button" class="btn btn-compact btn-ghost" onclick="toggleAccountBar()">Close</button>
    </div>

    <div style="display: flex; align-items: center; justify-content: space-between; gap: 16px; flex-wrap: wrap; margin-top: 8px;">
      <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
        <button type="button" class="btn btn-primary" onclick="signInWithOAuthProvider('apple')">
          <span id="appleIconSlot"></span> Continue with Apple
        </button>
        <button type="button" class="btn btn-primary" onclick="signInWithOAuthProvider('google')">
          <span id="googleIconSlot"></span> Continue with Google
        </button>
      </div>

      <div style="display: flex; align-items: flex-end; gap: 8px; flex: 1; min-width: 240px; max-width: 380px;">
        <div class="input-line-group" style="flex: 1; padding-bottom: 4px;">
          <label class="micro-label">OR SIGN IN VIA EMAIL LINK</label>
          <input type="email" id="magicLinkEmailInput" class="textarea-editorial" style="font-size: 14px;" placeholder="comic@domain.com" />
        </div>
        <button type="button" class="btn btn-compact" onclick="sendConsumerMagicLink()">Send Link</button>
      </div>
    </div>
  </div>

  <!-- Logged-In Consumer View -->
  <div id="loggedInAuthView" style="display: none;">
    <div class="block-header-row">
      <span class="micro-label" id="loggedInUserLabel">SIGNED IN AS COMIC</span>
      <div style="display: flex; align-items: center; gap: 8px;">
        <span class="mono" style="color: var(--accent);">ALL JOKES &amp; SCANS AUTOMATICALLY SYNCED</span>
        <button type="button" class="btn btn-compact" onclick="signOutComedyOS()">Sign Out</button>
        <button type="button" class="btn btn-compact btn-ghost" onclick="toggleAccountBar()">Close</button>
      </div>
    </div>
  </div>
</section>
```

---

## 4. Automatic Background Sync & OAuth Implementation Contract

1. **Auto-Initialize on Boot (`initComedyOSCloud()`):**
   - Check if `COMEDYOS_CLOUD_CONFIG.supabaseUrl` is configured (not `'https://YOUR_PROJECT_ID.supabase.co'`).
   - If configured:
     - Import `createClient` from `https://esm.sh/@supabase/supabase-js@2`.
     - Register `supabaseClient.auth.onAuthStateChange((event, session) => { ... })`.
     - When `session?.user` is present:
       - Update `#syncStatusIndicator` to `● SYNCED` (in `var(--accent)`).
       - Update `#accountBtnLabel` to `session.user.email`.
       - Migrate any unsynced local guest jokes (`!entry.user_id`) by setting `entry.user_id = session.user.id` and upserting them to `journal_entries` and `joke_blocks`.
       - Subscribe to real-time Postgres changes filtered by `user_id=eq.${session.user.id}`.
2. **Handwritten Scan & Voice Memo Storage Upload:**
   - When a user is logged in and captures a handwritten notebook scan (`ocr_image_data_url`) or voice memo, automatically upsert both the extracted text in `journal_entries` AND the attachment record in `media_attachments` (`media_type: 'handwriting_image' | 'voice_audio'`, `extracted_text`, `user_id: currentUser.id`).
3. **Preserving All Existing Desktop & Mobile Features:**
   - Keep 100% of the existing Desktop Two-Stage Sequential Workbench (`Alt+S`, `Alt+P`, `Alt+B`, `Alt+T`, Ghost Suggested `Set-up` & `Punchline`, Sequential `Bridge` variations, Obsidian/Antigravity Split-View Journal) and Mobile "Google Keep for Jokes" Capture Client intact.

---

## 5. Verification Checklist for Flash 3.8

- [ ] **Zero Supabase Jargon or Key Inputs in UI:** No `#supabaseUrlInput` or `#supabaseKeyInput` in the DOM; the UI says only `Sign In · Sync`, `Continue with Apple`, `Continue with Google`, and `● SYNCED`.
- [ ] **Apple & Google OAuth Triggers:** `signInWithOAuthProvider('apple')` and `signInWithOAuthProvider('google')` call `supabaseClient.auth.signInWithOAuth(...)` when configured, and provide an instant preview sign-in when testing locally before credentials are added.
- [ ] **Automatic Background Sync:** Every edit, block insertion, or mobile capture automatically syncs in the background (`SYNCING...` $\rightarrow$ `● SYNCED`) without the user ever clicking a manual "sync" button.
