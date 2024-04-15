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
    fig, ax = plt.subplots()
    matrix = np.dstack(game.payoff_matrices)
    cax = ax.matshow(matrix, cmap='coolwarm')

    # Set up axes
    ax.set_xticklabels([''] + ["Wakes Up", "Doesn't Wake Up"], rotation=45)
    ax.set_yticklabels([''] + ["Player 1", "Player 2"])

    # Loop over data dimensions and create text annotations.
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, f'{game.payoff_matrices[0][i, j]}\n{game.payoff_matrices[1][i, j]}', ha='center', va='center', color='black')

    plt.colorbar(cax, ax=ax)
    return fig

def main():
    st.title("Payoff Matrix for Waking Up Early")

    if st.button("Show Payoff Matrix"):
        game = create_game()
        fig = plot_payoff_matrix(game)
        st.pyplot(fig)

if __name__ == "__main__":
    main()




