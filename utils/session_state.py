import json
import streamlit as st
from .ocr_extractor import OCRExtractor
from .info_extractor import InfoExtractor
from datetime import datetime

def load_categories_from_json(file_path="categories.json"):
    """Load categories from a JSON file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return ["อาหาร", "เดินทาง", "อื่นๆ"]

def load_transactions_from_json(file_path="transactions.json"):
    """Load transactions from a JSON file and convert dates back to datetime.date."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            transactions = json.load(file)
            for transaction in transactions:
                if "date" in transaction:
                    transaction["date"] = datetime.strptime(transaction["date"], "%Y-%m-%d").date()
            return transactions
    except FileNotFoundError:
        return []

def initialize_session_state():
    if "transactions" not in st.session_state:
        st.session_state.transactions = load_transactions_from_json()

    if "ocr_extractor" not in st.session_state:
        st.session_state.ocr_extractor = OCRExtractor()

    if "info_extractor" not in st.session_state:
        st.session_state.info_extractor = InfoExtractor()
        
    if "categories" not in st.session_state:
        st.session_state.categories = load_categories_from_json()