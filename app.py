import streamlit as st
from section.category_management import manage_categories
from section.dashboard import plot_expenses_chart
from sidebar.sidebar import render_sidebar
from utils.session_state import initialize_session_state

initialize_session_state()

def main():
    
    if "categories" not in st.session_state:
        st.session_state.categories = ["อาหาร", "เดินทาง", "อื่นๆ"]
    
    # Render the sidebar
    render_sidebar(st.session_state.categories)

    # Main content area
    st.title("Dashboard")
    
    manage_categories()
    
    # Display stored transactions
    st.write("Welcome to the dashboard!")

    if st.session_state.transactions:
        st.subheader("Stored Transactions")
        for transaction in st.session_state.transactions:
            st.write(
                f"Date: {transaction['date']}, "
                f"Amount: {transaction['amount']}, "
                f"Category: {transaction['category']}"
            )

        # Call the chart function
        st.subheader("Expenses by Category and Day")
        plot_expenses_chart(st.session_state.transactions)
    else:
        st.info("No transactions stored yet.")

if __name__ == "__main__":
    main()
