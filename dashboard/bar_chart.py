import streamlit as st
import pandas as pd

BASE_COLOR_PALETTE = [
    "#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF",
    "#33FFF5", "#F5FF33", "#FF8333", "#8333FF", "#33FF83",
    "#5733FF", "#FF3357", "#33A1FF", "#A1FF33", "#FF5733",
    "#33FFA1", "#FF5733", "#57FF33", "#3357FF", "#FFA133",
    "#FF3383", "#83FF33", "#5733FF", "#A1FF33", "#FF3333",
    "#FF5733", "#3383FF", "#8333FF", "#FF83FF", "#33FFA1"
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