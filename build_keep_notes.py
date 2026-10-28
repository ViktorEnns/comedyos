import json
import glob
import os
import shutil
import re
import sys
from datetime import datetime
from collections import defaultdict

# Force UTF-8 stdout
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SRC_KEEP_DIR = r"G:\OneDrive\- DEV\Google Keep Takeout\extracted\Takeout\Keep"
VAULT_DEST = r"G:\OneDrive\- DEV\comedy os\comedy os obsidian vault\Google Keep Notes"
VAULT_ATTACHMENTS = os.path.join(VAULT_DEST, "attachments")
MIRROR_DEST = r"E:\- CODE\ComedyOS-2026\Comedy_OS_Note_Taker_Vault\Google Keep Notes"
EXISTING_VAULT_ROOT = r"G:\OneDrive\- DEV\comedy os\comedy os obsidian vault"

os.makedirs(VAULT_DEST, exist_ok=True)
os.makedirs(VAULT_ATTACHMENTS, exist_ok=True)

# 1. Load notes
files = glob.glob(os.path.join(SRC_KEEP_DIR, "*.json"))
raw_notes = []
for f in files:
    with open(f, "r", encoding="utf-8") as fp:
        try:
            d = json.load(fp)
            d["_filename"] = os.path.basename(f)
            raw_notes.append(d)
        except Exception:
            pass

print(f"Total raw notes loaded: {len(raw_notes)}")

# 2. Filter Personal / Household notes (Option B)
def is_personal(n):
    title = (n.get("title") or "").strip().lower()
    text = (n.get("textContent") or "").strip().lower()
    labels = [l.get("name", "").lower() for l in n.get("labels", [])]
    full = f"{title} {text} " + " ".join(labels)
    
    if any(l in labels for l in ["recipe", "pancakes", "arzt"]):
        return True
    
    personal_keywords = [
        "rezept", "fluffy pancake", "egg frying recipe", "pelmeni", "blanchieren", "chips no list",
        "bier brot joghurt", "callya rufnummer", "wlan name wird", "vodafone:", "zahnarzt kontrolle",
        "brillen", "jaguar 33843", "ray-ban", "rechtsanwalt plutte", "landewyck", "zugfahrt#4434",
        "walid guettat", "chess.com", "white bebe", "buta 09.10.2026 chess", "cigars left in portugal",
        "pichardo set", "tbilisi", "good chips", "good coffee", "wine summaries", "dream watch",
        "mifcom.de", "android estudio emulator login", "anytype key", "deutsche bahn fehler",
        "plexiglas platte", "popcorn unter zahnfleisch", "elitea aktiv physio", "room 11-04-08", "raum 11-04-08",
        ":now :now"
    ]
    if any(kw in full for kw in personal_keywords):
        if not any(k in full for k in ["slavery is a remote position", "transcendental meditation", "pfand maschine", "cooking with nazis"]):
            return True
            
    if not title and not text and not n.get("attachments"):
        return True
        
    return False

filtered_notes = [n for n in raw_notes if not is_personal(n)]
print(f"Notes kept after filtering personal: {len(filtered_notes)}")

# Helper to sanitize filename
def sanitize_filename(name):
    name = re.sub(r'[\\/*?:"<>|]', '', name)
    name = re.sub(r'[\s_]+', '_', name).strip('_')
    return name[:60] if name else "Untitled_Note"

# Generate title if missing
def derive_title(n):
    t = (n.get("title") or "").strip()
    if t:
        return t
    txt = (n.get("textContent") or "").strip()
    if not txt:
        return f"Note_{n['_filename'][:12]}"
    first_line = txt.split("\n")[0].strip()
    first_line = re.sub(r'^[#\-*>\s]+', '', first_line)
    first_line = re.sub(r'[\\/*?:"<>|]', '', first_line)
    words = first_line.split()[:7]
    title = " ".join(words).strip()
    return title if title else f"Note_{n['_filename'][:12]}"

# 3. Categorize
def classify_note(n):
    title = (n.get("title") or "").strip()
    text = (n.get("textContent") or "").strip()
    labels = [l.get("name", "").lower() for l in n.get("labels", [])]
    full = f"{title} {text} " + " ".join(labels)
    fl = full.lower()
    
    # 1. Comedy & ComedyOS
    comedy_kws = [
        "comedy", "standup", "joke", "jokes", "punchline", "setup", "stage", "bit", "bits", 
        "crowd work", "crowdwork", "open mic", "setlist", "roast", "comedian", "carolines", 
        "heckler", "laugh", "humor", "chappelle", "seinfeld", "carr", "funny is just", 
        "transcendental meditation is the tech bro", "slavery is a remote position", 
        "cooking with nazis", "pfand maschine", "italians, better than", "loneliness and architecture", 
        "funny names", "bombing", "laughter", "teleprompter", "delivery", "cadence"
    ]
    if any(k in fl for k in comedy_kws) or any(l in ["comedy", "standup", "jokes", "comedyos"] for l in labels):
        if any(k in fl for k in ["comedyos", "comedy os", "notation", "teleprompter", "transcript", "comparator", "note taker", "bit database", "laugh map", "surveyors of culture"]):
            return "01_Comedy_and_ComedyOS", "ComedyOS_Architecture_and_Features"
        elif any(k in fl for k in ["roast", "insult", "battle"]):
            return "01_Comedy_and_ComedyOS", "Roast_and_Crowd_Work"
        elif any(k in fl for k in ["delivery", "pause", "rhythm", "cadence", "act-out", "box breathing", "timing"]):
            return "01_Comedy_and_ComedyOS", "Performance_Craft_and_Delivery"
        else:
            return "01_Comedy_and_ComedyOS", "Joke_Premises_and_Bits"

    # 2. AI & LLM Tools
    ai_kws = [
        "prompt", "llm", "gpt", "gemini", "claude", "token", "embedding", "rag", "agent", 
        "model", "whisper", "diffusion", "midjourney", "transformer", "anthropic", "openai", 
        "system prompt", "few-shot", "zero-shot", "chain of thought", "context window", "arxiv"
    ]
    if any(k in fl for k in ai_kws) or any(l in ["ai", "llm", "prompt"] for l in labels):
        if "prompt" in fl or "prompt" in labels or "instruction" in fl:
            return "04_AI_and_UI_Tools", "Prompt_Engineering_and_Metaprompts"
        elif any(k in fl for k in ["whisper", "audio", "transcription", "speech", "voice"]):
            return "04_AI_and_UI_Tools", "Speech_and_Audio_Models"
        elif any(k in fl for k in ["agent", "rag", "embedding", "vector", "architecture"]):
            return "04_AI_and_UI_Tools", "Agent_Architecture_and_LLMs"
        else:
            return "04_AI_and_UI_Tools", "AI_Models_and_Workflows"

    # 3. UI & UX Design Tools
    ui_kws = [
        "ui", "ux", "wireframe", "layout", "design system", "interface", "figma", "typography", 
        "component", "modal", "widget", "dashboard", "user flow", "screen", "interaction", 
        "typeface", "bodoni", "micro-transition", "note taking", "notetaking", "obsidian", 
        "keep", "simplenote", "granite", "waveform"
    ]
    if any(k in fl for k in ui_kws):
        if any(k in fl for k in ["note taking", "notetaking", "notes app", "simplenote", "keep", "obsidian"]):
            return "04_AI_and_UI_Tools", "Note_Taking_UI_and_Ingestion_Patterns"
        elif any(k in fl for k in ["typography", "font", "bodoni", "typeface"]):
            return "04_AI_and_UI_Tools", "Typography_and_Visual_Systems"
        elif any(k in fl for k in ["component", "modal", "overlay", "widget", "waveform", "granite"]):
            return "04_AI_and_UI_Tools", "UI_Components_and_Interactions"
        else:
            return "04_AI_and_UI_Tools", "UX_Principles_and_Flows"

    # 4. Business & Product Strategy
    biz_kws = [
        "business", "pricing", "saas", "revenue", "monetization", "subscription", "mvp", 
        "retention", "churn", "customer", "market", "competitor", "gtm", "pitch", "investor", 
        "roadmap", "feature", "achievements", "pay more", "convenience", "split sheet", "tech sales"
    ]
    if any(k in fl for k in biz_kws) or any(l in ["mvp", "feature"] for l in labels):
        if any(k in fl for k in ["pricing", "monetization", "subscription", "revenue", "pay more", "cac", "ltv"]):
            return "02_Business_and_Strategy", "Pricing_and_Monetization"
        elif any(k in fl for k in ["mvp", "feature", "roadmap", "achievements", "split sheet"]):
            return "02_Business_and_Strategy", "Product_Roadmap_and_Scope"
        else:
            return "02_Business_and_Strategy", "Strategy_and_Value_Proposition"

    # 5. Branding & Marketing
    brand_kws = [
        "brand", "branding", "marketing", "audience", "positioning", "hook", "copywriting", 
        "viral", "social media", "newsletter", "content", "growth", "funnel", "campaign", 
        "landing page", "storytelling", "seo", "trade marks", "logo", "logos", "flickr"
    ]
    if any(k in fl for k in brand_kws) or any(l in ["article"] for l in labels):
        if any(k in fl for k in ["seo", "semrush", "ranking"]):
            return "03_Branding_and_Marketing", "SEO_and_Organic_Growth"
        elif any(k in fl for k in ["logo", "logos", "trade marks", "symbols"]):
            return "03_Branding_and_Marketing", "Visual_Identity_and_Logos"
        elif any(k in fl for k in ["copywriting", "hook", "storytelling", "article"]):
            return "03_Branding_and_Marketing", "Content_and_Copywriting"
        else:
            return "03_Branding_and_Marketing", "Brand_Positioning_and_Growth"

    return "02_Business_and_Strategy", "Strategy_and_Value_Proposition"

# Existing vault architecture links
existing_vault_map = {
    "transcription": "[[13_Whisper_ASR_Speech_To_Text]]",
    "whisper": "[[13_Whisper_ASR_Speech_To_Text]]",
    "audio": "[[10_Audio_Forward_Ingestion_Layer]]",
    "notation": "[[23_Inline_Delivery_Notation_Engine]]",
    "delivery": "[[23_Inline_Delivery_Notation_Engine]]",
    "note taking": "[[20_Text_Forward_Capture_Layer]]",
    "widget": "[[22_Zero_Click_Floating_Capture_Widget]]",
    "comparator": "[[30_The_Comparator_Bridge]]",
    "diff": "[[31_Visual_Diff_Report]]",
    "bit database": "[[40_Atomic_Bit_Database]]",
    "vector": "[[43_Conversational_Semantic_Search_And_Vector_Embeddings]]",
    "semantic": "[[43_Conversational_Semantic_Search_And_Vector_Embeddings]]",
    "jimmy carr": "[[25_Jimmy_Carr_Joke_Writing_Architecture]]",
    "workbench": "[[26_Desktop_Workbench_Mobile_Keep_Supabase_Architecture]]",
    "mobile keep": "[[26_Desktop_Workbench_Mobile_Keep_Supabase_Architecture]]",
    "stagnation": "[[Career_Stagnation]]",
    "bombing": "[[Career_Stagnation]]",
    "disconnect": "[[Audience_Disconnect]]",
    "roast": "[[00_Roast_With_Friends_Master]]",
}

def find_vault_links(text):
    tl = text.lower()
    found = []
    for k, link in existing_vault_map.items():
        if k in tl and link not in found:
            found.append(link)
    return found

# 4. Group notes into clusters (merging duplicate titles / variants)
clusters = defaultdict(list)
for n in filtered_notes:
    raw_t = derive_title(n)
    # Normalize common duplicates like "Comedy os", "Comedy os(1)"
    clean_key = re.sub(r'\(\d+\)$', '', raw_t).strip()
    clusters[clean_key].append(n)

print(f"Total consolidated note clusters: {len(clusters)}")

# Track written notes for glossary / dashboard
written_notes = []

# Process each cluster
for clean_title, note_list in clusters.items():
    # Pick primary category from the cluster
    first_note = note_list[0]
    cat, subcat = classify_note(first_note)
    
    # Destination folder
    target_dir = os.path.join(VAULT_DEST, cat, subcat)
    os.makedirs(target_dir, exist_ok=True)
    
    filename = sanitize_filename(clean_title) + ".md"
    file_path = os.path.join(target_dir, filename)
    
    # Collect all attachments, labels, timestamps
    all_attachments = []
    all_labels = set()
    all_vault_links = set()
    orig_files = []
    timestamps = []
    
    for n in note_list:
        orig_files.append(n["_filename"])
        for l in n.get("labels", []):
            all_labels.add(l.get("name"))
        # timestamps
        ts = n.get("userEditedTimestampUsec") or n.get("createdTimestampUsec")
        if ts:
            dt = datetime.fromtimestamp(ts / 1000000.0)
            timestamps.append(dt)
        # copy attachments
        for att in n.get("attachments", []):
            fp = att.get("filePath")
            if fp:
                src_att = os.path.join(SRC_KEEP_DIR, fp)
                if os.path.exists(src_att):
                    dest_att = os.path.join(VAULT_ATTACHMENTS, fp)
                    if not os.path.exists(dest_att):
                        shutil.copy2(src_att, dest_att)
                    all_attachments.append(fp)
                    
        # find cross-vault links
        links = find_vault_links((n.get("title") or "") + " " + (n.get("textContent") or ""))
        for l in links:
            all_vault_links.add(l)
            
    earliest_date = min(timestamps).strftime("%Y-%m-%d %H:%M:%S") if timestamps else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    latest_date = max(timestamps).strftime("%Y-%m-%d %H:%M:%S") if timestamps else earliest_date
    
    # Clean tags
    tag_list = [f"#{cat.split('_', 1)[-1].lower()}"]
    for l in sorted(all_labels):
        tag_list.append(f"#{l.replace(' ', '-').lower()}")
    tag_list.append("#google-keep-takeout")
    
    # Generate Markdown Content
    md = []
    md.append("---")
    md.append(f'title: "{clean_title.replace("\"", "\\\"")}"')
    md.append(f'created: "{earliest_date}"')
    md.append(f'updated: "{latest_date}"')
    md.append(f'category: "{cat}"')
    md.append(f'subcategory: "{subcat}"')
    md.append(f'source: "Google Keep Takeout"')
    md.append(f'original_files: {json.dumps(orig_files)}')
    md.append(f'tags: {json.dumps(tag_list)}')
    if all_vault_links:
        md.append(f'related_vault_notes: {json.dumps(sorted(list(all_vault_links)))}')
    md.append("---")
    md.append("")
    md.append(f"# {clean_title}")
    md.append("")
    
    # Cross-vault link callout if applicable
    if all_vault_links:
        links_str = " | ".join(sorted(list(all_vault_links)))
        md.append("> [!INFO] Cross-Vault Architecture Connections")
        md.append(f"> **Related System Modules:** {links_str}")
        md.append("")

    # If cluster has multiple variants, present combined master view
    if len(note_list) > 1:
        md.append(f"> [!NOTE] Consolidated Note Cluster ({len(note_list)} Variants)")
        md.append(f"> This note synthesizes {len(note_list)} Google Keep entries with identical or closely related topics.")
        md.append("")
        for idx, n in enumerate(note_list, 1):
            n_title = (n.get("title") or clean_title).strip()
            n_text = (n.get("textContent") or "").strip()
            ts = n.get("userEditedTimestampUsec") or n.get("createdTimestampUsec")
            dt_str = datetime.fromtimestamp(ts / 1000000.0).strftime("%Y-%m-%d %H:%M") if ts else "Undated"
            
            md.append(f"## Variant {idx}: {n_title} `({dt_str})`")
            md.append(f"*Source File: `{n['_filename']}`*")
            md.append("")
            md.append(n_text if n_text else "*(No textual content)*")
            md.append("")
            
            # Variant attachments
            for att in n.get("attachments", []):
                fp = att.get("filePath")
                if fp:
                    md.append(f"![[{fp}]]")
                    md.append("")
            md.append("---")
            md.append("")
    else:
        # Single note
        n_text = (note_list[0].get("textContent") or "").strip()
        md.append(n_text if n_text else "*(No textual content)*")
        md.append("")
        for fp in all_attachments:
            md.append(f"![[{fp}]]")
            md.append("")

    # Footer Metadata
    md.append("")
    md.append("---")
    md.append(f"*Imported from Google Keep Takeout · Created: {earliest_date} · Last Modified: {latest_date}*")
    
    content = "\n".join(md)
    with open(file_path, "w", encoding="utf-8") as fp:
        fp.write(content)
        
    rel_vault_path = os.path.relpath(file_path, VAULT_DEST)
    first_snippet = (note_list[0].get("textContent") or "").replace("\n", " ")[:90]
    written_notes.append({
        "title": clean_title,
        "filename": filename,
        "rel_path": rel_vault_path,
        "category": cat,
        "subcategory": subcat,
        "variants": len(note_list),
        "attachments": len(all_attachments),
        "created": earliest_date,
        "snippet": first_snippet,
        "vault_links": sorted(list(all_vault_links))
    })

print(f"Successfully generated {len(written_notes)} markdown notes in {VAULT_DEST}")

# 5. Generate Master Overview & Visual Dashboard
dashboard_path = os.path.join(VAULT_DEST, "00_Google_Keep_Notes_Overview.md")

total_notes_count = len(written_notes)
total_variants_count = sum(n["variants"] for n in written_notes)
total_attachments_count = len(glob.glob(os.path.join(VAULT_ATTACHMENTS, "*")))

# Group written notes by Category & Subcategory
cat_groups = defaultdict(lambda: defaultdict(list))
for wn in written_notes:
    cat_groups[wn["category"]][wn["subcategory"]].append(wn)

d_md = []
d_md.append("---")
d_md.append('title: "Google Keep Notes — Vault Overview & Visual Dashboard"')
d_md.append(f'created: "{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}"')
d_md.append('tags: ["#dashboard", "#google-keep", "#overview", "#glossary"]')
d_md.append("---")
d_md.append("")
d_md.append("# 🗂️ Google Keep Notes — Vault Dashboard & Topic Glossary")
d_md.append("")
d_md.append("> [!ABSTRACT] Executive Overview")
d_md.append(f"> This visual index consolidates **{total_variants_count} original Google Keep notes** into **{total_notes_count} structured vault entries** with **{total_attachments_count} embedded visual attachments**. Personal grocery lists and household appointments have been excluded, focusing strictly on Comedy, Business Strategy, Branding/Marketing, and AI/UI Architecture.")
d_md.append("")

# KPI Metrics Callouts
d_md.append("## 📊 Vault Intelligence Metrics")
d_md.append("")
d_md.append("| Metric | Count | Description |")
d_md.append("| :--- | :---: | :--- |")
d_md.append(f"| **Active Master Notes** | `{total_notes_count}` | Deduplicated, high-density knowledge entries |")
d_md.append(f"| **Original Keep Entries Synthesized** | `{total_variants_count}` | Raw notes processed and clustered |")
d_md.append(f"| **Embedded Visual Attachments** | `{total_attachments_count}` | Screenshots, UI mockups, whiteboard sketches in `attachments/` |")
d_md.append(f"| **Core Knowledge Domains** | `4` | Comedy & ComedyOS / Business / Branding / AI & UI Tools |")
d_md.append(f"| **Active Subcategories** | `{sum(len(sub) for sub in cat_groups.values())}` | Specialized functional domains |")
d_md.append("")

# Mermaid Visual Architecture Diagram
d_md.append("## 🗺️ Knowledge Domain Map")
d_md.append("")
d_md.append("```mermaid")
d_md.append("graph TD")
d_md.append("    ROOT[\"Google Keep Notes Vault\"] --> C1[\"01. Comedy & ComedyOS\"]")
d_md.append("    ROOT --> C2[\"02. Business & Strategy\"]")
d_md.append("    ROOT --> C3[\"03. Branding & Marketing\"]")
d_md.append("    ROOT --> C4[\"04. AI & UI Tools\"]")
d_md.append("")
d_md.append("    C1 --> C1_1[\"ComedyOS Architecture & Features\"]")
d_md.append("    C1 --> C1_2[\"Joke Premises & Bits\"]")
d_md.append("    C1 --> C1_3[\"Performance Craft & Delivery\"]")
d_md.append("    C1 --> C1_4[\"Roast & Crowd Work\"]")
d_md.append("")
d_md.append("    C2 --> C2_1[\"Pricing & Monetization (LTV/CAC)\"]")
d_md.append("    C2 --> C2_2[\"Product Roadmap & Scope\"]")
d_md.append("    C2 --> C2_3[\"Strategy & Value Proposition\"]")
d_md.append("")
d_md.append("    C3 --> C3_1[\"Brand Positioning & Pitch\"]")
d_md.append("    C3 --> C3_2[\"Visual Identity & Logos\"]")
d_md.append("    C3 --> C3_3[\"SEO & Content Growth\"]")
d_md.append("")
d_md.append("    C4 --> C4_1[\"Prompt Engineering & Metaprompts\"]")
d_md.append("    C4 --> C4_2[\"Agent Architecture & LLMs\"]")
d_md.append("    C4 --> C4_3[\"Note-Taking UI & Ingestion Patterns\"]")
d_md.append("    C4 --> C4_4[\"UI Components & Interactions\"]")
d_md.append("    C4 --> C4_5[\"Speech & Whisper Models\"]")
d_md.append("```")
d_md.append("")

# Category Section Breakdown
d_md.append("## 🗃️ Domain Directories & Categorized Index")
d_md.append("")

category_titles = {
    "01_Comedy_and_ComedyOS": "🎭 01. Comedy & ComedyOS",
    "02_Business_and_Strategy": "💼 02. Business & Strategy",
    "03_Branding_and_Marketing": "🎯 03. Branding & Marketing",
    "04_AI_and_UI_Tools": "⚡ 04. AI & UI Tools"
}

for cat_code in sorted(cat_groups.keys()):
    cat_name = category_titles.get(cat_code, cat_code)
    subcats = cat_groups[cat_code]
    cat_total = sum(len(v) for v in subcats.values())
    
    d_md.append(f"### {cat_name} `({cat_total} notes)`")
    d_md.append("")
    
    for subcat_code, nlist in sorted(subcats.items()):
        subcat_clean = subcat_code.replace("_", " ")
        d_md.append(f"#### 📂 {subcat_clean} `({len(nlist)} entries)`")
        d_md.append("")
        d_md.append("| Note Title | Attachments | Variants | Architecture Backlink | Preview Snippet |")
        d_md.append("| :--- | :---: | :---: | :--- | :--- |")
        
        for n in sorted(nlist, key=lambda x: x["title"].lower()):
            note_link = f"[[{n['title']}]]"
            att_badge = f"📎 {n['attachments']}" if n['attachments'] > 0 else "—"
            var_badge = f"🔄 {n['variants']}" if n['variants'] > 1 else "1"
            vlinks = ", ".join(n["vault_links"]) if n["vault_links"] else "—"
            clean_snippet = n["snippet"].replace("|", "\\|")
            d_md.append(f"| **{note_link}** | {att_badge} | {var_badge} | {vlinks} | {clean_snippet} |")
        d_md.append("")

# Complete Alphabetical Glossary
d_md.append("## 📚 Complete Alphabetical Glossary")
d_md.append("")
d_md.append("| Note Name | Domain | Subcategory | Snippet / Idea |")
d_md.append("| :--- | :--- | :--- | :--- |")
for n in sorted(written_notes, key=lambda x: x["title"].lower()):
    note_link = f"[[{n['title']}]]"
    domain_clean = n["category"].split("_", 1)[-1].replace("_", " ")
    sub_clean = n["subcategory"].replace("_", " ")
    clean_snippet = n["snippet"].replace("|", "\\|")
    d_md.append(f"| **{note_link}** | `{domain_clean}` | `{sub_clean}` | {clean_snippet} |")

d_md.append("")
d_md.append("---")
d_md.append(f"*Dashboard generated automatically on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

with open(dashboard_path, "w", encoding="utf-8") as fp:
    fp.write("\n".join(d_md))

print(f"Master Overview & Visual Dashboard written to: {dashboard_path}")

# 6. Cross-reference existing vault notes
# Check existing vault notes and append a callout if a Keep note adds new variant details
cross_ref_count = 0
for wn in written_notes:
    if wn["vault_links"]:
        for vlink in wn["vault_links"]:
            # extract note name from [[note]]
            base_vname = vlink.replace("[[", "").replace("]]", "")
            # search for matching file in EXISTING_VAULT_ROOT
            matches = glob.glob(os.path.join(EXISTING_VAULT_ROOT, "**", f"{base_vname}.md"), recursive=True)
            for m in matches:
                if "Google Keep Notes" in m:
                    continue
                try:
                    with open(m, "r", encoding="utf-8") as fp:
                        existing_content = fp.read()
                    keep_callout = f"\n\n> [!NOTE] Google Keep Takeout Origin & Variant\n> **Linked Keep Note:** [[{wn['title']}]] (`{wn['category']}/{wn['subcategory']}`)\n> **Insight:** {wn['snippet']}...\n"
                    if f"[[{wn['title']}]]" not in existing_content:
                        with open(m, "a", encoding="utf-8") as fp:
                            fp.write(keep_callout)
                        cross_ref_count += 1
                except Exception:
                    pass

print(f"Appended {cross_ref_count} cross-reference variant callouts to existing vault architecture files.")

# 7. Mirror to E: drive Codebase Vault
print(f"Mirroring Google Keep Notes to codebase vault: {MIRROR_DEST}")
if os.path.exists(MIRROR_DEST):
    shutil.rmtree(MIRROR_DEST)
shutil.copytree(VAULT_DEST, MIRROR_DEST)
print("Mirroring completed successfully!")
