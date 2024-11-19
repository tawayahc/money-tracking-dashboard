import streamlit as st
from virtual_assistant.chatgpt_integration import ChatGPTClient

# Ensure the ChatGPT client is initialized in the session state
if "chatgpt_client" not in st.session_state:
    st.session_state.chatgpt_client = ChatGPTClient()

predefined_queries = [
        "Analyze my expense history and identify categories where I might be overspending. What steps can I take to reduce these costs?",
        "Given my spending habits, how can I adjust my expenses to save for a specific goal, like a vacation or a new gadget?",
        "Looking at my expense history, can you suggest ways to manage my budget during high-spending months like December?",
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
    
    selected_query = st.selectbox("Choose a example prompt:", [""] + predefined_queries)
    
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
