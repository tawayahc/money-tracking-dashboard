import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def plot_expenses_chart(transactions):
    """
    Plot a bar chart to show the number of expenses for each category by day.

    Args:
        transactions (list): A list of transaction dictionaries with 'date', 'amount', and 'category' keys.
    """
    if not transactions:
        st.info("No transaction data available for the chart.")
        return

    # Convert transactions to a DataFrame
    transactions_df = pd.DataFrame(transactions)
    transactions_df['date'] = pd.to_datetime(transactions_df['date'])

    # Group and pivot data for chart
    daily_expenses = transactions_df.groupby(['date', 'category']).size().unstack(fill_value=0)

    # Plot the chart
    fig, ax = plt.subplots(figsize=(10, 6))
    daily_expenses.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title("Daily Expenses by Category", fontsize=16)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Number of Expenses", fontsize=12)
    ax.legend(title="Category", fontsize=10)

    # Display the chart in Streamlit
    st.pyplot(fig)
