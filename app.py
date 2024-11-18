import streamlit as st
from sidebar.sidebar import render_sidebar

if "transactions" not in st.session_state:
    st.session_state.transactions = []

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

if __name__ == "__main__":
    main()
