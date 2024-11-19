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
