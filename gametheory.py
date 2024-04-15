import streamlit as st
import nashpy as nash
import numpy as np
import matplotlib.pyplot as plt

def create_game():
    # Define the payoff matrices for the players
    A = np.array([[1, 0],  # Payoffs when Player 1 wakes up
                  [2, 0]]) # Payoffs when Player 1 doesn't wake up
    B = np.array([[1, 2],  # Payoffs when Player 2 wakes up
                  [0, 0]]) # Payoffs when Player 2 doesn't wake up

    # Create the game
    game = nash.Game(A, B)
    return game

def plot_payoff_matrix(game):
    # Extract payoff matrices
    payoff_matrix_1 = game.payoff_matrices[0]
    payoff_matrix_2 = game.payoff_matrices[1]

    # Combine payoffs into a single string for display
    combined_payoffs = np.array([[f"{payoff_matrix_1[i, j]}\n{payoff_matrix_2[i, j]}"
                                  for j in range(payoff_matrix_1.shape[1])]
                                 for i in range(payoff_matrix_1.shape[0])])

    fig, ax = plt.subplots()
    # Create a table with the combined payoffs
    table = ax.table(cellText=combined_payoffs, colLabels=["Wakes Up", "Doesn't Wake Up"], rowLabels=["Player 1", "Player 2"], cellLoc='center', loc='center')

    # Hide axes
    ax.axis('off')
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    table.scale(1, 2)  # scale column widths and row heights

    return fig

def main():
    st.title("Payoff Matrix for Waking Up Early")

    if st.button("Show Payoff Matrix"):
        game = create_game()
        fig = plot_payoff_matrix(game)
        st.pyplot(fig)

if __name__ == "__main__":
    main()




