# ComedyOS Security Architecture & Feature Assurance Framework

> **Status:** Active & Mandatory Governance  
> **Last Updated:** October 2026  
> **Applies to:** Core Engine, Web Application, Local-First Storage, Cloudflare Edge Workers, and Docs Wiki

---

## 1. Security Philosophy & The Threat Model

Stand-up comedy material is unreleased, raw, intellectual property. A comedian's private notebook contains deeply personal observations, unvetted dark humor, experimental premises, and half-formed thoughts that—if leaked or scraped—could damage their career, invite material theft ("joke-stealing"), or expose them to public misunderstanding.

### The ComedyOS Zero-Trust Manifesto:
1. **Local-First by Default:** Comedians' written notes and stage audio recordings belong exclusively on their physical device (Origin Private File System / OPFS / SQLite WASM). They must never hit a multi-tenant cloud server without explicit, end-to-end encrypted opt-in.
2. **Ephemeral Edge Processing:** Any edge function (e.g., OCR translation, whisper transcript sync) must process data in volatile memory without persistence or AI training retention.
3. **Defense in Depth:** Protect against client-side tampering, edge exploitation, supply-chain attacks, and scraping.

---

## 2. Feature Vulnerability Analysis & Flaw Mitigation

| Feature Component | Inherent Security & Privacy Flaws | Threat Level | Required Architecture & Mitigation |
| :--- | :--- | :--- | :--- |
| **Stage 01: Setlist Builder** | • Client-side XSS via user-injected bit titles/tags.<br>• Prototype pollution in drag-and-drop state. | **Medium** | • Strict DOMPurify sanitization before rendering note titles.<br>• Schema validation on all setlist imports.<br>• Zero `eval()` or unescaped `innerHTML`. |
| **Stage 02: Longhand OCR Engine** | • EXIF metadata leakage in notebook photos (GPS location, device IDs, timestamps).<br>• Third-party OCR endpoints storing or training on photo buffers. | **High** | • Client-side EXIF stripping via Canvas/WASM prior to OCR processing.<br>• Zero-retention enterprise SLAs or on-device local WebAssembly OCR (Tesseract.js/Transformer.js). |
| **Stage 03: Pocket Audio Recorder** | • Microphone permission hijacking.<br>• Unencrypted temporary audio chunks cached in browser storage.<br>• Acoustic room fingerprinting. | **Critical** | • Audio recorded directly into OPFS encrypted with Web Crypto API (AES-GCM-256).<br>• Strict visual audio indicator while mic is active; explicit permission teardown when exiting stage mode. |
| **Waitlist Edge Function** | • Email harvesting & scraping attacks.<br>• Flooding/DDoS and bot spam.<br>• Google Sheet webhook credential leakage.<br>• Cross-Site Request Forgery (CSRF). | **High** | • Cloudflare Turnstile token validation on every submission.<br>• Cloudflare Worker rate limiting: max 3 requests per IP per minute.<br>• HMAC signature on cloud-to-sheet webhooks.<br>• Strict CORS headers restricted to `comedyos.com`. |
| **PWA & Local-First Storage** | • Cleartext database inspection on shared or stolen devices.<br>• Service Worker cache poisoning.<br>• Man-in-the-middle cache injection. | **High** | • Database at rest encrypted via SQLCipher in WebAssembly.<br>• Cache-Control: `no-store` on private user data.<br>• Strict Content Security Policy (CSP) blocking external scripts. |

---

## 3. Security Tooling Matrix: Current vs. Superior Alternatives

We evaluate each tool against modern security standards, ease of automation in CI/CD, and zero false-positive fatigue:

### 3.1 Static Application Security Testing (SAST) & Code Quality
| Category | Baseline / Common Tool | Recommended Alternative | Rationale & Advantage |
| :--- | :--- | :--- | :--- |
| **Code Scanning** | SonarQube | **Semgrep OSS** | Semgrep is significantly faster, lightweight, runs locally without heavyweight Java daemon, and supports custom rule definitions tailored to our local-first comedy data models. |
| **Privacy / Data Leaks** | ESLint Security Plugin | **Bearer CLI** | Bearer specifically tracks sensitive data flows (PII, credentials, audio buffers) from source to sink in TypeScript/JavaScript applications. |

### 3.2 Software Composition Analysis (SCA) & Supply Chain Security
| Category | Baseline / Common Tool | Recommended Alternative | Rationale & Advantage |
| :--- | :--- | :--- | :--- |
| **Dependency Auditing** | `npm audit` | **Socket.dev CLI** | `npm audit` only checks known CVEs. Socket detects supply-chain attacks, typosquatting, hidden network calls, and unauthorized disk access in real time. |
| **Vulnerability Monitor** | Dependabot | **Trivy + Snyk Developer** | Trivy provides lightning-fast container, repo, and filesystem vulnerability scanning with significantly fewer false positives than raw Dependabot PR spam. |

### 3.3 Secret Detection & Token Leak Prevention
| Category | Baseline / Common Tool | Recommended Alternative | Rationale & Advantage |
| :--- | :--- | :--- | :--- |
| **Secret Scanning** | `git-secrets` | **TruffleHog v3 + Gitleaks** | TruffleHog performs live entropy and active verification against 700+ credential formats, preventing API tokens and webhook URLs from entering git history. |

### 3.4 Dynamic Application Security Testing (DAST) & Edge Defense
| Category | Baseline / Common Tool | Recommended Alternative | Rationale & Advantage |
| :--- | :--- | :--- | :--- |
| **Bot Mitigation** | Google reCAPTCHA v2/v3 | **Cloudflare Turnstile** | Turnstile preserves user privacy, does not track users for advertising, eliminates frustrating puzzle capchas, and integrates natively with Cloudflare Workers. |
| **Vulnerability Scanner** | OWASP ZAP (Manual) | **Nuclei + StackHawk** | Fast, template-based dynamic scanning of running web applications and APIs directly within GitHub Actions workflows. |
| **Edge WAF & Bot Defense** | AWS WAF | **Cloudflare Bot Fight Mode + Cloudflare WAF** | Out-of-the-box machine-learning behavioral bot mitigation, managed challenge pages, and automated DDoS protection at the network edge. |

---

## 4. Mandatory Security Checklist for New Features

Every feature branch or Pull Request **must** satisfy this checklist before merging:

### Gate 1: Architecture & Data Sovereignty
- [ ] **Data Minimization:** Does this feature collect *only* the minimum data strictly required to function?
- [ ] **Local-First Integrity:** Does the feature operate completely offline? If network connectivity is lost, does it fail safely without data loss?
- [ ] **No AI Training Without Consent:** Are user notes, audio, or OCR buffers guaranteed never to be passed to third-party model training datasets?

### Gate 2: Input Handling & Cryptography
- [ ] **Input Sanitization:** Are all user inputs, bit titles, premise descriptions, and audio filenames sanitized against XSS, SQL injection, and path traversal?
- [ ] **Zero Cleartext Credentials:** Are all secrets, tokens, and service keys kept out of client-side code and loaded via environment variables / Cloudflare Secrets?
- [ ] **Encryption at Rest:** Is sensitive user data stored locally encrypted via WebCrypto (AES-GCM-256)?
- [ ] **Metadata Stripping:** Are uploaded images and audio files stripped of EXIF, GPS, and device serial metadata on the client side before any processing?

### Gate 3: Network & Edge Security
- [ ] **Strict CORS:** Are API routes and Cloudflare Workers locked to authorized origin domains?
- [ ] **Rate Limiting:** Is every public submission route protected by IP and fingerprint rate limiting?
- [ ] **Content Security Policy (CSP):** Does the feature comply with strict CSP headers (no inline scripts, trusted connect-src only)?
- [ ] **Bot Challenge:** Are unauthenticated public forms guarded by Cloudflare Turnstile?

---

## 5. Feature Security Checker Protocol (Pre-Code Evaluation)

Before engineering any proposed feature (e.g., Cloud Audio Sync, Collaborative Writing, AI Punchline Polisher), run the concept through this 4-step assessment:

```
[Feature Concept]
       ↓
[Step 1: Threat Boundary Analysis]
       ↓
[Step 2: Abuse Case Brainstorming]
       ↓
[Step 3: Cryptographic Storage Plan]
       ↓
[Step 4: Go / No-Go Gate]
```

### Step 1: Threat Boundary Analysis
* Where is the boundary between the comic's private device and the outside network?
* What external services, CDNs, or APIs are touched?
* If the external service is compromised, what is the blast radius?

### Step 2: Abuse Case Brainstorming
* How could a malicious actor abuse this feature to scrape other comedians' jokes?
* Can the endpoint be flooded to cause financial exhaustion (denial of wallet)?
* Could an attacker inject executable payloads into collaborative notes or setlists?

### Step 3: Cryptographic Storage Plan
* Where does the output live? (Memory only, OPFS, IndexedDB, Edge Key-Value).
* What is the time-to-live (TTL)? Is there an automated garbage-collection protocol?
* What happens when the user clicks "Delete All Data"? Does cryptographic erasure take place?

### Step 4: Final Security Clearance Score
A feature can only be developed if it scores a **PASS** on:
1. **User Material Isolation:** 100% private to the creator.
2. **Zero Involuntary Cloud Sync:** Opt-in only.
3. **Automated Threat Test Coverage:** Verifiable via Semgrep/Trivy in CI.
