import streamlit as st
import pandas as pd

BASE_COLOR_PALETTE = [
    "#AB3428",
    "#E28443",
    "#F49E4C",
    "#98BEA2",
    "#2d728f"
]

def get_adjusted_palette(categories):
    """
    Adjust the palette length to match the number of categories.

    Args:
        categories (list): List of categories.

    Returns:
        list: Adjusted color palette.
    """
    num_categories = len(categories)
    adjusted_palette = [BASE_COLOR_PALETTE[i % len(BASE_COLOR_PALETTE)] for i in range(num_categories)]
    return adjusted_palette

def plot_line_chart(transactions):
    """
    Plot a line chart showing monthly expenses for selected categories using st.line_chart.

    Args:
        transactions (list): A list of transaction dictionaries with 'date', 'amount', and 'category' keys.
    """
    if not transactions:
        st.info("No transaction data available for the line chart.")
        return

    transactions_df = pd.DataFrame(transactions)
    transactions_df['date'] = pd.to_datetime(transactions_df['date'])

    transactions_df['year_month'] = transactions_df['date'].dt.to_period('M').astype(str)

    monthly_expenses = (
        transactions_df.groupby(['year_month', 'category'])['amount']
        .sum()
        .reset_index()
        .pivot(index='year_month', columns='category', values='amount')
        .fillna(0) 
    )

    monthly_expenses = monthly_expenses.sort_index()

    all_categories = list(monthly_expenses.columns)
    selected_categories = st.multiselect(
        "",
        options=all_categories,
        default=all_categories,
    )

    filtered_expenses = monthly_expenses[selected_categories] if selected_categories else monthly_expenses

    st.line_chart(filtered_expenses, color=get_adjusted_palette(filtered_expenses.columns))
