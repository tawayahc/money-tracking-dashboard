import streamlit as st
from PIL import Image

def render_sidebar(categories_list):
    st.sidebar.title("📝 ADD TRANSACTION HISTORY")
    st.sidebar.markdown("<hr/>", unsafe_allow_html=True)
    
    # Add transaction by image
    st.sidebar.header("Add by Image")
    uploaded_files = st.sidebar.file_uploader(
        'Choose your payment slip images',
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )
    if uploaded_files:
        images = [Image.open(file) for file in uploaded_files]
        ocr = st.session_state.ocr_extractor
        extracted_text = ocr.extract_text_from_images(images)
        st.write(extracted_text)
        st.toast("Successfully added transaction!", icon="✅")
    
    # Add transaction by form
    st.sidebar.header("Add by Form")
    with st.sidebar.form(key="transaction_form"):
        selected_date = st.date_input("Date")
        
        selected_amount = st.number_input(
            "Amount (฿: Baht)", 
            min_value=0.0, 
            step=0.01, 
            format="%.2f"
        )
        
        selected_category = st.selectbox(
            "Category", 
            categories_list
        )
        
        submit_button = st.form_submit_button(label="Add Transaction")
        
        if submit_button:
            transaction = {
                "date": selected_date,
                "amount": selected_amount,
                "category": selected_category
            }
            st.session_state.transactions.append(transaction)
            st.toast("Successfully added transaction!", icon="✅")
