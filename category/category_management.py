import streamlit as st
import json
from category.styles import get_styles

def save_categories_to_json(file_path="categories.json"):
    """Save the current categories to a JSON file."""
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(st.session_state.categories, file, ensure_ascii=False, indent=4)

def calculate_totals():
    """Calculate total amounts for each category."""
    totals = {category: 0 for category in st.session_state.categories} 
    for transaction in st.session_state.transactions:
        category = transaction.get("category", "อื่นๆ") 
        amount = transaction.get("amount", 0)
        if category in totals:
            totals[category] += amount
    return totals

def manage_categories():
    """Render category management UI and handle interactions."""

    st.markdown(get_styles(), unsafe_allow_html=True)
    
    if "new_category" not in st.session_state:
        st.session_state.new_category = ""

    new_category = st.text_input(
        "Add New Category",
        value=st.session_state.new_category,  
        placeholder="Enter a new category and press Enter",  
        label_visibility="collapsed", 
        key="category_input", 
    )

    if new_category != st.session_state.new_category:  
        st.session_state.new_category = new_category.strip() 
        if st.session_state.new_category and st.session_state.new_category not in st.session_state.categories:
            st.session_state.categories.append(st.session_state.new_category)
            st.session_state.categories = [cat for cat in st.session_state.categories if cat != "อื่นๆ"] + ["อื่นๆ"]
            save_categories_to_json() 
            st.toast(f"Category '{st.session_state.new_category}' added!", icon="✅")
        elif st.session_state.new_category in st.session_state.categories:
            st.toast(f"Category '{st.session_state.new_category}' already exists!", icon="❌")
        else:
            st.toast("Category name cannot be empty!", icon="❌")
        st.session_state.new_category = ""  

    if st.session_state.categories:
        totals = calculate_totals()

        categories_html = '<div class="scroll-container">'
        for category in st.session_state.categories:
            total = totals.get(category, 0)  
            categories_html += f'<div><span>{category}<br>฿{total:,.2f}</span></div>'
        categories_html += '</div>'

        st.markdown(categories_html, unsafe_allow_html=True)
    else:
        st.info("No categories available.")
