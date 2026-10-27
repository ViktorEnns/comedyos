/**
 * Comedy OS — Joke Writing Domain Model
 * Based on Jimmy Carr's "On Jokes" Architecture (Setup-Punchline Core + Subservient Blocks)
 */

export type DeliveryCueType = 'pause' | 'vocal_stress' | 'act_out' | 'mic_technique' | 'callback';

export interface DeliveryCue {
  id: string;
  type: DeliveryCueType;
  /** Pause duration in seconds if type === 'pause' */
  duration_seconds?: number;
  /** Vocal stress word or act-out note */
  content: string;
}

export type HitRateTier = 'A' | 'B' | 'C' | 'untested';

export interface PunchlineVariant {
  id: string;
  text: string;
  /** Whether this punchline is currently selected for the live stage setlist */
  is_stage_active: boolean;
  delivery_notes?: string;
  cues: DeliveryCue[];
  hit_rate_tier: HitRateTier;
  average_laugh_duration_seconds: number;
  created_at: string;
  updated_at: string;
}

export type SubservientBlockType = 'bridge' | 'tag' | 'ad_lib_riff';

export interface SubservientBlock {
  id: string;
  type: SubservientBlockType;
  text: string;
  /** Stage execution order relative to the active punchline:
   * 'pre_punch' (bridge/misdirect inserted between setup and punch) or 'post_punch' (tag/topper appended after punch)
   */
  position: 'pre_punch' | 'post_punch';
  sort_order: number;
  is_stage_active: boolean;
  cues: DeliveryCue[];
  average_laugh_duration_seconds?: number;
  discovered_at_venue?: string;
  discovered_from_audio_id?: string;
}

export type JokeLifecycleState = 'draft' | 'testing' | 'stage_ready' | 'retired';

export interface JimmyCarrJokeBit {
  id: string;
  title: string;
  state: JokeLifecycleState;
  
  /** The foundational premise / core comic theory */
  premise: string;
  
  /** The primary set-up: sets the expectation or false narrative */
  setup: {
    text: string;
    cues: DeliveryCue[];
  };
  
  /** Stack of punchline variations — hard turn / paradox / cognitive shatter */
  punchlines: PunchlineVariant[];
  
  /** Subservient tags, bridges, misdirects, and harvested riffs */
  subservient_blocks: SubservientBlock[];
  
  /** Topics & taxonomy */
  topics: string[];
  callbacks_to_bit_ids: string[];
  target_duration_seconds: number;
  
  /** Bi-directional link to continuous scratchpad stream */
  source_stream_ref?: {
    vault_file_path: string;
    line_start: number;
    line_end: number;
  };
  
  created_at: string;
  updated_at: string;
}

/** Ingestion Review Proposed Split (from Whisper audio or raw scratchpad) */
export interface JokeIngestionProposal {
  raw_transcript: string;
  proposed_premise: string;
  proposed_setup: string;
  proposed_punchline: string;
  proposed_tags: string[];
  detected_cues: DeliveryCue[];
  confidence_score: number;
}
