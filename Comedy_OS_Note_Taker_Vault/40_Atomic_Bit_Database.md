---
id: LAYER-DATA-040
title: Atomic Bit Vault & Object Schema
type: architecture-layer
status: active
tags: [comedy-os, bit-vault, schema, object-oriented, atomic-notes, jimmy-carr]
---

# 🧱 Atomic Bit Vault & Object Schema

> **Jokes as Domain Objects:** In Comedy OS, a joke is not an unstructured string in a notes document. It is a structured **Atomic Bit Object** implementing Jimmy Carr's "On Jokes" architecture: a foundational Premise, an expectation-setting Set-up, a cognitive-turn Punchline stack (with stage-active toggling), and modular subservient blocks (bridges, tags, toppers, and harvested riffs).

## 1. Bit Data Schema (Jimmy Carr Architecture)

```typescript
import {
  JimmyCarrJokeBit,
  PunchlineVariant,
  SubservientBlock,
  DeliveryCue,
  HitRateTier,
  JokeLifecycleState
} from 'comedyos-app';

export interface AtomicBit extends JimmyCarrJokeBit {
  // Performance History Run log
  run_history: Array<{
    tape_id: string;
    venue: string;
    city: string;
    date: string;
    laugh_duration_seconds: number;
    dropped_tags: string[];
    selected_punchline_id: string;
  }>;
}
```

### Full Expanded Object Schema

```typescript
export interface JimmyCarrJokeBit {
  id: string; // e.g. "bit_tsa_security_2026"
  title: string; // "TSA Airport Security"
  state: 'draft' | 'testing' | 'stage_ready' | 'retired';
  
  // 1. Foundational Premise / Concept Angle
  premise: string; // "TSA is security theater designed to humiliate passengers"
  
  // 2. Set-up: The false expectation / narrative trap
  setup: {
    text: string;
    cues: DeliveryCue[]; // [pause: 1.5s], vocal stress, act-outs
  };
  
  // 3. Punchline Stack: The hard cognitive turn / paradox
  punchlines: Array<{
    id: string;
    text: string;
    is_stage_active: boolean; // Currently armed for live setlist
    delivery_notes?: string;
    cues: DeliveryCue[];
    hit_rate_tier: 'A' | 'B' | 'C' | 'untested';
    average_laugh_duration_seconds: number;
    created_at: string;
    updated_at: string;
  }>;
  
  // 4. Subservient Blocks: Bridges, Tags, Toppers, Harvested Riffs
  subservient_blocks: Array<{
    id: string;
    type: 'bridge' | 'tag' | 'ad_lib_riff';
    text: string;
    // 'pre_punch' (bridge/misdirect inserted between setup and punch)
    // 'post_punch' (tag/topper appended after punch)
    position: 'pre_punch' | 'post_punch';
    sort_order: number;
    is_stage_active: boolean;
    cues: DeliveryCue[];
    average_laugh_duration_seconds?: number;
    discovered_at_venue?: string;
    discovered_from_audio_id?: string;
  }>;

  // Setlist & Categorization
  target_duration_seconds: number;
  topics: string[]; // ["travel", "paranoia", "government"]
  callbacks_to_bit_ids: string[];
  
  // Bi-directional link to continuous scratchpad stream
  source_stream_ref?: {
    vault_file_path: string;
    line_start: number;
    line_end: number;
  };

  created_at: string;
  updated_at: string;
}
```

## 2. Component Nodes
- [[25_Jimmy_Carr_Joke_Writing_Architecture|2.5 Jimmy Carr Joke Writing Screen & Interaction Architecture]]
- [[41_Jokes_As_Living_Objects_State_Machine|4.1 Jokes as Living Objects (Lifecycle State Machine)]]
- [[42_Drag_And_Drop_Modular_Setlist_Timeline|4.2 Drag-and-Drop Modular Setlist Timeline]]
- [[43_Conversational_Semantic_Search_And_Vector_Embeddings|4.3 Semantic Vector Search & Contextual Zero-Tag Indexing]]
