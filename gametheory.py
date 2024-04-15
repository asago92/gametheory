import streamlit as st
import gambit

def create_game():
    game = gambit.Game.new_table([2, 2])
    return game

def solve_game(game):
    solver = gambit.nash.ExternalLCPSolver()
    solver.quiet = True
    solver.solve(game)
    return game.mixed_strategy_profile()
def main():
    st.title("Game Theory App")

    if st.button("Create Game"):
        game = create_game()
        st.success("Game created successfully!")

    if st.button("Solve Game"):
        try:
            strategies = solve_game(game)
            st.write("Mixed Strategy Profile:")
            st.write(strategies)
        except NameError:
            st.error("Please create a game first!")

if __name__ == "__main__":
    main()
