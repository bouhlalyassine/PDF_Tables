import json
from pathlib import Path
import requests
import streamlit as st
import os
import base64

TITLE = "PDF Tables"
PAGE_ICON ="ico_potfolio.ico"


current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()


# CSS
css_file = current_dir / "main.css"


# My Tutos :
# size :
space = 15
tuto_space = 70

tuto_tabl_p = current_dir / "files" / "tuto_ext_tbl_pdf.mp4"
tuto_tabl = str(tuto_tabl_p)

pp_logo_portfolio = current_dir / "files" /  "logo_portfolio.png"
linkpic_code = current_dir / "files" /  "code.png"


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


# Clickable img
@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

@st.cache_data
def get_img_with_href(local_img_path, target_url, width, loc):
    img_format = os.path.splitext(local_img_path)[-1].replace('.', '')
    bin_str = get_base64_of_bin_file(local_img_path)
    html_code = f'''
        <a href="{target_url}" target="_{loc}" style="display: flex; justify-content: center; align-items: center;">
            <img src="data:image/{img_format};base64,{bin_str}" width="{width}" class="img-hover-effect">
        </a>'''
    return html_code