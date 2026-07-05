from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Model Configuration
OPENAI_MODEL = "gpt-4.1-mini"
MISTRAL_MODEL = "mistral-small-latest"

# Application Configuration
APP_NAME = "AI Business Proposal Generator"
APP_VERSION = "1.0.0"

# Output Directory
OUTPUT_DIR = "generated_docs"


def validate_config():
    """
    Validate that required environment variables are present.
    Raises:
        ValueError: If any required environment variable is missing.
    """
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is missing. Check your .env file.")
    if not MISTRAL_API_KEY:
        raise ValueError("MISTRAL_API_KEY is missing. Check your .env file.")
    

