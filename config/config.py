from os import path
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
COOKIE_PATH = path.join(BASE_DIR, "cookies/cookies.txt")
