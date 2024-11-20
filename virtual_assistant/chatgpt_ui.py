import streamlit as st
from virtual_assistant.chatgpt_integration import ChatGPTClient

# Ensure the ChatGPT client is initialized in the session state
if "chatgpt_client" not in st.session_state:
    st.session_state.chatgpt_client = ChatGPTClient()

predefined_queries = [
    "What is the best category to reduce spending in based on 2024 data? 1. Group transactions by category and sum the amount for each. 2. Identify the category with the highest total spending. 3. Suggest reducing spending in this category to save more.",
    "Which month would be best to budget more for 'บิล' payments in 2024? 1. Filter transactions by category = 'บิล' and year = 2024. 2. Group by month and calculate the total amount for each. 3. Identify the month with the highest spending on 'บิล' and recommend increasing the budget for it.",
    "What category should have a higher budget allocation in 2025 based on past spending trends?  1. Compare total spending per category across the years 2023-2024. 2. Identify the category with consistent or increasing spending. 3. Suggest allocating more budget for this category in 2025.",
    "Are there any unusual spikes in spending for 'ช็อปปิ้ง' in 2024? 1. Filter transactions by category = 'ช็อปปิ้ง' and year = 2024. 2. Group by month and calculate the total spending for each month. 3. Identify months with spending significantly higher than the monthly average and flag them as unusual spikes.",
    "How can transportation costs ('เดินทาง') be optimized in 2024? 1. Filter transactions by category = 'เดินทาง' and year = 2024. 2. Calculate the average spending per transaction. 3. Suggest strategies to optimize transportation costs, such as reducing trips or choosing cost-effective options, based on transaction data.",
    "What is the total amount spent on 'อาหาร' in 2024? 1. Filter transactions by category = 'อาหาร' and year = 2024. 2. Sum the amount field for these transactions. 3. Return the total.",
    "Which category has the highest total spending in 2024? 1. Filter transactions by year = 2024. 2. Group by category and calculate the total amount for each. 3. Identify the category with the highest total.",
    "What is the average amount spent per transaction on 'เดินทาง'? 1. Filter transactions by category = 'เดินทาง'. 2. Calculate the average of the amount field for these transactions. 3. Return the result.",
    "How many transactions were made in November 2024?  1. Filter transactions by month = 11 and year = 2024. 2. Count the total number of transactions. 3. Return the count.",
    "What is the largest transaction in the 'ช็อปปิ้ง' category?  1. Filter transactions by category = 'ช็อปปิ้ง'. 2. Find the maximum value in the amount field for these transactions. 3. Return the maximum value and its corresponding date.",
    "Which month in 2024 had the highest spending overall? 1. Filter transactions by year = 2024. 2. Group transactions by month and sum the amount for each month. 3. Identify the month with the highest total spending.",
    "How many transactions were made for 'บิล' in 2023 and 2024 combined? 1. Filter transactions by category = 'บิล' and years = 2023 or 2024. 2. Count the total number of transactions. 3. Return the count.",
    "What is the most frequent transaction amount in the 'อื่นๆ' category? 1. Filter transactions by category = 'อื่นๆ'. 2. Count occurrences of each amount value. 3. Identify the amount value that appears most frequently.",
    "How does spending on 'เดินทาง' compare to 'อาหาร' in 2025? 1. Filter transactions by year = 2025 and categories = 'เดินทาง', 'อาหาร'. 2. Calculate the total amount for each category. 3. Compare the totals and return the difference or ratio.",
    "What is the total spending across all categories for each year? 1. Group transactions by year and sum the amount for each year. 2. Return the total spending per year."
]

def render_chatgpt_ui():
    """
    Renders the ChatGPT API key input and chat interface in the Streamlit app.
    """
    st.markdown(
        """
        <style>
        input[type="password"]::-ms-reveal,
        input[type="password"]::-ms-clear {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    st.subheader("API Key")
    api_key_input = st.text_input(
        "Enter your OpenAI API Key",
        value="",
        placeholder="sk-xxxxxxxx",
        type="password",
    )
    if st.button("Set API Key"):
        if api_key_input:
            st.session_state.chatgpt_client.set_api_key(api_key_input)
            st.success("API key set successfully.")
        else:
            st.warning("Please enter a valid API key.")
    
    st.subheader("ChatGPT")
    
    selected_query = st.selectbox("Choose an example prompt:", [""] + predefined_queries)
    
    user_input = st.text_area(
        "Enter your message:",
        value=selected_query if selected_query else "",
    )

    if st.button("Send with transaction history"):
        if not st.session_state.chatgpt_client.api_key:
            st.warning("Please enter a valid API key.")
        elif not st.session_state.transactions:
            st.warning("No transaction data available to send.")
        else:
            # Prepare the payload with user input and transactions
            transactions = st.session_state.transactions
            full_prompt = f"{user_input}\n\nHere is my transaction history:\n{transactions}"
            
            st.write("You:", user_input)
            response = st.session_state.chatgpt_client.create_chat(full_prompt)
            st.write("### ChatGPT Response")
            st.success(response)
