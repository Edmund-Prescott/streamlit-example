import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
df = pd.DataFrame(np.random.randn(100, 2), columns=['x', 'y'])

# Define the slider range
range_slider = st.sidebar.slider('Select range of x values', -3.0, 3.0, (-2.0, 2.0))

# Define the buttons
button1 = st.sidebar.button('Plot Scatter')
button2 = st.sidebar.button('Plot Line')

# Generate the plot based on the button selection
if button1:
    fig, ax = plt.subplots()
    ax.scatter(df['x'], df['y'])
    ax.set_xlim(range_slider)
    st.pyplot(fig)
    
if button2:
    fig, ax = plt.subplots()
    ax.plot(df['x'], df['y'])
    ax.set_xlim(range_slider)
    st.pyplot(fig)
