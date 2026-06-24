from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
MODEL_NAME = "gpt-4o-mini"         # cheap and fast for development
TEMPERATURE = 0.0                  # deterministic outputs — critical for evaluation
FEW_SHOT_K = 4                     # matches your thesis k=4