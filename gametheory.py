import streamlit as st
import nashpy as nash
import numpy as np

def create_game():
    # Define the payoff matrices for the players
    A = np.array([[1, 0],  # Payoffs when Player 1 wakes up
                  [2, 0]]) # Payoffs when Player 1 doesn't wake up
    B = np.array([[1, 2],  # Payoffs when Player 2 wakes up
                  [0, 0]]) # Payoffs when Player 2 doesn't wake up

    # Create the game
    game = nash.Game(A, B)
    return game

def main():
    st.title("Payoff Matrix for Waking Up Early")

    if st.button("Show Payoff Matrix"):
        game = create_game()
        st.write("Payoff Matrix for Player 1 (Row player):")
        st.write(game.payoff_matrices[0])
        st.write("Payoff Matrix for Player 2 (Column player):")
        st.write(game.payoff_matrices[1])

if __name__ == "__main__":
    main()



