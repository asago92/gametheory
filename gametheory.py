import streamlit as st
import gambit

def create_game():
    # Define the number of players
    num_players = 2
    # Create a new game with 2 players, each with 2 strategies
    game = gambit.Game.new_table([2, 2])

    # Define the players' labels
    game.players[0].label = "Player 1"
    game.players[1].label = "Player 2"

    # Define strategies
    game.players[0].strategies[0].label = "Wakes Up"
    game.players[0].strategies[1].label = "Doesn't Wake Up"
    game.players[1].strategies[0].label = "Wakes Up"
    game.players[1].strategies[1].label = "Doesn't Wake Up"

    # Define payoffs
    game[0, 0][0] = 1  # Player 1's payoff
    game[0, 0][1] = 1  # Player 2's payoff

    game[0, 1][0] = 0
    game[0, 1][1] = 2

    game[1, 0][0] = 2
    game[1, 0][1] = 0

    game[1, 1][0] = 0
    game[1, 1][1] = 0

    return game

def main():
    st.title("Payoff Matrix for Waking Up Early")

    if st.button("Show Payoff Matrix"):
        game = create_game()
        st.write("Payoff Matrix:")
        st.write(game)

if __name__ == "__main__":
    main()


