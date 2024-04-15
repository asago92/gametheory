import streamlit as st
import gambit

def create_game():
    # Define the players and actions
    players = ["Player 1 (Wakes Up)", "Player 2 (Doesn't Wake Up)"]
    actions = ["Wakes Up", "Doesn't Wake Up"]

    # Create the game
    game = gambit.NormalFormGame(players, actions)

    # Define payoffs
    game[0, 0] = (1, 1)  # Player 1 wakes up, Player 2 wakes up
    game[0, 1] = (0, 2)  # Player 1 wakes up, Player 2 doesn't wake up
    game[1, 0] = (2, 0)  # Player 1 doesn't wake up, Player 2 wakes up
    game[1, 1] = (0, 0)  # Player 1 doesn't wake up, Player 2 doesn't wake up

    return game

def main():
    st.title("Payoff Matrix for Waking Up Early")

    if st.button("Show Payoff Matrix"):
        game = create_game()
        st.write("Payoff Matrix:")
        st.write(game)

if __name__ == "__main__":
    main()

