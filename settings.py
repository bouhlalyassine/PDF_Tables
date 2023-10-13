import json
from pathlib import Path
import requests
import streamlit as st
import os
import base64

TITLE = "PDF Tables"

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# lotties :
lottie_pdf_table = current_dir / "files" / "table_pdf.json"

def load_lottiefile(filepath : str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
