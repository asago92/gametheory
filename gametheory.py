import streamlit as st
import nashpy as nash
import numpy as np
import matplotlib.pyplot as plt

# Define the payoffs for both players
# Player 1 (Night self) is the row player, Player 2 (Morning self) is the column player
A = np.array([[0, 10],   # No alarm: Stay in bed, Get up
              [-2, 8]])  # Set alarm: Stay in bed, Get up
B = np.array([[10, 0],   # No alarm: Stay in bed, Get up
              [-5, -1]]) # Set alarm: Stay in bed, Get up

st.set_option('deprecation.showPyplotGlobalUse', False)

# Create the game
game = nash.Game(A, B)

def plot_payoff_matrix(A, B):
    # Labels for the strategies
    row_labels = ["No alarm", "Set alarm"]
    col_labels = ["Stay in bed", "Get up"]
    
    fig, ax = plt.subplots()
    ax.set_axis_off()
    
    # Combining the payoffs into a single matrix for display
    combined_payoffs = np.dstack((A, B)).astype(str)
    combined_payoff_text = np.core.defchararray.add(combined_payoffs[:, :, 0], ", ")
    combined_payoff_text = np.core.defchararray.add(combined_payoff_text, combined_payoffs[:, :, 1])
    
    # Create the table
    table = ax.table(cellText=combined_payoff_text,
                     rowLabels=row_labels,
                     colLabels=col_labels,
                     rowColours=["gray"] * 2,
                     colColours=["gray"] * 2,
                     cellLoc='center',
                     loc='center')
    
    # Adjust table scale and fontsize
    table.scale(1, 1.5)
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    ax.set_title('Night self vs Morning self', fontweight='bold', loc='left')
    
    plt.show()

def main():
    st.title("Payoff Matrix for Night Self vs Morning Self")

    if st.button("Show Payoff Matrix"):
        # Plot and display the payoff matrix
        fig = plot_payoff_matrix(A, B)
        st.pyplot(fig)

if __name__ == "__main__":
    main()






