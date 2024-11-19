import streamlit as st
import pandas as pd
from streamlit_apexjs import st_apexcharts

COLOR_PALETTE = [
    "#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#A133FF",
    "#33FFF5", "#F5FF33", "#FF8333", "#8333FF", "#33FF83",
    "#5733FF", "#FF3357", "#33A1FF", "#A1FF33", "#FF5733",
    "#33FFA1", "#FF5733", "#57FF33", "#3357FF", "#FFA133",
    "#FF3383", "#83FF33", "#5733FF", "#A1FF33", "#FF3333",
    "#FF5733", "#3383FF", "#8333FF", "#FF83FF", "#33FFA1"
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
