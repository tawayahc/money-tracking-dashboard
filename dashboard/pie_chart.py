import streamlit as st
import pandas as pd
from streamlit_apexjs import st_apexcharts

COLOR_PALETTE = [
    "#AB3428",
    "#E28443",
    "#F49E4C",
    "#98BEA2",
    "#2d728f"
]


def plot_pie_chart(transactions):
    """
    Plot a pie chart to show the percentage of each category using st_apexcharts.

    Args:
        transactions (list): A list of transaction dictionaries with 'amount' and 'category' keys.
    """
    if not transactions:
        st.info("No transaction data available for the pie chart.")
        return

    transactions_df = pd.DataFrame(transactions)

    category_totals = transactions_df.groupby("category")["amount"].sum()

    category_colors = [
        COLOR_PALETTE[i % len(COLOR_PALETTE)] for i in range(len(category_totals))
    ]

    options = {
        "chart": {
            "toolbar": {
                "show": False  
            }
        },
        "labels": category_totals.index.tolist(),
        "colors": category_colors,
        "legend": {
            "show": True,
            "position": "bottom",
        }
    }

    series = category_totals.values.tolist()

    st_apexcharts(options, series, 'donut', '450')
