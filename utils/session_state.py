import streamlit as st
from .ocr_extractor import OCRExtractor
from .info_extractor import InfoExtractor

def initialize_session_state():
    if "transactions" not in st.session_state:
        st.session_state.transactions = []

    if "ocr_extractor" not in st.session_state:
        st.session_state.ocr_extractor = OCRExtractor()

    if "info_extractor" not in st.session_state:
        st.session_state.info_extractor = InfoExtractor()