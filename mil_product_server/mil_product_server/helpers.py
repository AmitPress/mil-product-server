import os
from dotenv import load_dotenv
load_dotenv("../../.env")

def get_env(key: str) -> str :
    return os.environ[key]