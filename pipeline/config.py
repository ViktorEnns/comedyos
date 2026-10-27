import os
import certifi
from pathlib import Path
from dotenv import load_dotenv

# Base paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

# Pipeline paths
QUEUE_FILE = PROJECT_ROOT / "queue.json"
OUTPUT_DIR = PROJECT_ROOT / "output" / "quotes"
INDEX_FILE = PROJECT_ROOT / "output" / "index.md"
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID", "13ZfCLYpeQoUgcZlhqp6AZcBUz9a-1USrnjAv7JdhObU")

# Model Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

# Discovery queries
DEFAULT_QUERIES = [
    "Joe Rogan Louis CK",
    "Joe Rogan Mark Normand",
    "Your Mom's House",
    "2 Bears 1 Cave",
    "Blocks Podcast Neal Brennan",
    "Conan O'Brien Needs a Friend",
    "Good One: A Podcast About Jokes"
]

# Duration threshold (25 minutes in seconds)
MIN_FULL_EPISODE_DURATION = 25 * 60

# Keywords for shorter clips (<25 min) discussing comedy craft
CRAFT_KEYWORDS = [
    "writing", "write", "joke", "jokes", "craft", "bomb", "bombing", "bombed",
    "heckler", "heckling", "routine", "stagecraft", "process", "special",
    "bit", "bits", "standup", "stand up", "stand-up", "material", "set",
    "timing", "premise", "punchline", "crowd work", "critic", "inner critic",
    "open mic", "rejection", "creative process", "comedy club", "tight five"
]

# Allowed Core Craft Themes
THEMES = [
    "Writing & Joke Construction",
    "Performance & Stagecraft",
    "Mental Attitudes",
    "Overcoming Bombs/Blocks",
    "Professional Problem-Solving"
]

# Chunking constraints
CHUNK_MIN_WORDS = 4000
CHUNK_MAX_WORDS = 6000

# --- Hard Safety Ceilings & Token-Guard Circuit Breakers ---
MAX_TOTAL_TOKENS_PER_RUN = 250_000       # Hard stop across the entire CLI execution
MAX_CHUNKS_PER_VIDEO = 8                 # Stop chunking after ~40k words per video
MAX_CONSECUTIVE_EMPTY_CHUNKS = 3         # Bail on a video if 3 chunks in a row have no craft

# --- Zero-Token Pre-filter Lexicon ---
# Chunk must contain at least 2 of these words to warrant an LLM call:
COMEDY_CRAFT_LEXICON = {
    "joke", "jokes", "writing", "premise", "punchline", "tag", "callback", 
    "bomb", "bombed", "bombing", "heckler", "setlist", "special", "stagecraft", 
    "crowd work", "open mic", "the store", "cellar", "tight five", "hour", 
    "bit", "bits", "routine", "material", "delivery", "timing", "chuckle"
}
MIN_KEYWORD_MATCHES = 2

