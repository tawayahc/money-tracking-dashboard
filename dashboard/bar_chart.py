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

def plot_expenses_chart(transactions):
    """
    Plot a bar chart to show the number of expenses for each category grouped by day, month, or year using st.bar_chart.

    Args:
        transactions (list): A list of transaction dictionaries with 'date', 'amount', and 'category' keys.
    """
    if not transactions:
        st.info("No transaction data available for the chart.")
        return

    transactions_df = pd.DataFrame(transactions)
    transactions_df['date'] = pd.to_datetime(transactions_df['date'])

    group_by = st.selectbox("", ["Day", "Month", "Year"])

    if group_by == "Day":
        transactions_df['grouped_date'] = transactions_df['date'].dt.strftime('%Y-%m-%d')
    elif group_by == "Month":
        transactions_df['grouped_date'] = transactions_df['date'].dt.strftime('%Y-%m')
    elif group_by == "Year":
        transactions_df['grouped_date'] = transactions_df['date'].dt.strftime('%Y')

    grouped_expenses = (
        transactions_df.groupby(['grouped_date', 'category'])['amount']
        .sum()
        .unstack(fill_value=0)  
    )
    st.bar_chart(grouped_expenses, color=get_adjusted_palette(grouped_expenses.columns))
