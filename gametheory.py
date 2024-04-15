import streamlit as st
import nashpy as nash
import numpy as np
import matplotlib.pyplot as plt


def plot_payoff_matrix():
    # Payoffs from the uploaded image
    payoffs = np.array([[0, 10],   # No alarm: Stay in bed, Get up
                        [-2, 8]])  # Set alarm: Stay in bed, Get up

    # Label for the strategies
    row_labels = ["No alarm", "Set alarm"]
    col_labels = ["Stay in bed", "Get up"]

    fig, ax = plt.subplots()
    ax.set_axis_off()
    table = ax.table(
        cellText=payoffs,
        rowLabels=row_labels,
        colLabels=col_labels,
        rowColours=["gray"] * 2,
        colColours=["gray"] * 2,
        cellLoc='center',
        loc='upper left'
    )

    # Adjust table scale
    table.scale(1, 1.5)
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    ax.set_title('Night self vs Morning self', fontweight='bold', loc='left')

    plt.show()

plot_payoff_matrix()





