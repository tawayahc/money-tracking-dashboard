import streamlit as st
from .ocr_extractor import OCRExtractor
from .info_extractor import InfoExtractor
from virtual_assistant.chatgpt_integration import ChatGPTClient

def initialize_session_state():
    if "transactions" not in st.session_state:
        st.session_state.transactions = []

    if "ocr_extractor" not in st.session_state:
        st.session_state.ocr_extractor = OCRExtractor()

    if "info_extractor" not in st.session_state:
        st.session_state.info_extractor = InfoExtractor()

    if "chatgpt_client" not in st.session_state:
        st.session_state.chatgpt_client = ChatGPTClient()