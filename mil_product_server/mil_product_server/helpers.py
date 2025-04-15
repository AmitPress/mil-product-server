import os
from dotenv import load_dotenv
load_dotenv("/app/.env")

def get_env(key: str) -> str :
    return os.environ[key]