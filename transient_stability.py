import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def calculate_delta(P_ratio):
    # Calculate the load angle delta using the inverse sine function
    delta = np.arcsin(P_ratio)
    return np.degrees(delta)


def power_vs_delta(P_ratio):
    # Calculate the load angle delta
    delta = calculate_delta(P_ratio)

    # Plot the graph
    delta_values = np.linspace(0, 180, 100)
    P_values = np.sin(np.radians(delta_values))

    fig, ax = plt.subplots()
    ax.plot(delta_values, P_values)
    ax.scatter([delta], [P_ratio], color='red', label='Selected Point')
    ax.set_xlabel('Delta (degrees)')
    ax.set_ylabel('Power (P)')
    ax.set_title('Power vs. Delta')
    ax.legend()
    ax.grid(True)

    # Display the calculated delta value in a separate box
    st.sidebar.subheader("Calculated Delta")
    st.sidebar.text(f"{delta:.2f} degrees")

    st.pyplot(fig)


# Streamlit UI
st.title("Power vs. Delta Plotter")
st.sidebar.header("Input Parameter")

# Input field for P1/Pmax
P_ratio = st.sidebar.number_input(
    "P1/Pmax", min_value=-1.0, max_value=1.0, value=0.0)

# Plot the graph based on user input
power_vs_delta(P_ratio)
