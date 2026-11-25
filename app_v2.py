"""StegoVault 2.0 - hosts the HTML website inside Streamlit.
Run locally:  streamlit run app_v2.py
Needs index.html in the same folder as this file."""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="StegoVault 2.0", page_icon="🔐",
                   layout="wide", initial_sidebar_state="collapsed")

# remove Streamlit's own padding/header so the website fills the page
st.markdown("""
<style>
[data-testid="stHeader"], [data-testid="stToolbar"], footer {display:none !important;}
.block-container {padding:0 !important; max-width:100% !important;}
iframe {border:0 !important;}
</style>
""", unsafe_allow_html=True)

html = (Path(__file__).parent / "index.html").read_text(encoding="utf-8")
components.html(html, height=1800, scrolling=True)
