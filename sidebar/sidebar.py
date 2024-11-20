import datetime
import streamlit as st
import json
from PIL import Image

def save_transactions_to_json(file_path="transactions.json"):
    """Save the current transactions to a JSON file."""
    transactions_serializable = [
        {
            **transaction,
            "date": transaction["date"].isoformat() if isinstance(transaction["date"], (str, type(None))) else str(transaction["date"])
        }
        for transaction in st.session_state.transactions
    ]

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(transactions_serializable, file, ensure_ascii=False, indent=4)

def convert_to_standard_date(date_str):
    """
    Convert a date string to the standard format YYYY-MM-DD.
    If the date string is invalid, return today's date in the standard format.
    """
    try:
        possible_formats = [
            "%d %b %y",  
            "%d %B %y", 
            "%d-%m-%y",
            "%d/%m/%y", 
        ]

        for date_format in possible_formats:
            try:
                parsed_date = datetime.strptime(date_str, date_format)
                return parsed_date.strftime("%Y-%m-%d") 
            except ValueError:
                continue

        raise ValueError("Date format not recognized.")
    except Exception:
        return datetime.now().strftime("%Y-%m-%d")

def render_sidebar():
    st.sidebar.title("📝 ADD TRANSACTION HISTORY")
    st.sidebar.markdown("<hr/>", unsafe_allow_html=True)
    
    st.session_state.categories = [cat for cat in st.session_state.categories if cat != "อื่นๆ"] + ["อื่นๆ"]
    
    st.sidebar.header("Add by Image")
    uploaded_files = st.sidebar.file_uploader(
        'Choose your payment slip images',
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    if uploaded_files:
        images = [Image.open(file) for file in uploaded_files]
        ocr = st.session_state.ocr_extractor
        get_info = st.session_state.info_extractor
        extracted_text_list = ocr.extract_text_from_images(images)
        
        for text in extracted_text_list:
            text = " ".join(text)
            extracted_info = get_info.extract_info(text)
            st.toast(f"Extracted info: {extracted_info["Amount"]} Baht {extracted_info["Fee"]} Baht, {extracted_info['Date']}, {extracted_info['Memo']}")
            most_similar_word = ""
            similarity = 0.0
            # Extracted info: 100.0 Baht 0.0 Baht, 29 24, ค่าส่งของ k+ sep

            try:
                most_similar_word, similarity = st.session_state.fasttext_similarity.find_most_similar(
                    extracted_info["Memo"], st.session_state.categories
                )
            except Exception as e:
                st.warning(f"Error: {str(e)}")
                
            extracted_date = convert_to_standard_date(extracted_info["Date"])

            transaction = {
                "date": extracted_date,
                "amount": get_info.correct_amount_fee(extracted_info["Amount"]) + get_info.correct_amount_fee(extracted_info["Fee"]),
                "category": most_similar_word
            }
            st.session_state.transactions.append(transaction)
        st.toast("Successfully added transaction!", icon="✅")
    
    st.sidebar.header("Add by Form")
    with st.sidebar.form(key="transaction_form"):
        selected_date = st.date_input("Date")
        
        selected_amount = st.number_input(
            "Amount (฿: Baht)",
            min_value=0.0,
            step=1.0,
            format="%.2f"
        )
        
        selected_category = st.selectbox(
            "Category",
            options=st.session_state.categories,
        )
        
        submit_button = st.form_submit_button(label="Add Transaction")
        
        if submit_button:
            transaction = {
                "date": selected_date,
                "amount": selected_amount,
                "category": selected_category
            }
            st.session_state.transactions.append(transaction)
            save_transactions_to_json()
            st.toast("Successfully added transaction!", icon="✅")
