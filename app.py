import streamlit as st
from category.category_management import manage_categories
from dashboard.bar_chart import plot_expenses_chart
from dashboard.line_chart import plot_line_chart
from dashboard.pie_chart import plot_pie_chart
from sidebar.sidebar import render_sidebar
from utils.session_state import initialize_session_state
from virtual_assistant.chatgpt_integration import ChatGPTClient
from virtual_assistant.chatgpt_ui import render_chatgpt_ui

initialize_session_state()

if "chatgpt_client" not in st.session_state:
    st.session_state.chatgpt_client = ChatGPTClient()

def main():
    
    if "categories" not in st.session_state:
        st.session_state.categories = ["อาหาร", "เดินทาง", "อื่นๆ"]
    
    render_sidebar(st.session_state.categories)

    st.title("Dashboard")
    
    manage_categories()
    
    st.divider()

    if st.session_state.transactions:
        plot_expenses_chart(st.session_state.transactions)
        
        st.divider()
        
        col1, col2 = st.columns([4, 6])

        with col1:
            st.markdown("<div style='margin-top: 45px;'></div>", unsafe_allow_html=True)
            plot_pie_chart(st.session_state.transactions)

        with col2:
            plot_line_chart(st.session_state.transactions)

    st.divider()
    
    render_chatgpt_ui()

if __name__ == "__main__":
    main()
