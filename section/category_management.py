import streamlit as st

def manage_categories():
    """Render category management UI and handle interactions."""
    st.subheader("Manage Categories")
    with st.form(key="add_category_form"):
        new_category = st.text_input("Add New Category", value="")
        add_category_button = st.form_submit_button(label="Add Category")
        if add_category_button:
            if new_category.strip() and new_category not in st.session_state.categories:
                st.session_state.categories.append(new_category.strip())
                st.success(f"Category '{new_category}' added!")
            elif new_category in st.session_state.categories:
                st.warning(f"Category '{new_category}' already exists!")
            else:
                st.error("Category name cannot be empty!")

    # Display all categories with your custom layout logic
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("Categories")
    if st.session_state.categories:
        # Inject custom CSS for horizontal scrolling and the 2-row, 3-column layout
        st.markdown(
            """
            <style>
            .scroll-container {
                display: grid;
                grid-template-rows: repeat(2, 1fr); /* Two rows */
                grid-auto-flow: column; /* Flow items horizontally */
                grid-auto-columns: minmax(150px, 1fr); /* Each column takes a fixed size */
                gap: 10px; /* Spacing between items */
                overflow-x: auto; /* Enable horizontal scrolling */
                overflow-y: hidden; /* Prevent vertical scrolling */
                padding: 10px;
                white-space: nowrap; /* Prevent wrapping */
                max-width: 100%;
            }
            .scroll-container > div {
                display: flex;
                justify-content: center;
                align-items: center;
                min-width: 150px; /* Box size */
                min-height: 150px; /* Box size */
                text-align: center; 
                border: 1px solid #ddd; 
                border-radius: 5px; 
                background-color: #f9f9f9;
                box-sizing: border-box;
                overflow: hidden;
                word-wrap: break-word; /* Allow wrapping for long words */
                padding: 10px;
            }
            .scroll-container > div span {
                display: inline-block;
                max-width: 100%;
                text-overflow: ellipsis;
                white-space: normal; /* Allow wrapping */
                font-size: 14px; /* Adjust font size */
                word-break: break-word; /* Break words if too long */
                overflow-wrap: break-word; /* Ensure wrapping works in all browsers */
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Generate the HTML for the categories
        categories_html = '<div class="scroll-container">'
        for category in st.session_state.categories:
            categories_html += f'<div><span>{category}</span></div>'
        categories_html += '</div>'

        st.markdown(categories_html, unsafe_allow_html=True)
    else:
        st.info("No categories available.")
