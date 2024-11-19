import streamlit as st
from sidebar.sidebar import render_sidebar
from utils.session_state import initialize_session_state

initialize_session_state()

def main():
    categories = ["อาหาร", "ขนม", "เดินทาง", "ของใช้", "บ้าน", "อื่น ๆ"]
    
    # Render the sidebar
    render_sidebar(categories)

    # Main content area
    st.title("Dashboard")
    st.write("Welcome to the dashboard!")

    # Display stored transactions
    if st.session_state.transactions:
        st.subheader("Stored Transactions")
        for transaction in st.session_state.transactions:
            st.write(
                f"Date: {transaction['date']}, "
                f"Amount: {transaction['amount']}, "
                f"Category: {transaction['category']}"
            )
    else:
        st.info("No transactions stored yet.")

    # ChatGPT Section
    st.subheader("ChatGPT")
    user_input = st.text_area("Enter your message:")
    if st.button("Send"):
        st.write("You:", user_input)
        # Use ChatGPTClient to send the prompt
        response = st.session_state.chatgpt_client.create_chat(user_input)
        st.write("### ChatGPT Response")
        st.success(response)
    else:
        st.warning("Please enter a valid prompt.")

if __name__ == "__main__":
    main()
