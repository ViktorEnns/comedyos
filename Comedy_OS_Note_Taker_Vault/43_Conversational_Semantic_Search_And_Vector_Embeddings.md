---
id: FEAT-DATA-043
title: Semantic Vector Search & Contextual Zero-Tag Indexing
type: system-feature
status: active
tags: [comedy-os, semantic-search, vector-embeddings, invisible-librarian, vertex-ai]
---

# 🧠 Semantic Vector Search & Contextual Zero-Tag Indexing

> **The Invisible Librarian:** Traditional note tags (`#dating`, `#airports`, `#family`) break down when you have 500 bits. You don't remember how you tagged it 3 years ago. Semantic Vector Search finds ideas by conceptual meaning.

```mermaid
flowchart TD
    Raw[Comedian's Notes & Bit Cards] --> Embed[Vertex AI / Local ONNX Embedding Engine]
    Embed --> VecStore[(Vector Database - Cosine Index)]
    Query[Natural Language Prompt:<br/>'Show me premises with A-level laughs in Austin about awkward dating']
    Query --> QEmbed[Query Embedding]
    QEmbed --> Search[Semantic Vector Matching + SQL Filters]
    VecStore --> Search
    Search --> Results[Ranked Bits: 'Tinder date in coffee shop', 'The ex-girlfriend dog custody']
```

## 1. Natural Language Search Queries Supported

- *"Show me crowd work riffs about dentists."*
- *"Find bits that kill in Austin but struggled in New York."*
- *"What jokes do I have where I talk about feeling like an imposter?"*
- *"Show me bits with untested tags written in the last 30 days."*

## 2. Technical Stack
- **Embedding Model:** Local on-device lightweight text embeddings (e.g. `bge-small-en-v1.5` ONNX) backed by cloud sync with `text-embedding-004` on Google Cloud / Vertex AI.
- **Zero-Tag Philosophy:** Automatically extracts latent comedy concepts (e.g. Self-Deprecation, Observational, Absurdist, Crowdwork, Storytelling) without requiring user tagging.
