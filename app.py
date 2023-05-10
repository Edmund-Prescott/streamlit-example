import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set up the page layout
st.set_page_config(page_title='Bioinformatics', layout='centered')

# Add some CSS styling to the title element
st.markdown("""
<style>
    .css-1fcmnwj { margin-top: 0; }
    .chart-container {
        max-width: 700px;
        max-height: 500px;
    }
    img {
        max-width: 700px;
        max-height: 300px;
        margin-left: 0px
    }
    div.stSlider{
        max-width: 400px;
    }

    div[data-testid="stHorizontalBlock"] > div:first-of-type {
        width: fit-content;
    }
</style>
""", unsafe_allow_html=True)

# Add a title to the center top of the page
st.title('Bioinformatics')

# Set up the left and right columns
left_column, right_column = st.columns(2)

# TODO: set image orgin to left side


# Add radio button for disease selection
disease = left_column.radio('Select a disease:', ('Rubella', 'Covid', 'Measles'), index=1)

# Add slider for vaccination status
vaccination_status = left_column.slider('Vaccination status:', min_value=0, max_value=95, step=1)

# Add select_slider for mask wearing
mask_wearing_options = ['None', 'Very low', 'Low', 'Medium', 'High', 'Very high']
mask_wearing_labels = ['None', 'Very low', 'Low', 'Medium', 'High', 'Very high']
mask_wearing = left_column.select_slider('Mask wearing:', options=mask_wearing_options, value='Low', format_func=lambda x: mask_wearing_labels[mask_wearing_options.index(x)])

# Add select_slider for social distancing
social_distancing_options = ['None', 'Low', 'Medium', 'High', 'Extreme']
social_distancing_labels = ['None', 'Low', 'Medium', 'High', 'Extreme']
social_distancing = left_column.select_slider('Social distancing:', options=social_distancing_options, value='Low', format_func=lambda x: social_distancing_labels[social_distancing_options.index(x)])


# Generate data for dot map
np.random.seed(0)
num_people = 500
infected = np.random.choice(num_people, int(num_people/10), replace=False)
healthy = np.setdiff1d(np.arange(num_people), infected)
dead = np.random.choice(infected, int(len(infected)/10), replace=False)
colors = np.array(['g'] * num_people)
colors[infected] = 'r'
colors[dead] = 'k'
data = pd.DataFrame({'x': np.random.rand(num_people), 'y': np.random.rand(num_people), 'color': colors})

# Generate data for line chart
num_days = 30
x = np.arange(num_days)
y = np.random.randint(0, 100, size=num_days)

# Plot the dot map and line chart in the right column
with right_column:
    # Dot map
    fig1, ax1 = plt.subplots()
    ax1.scatter(data['x'], data['y'], c=data['color'])
    st.pyplot(fig1)

    # Line chart
    fig2, ax2 = plt.subplots()
    ax2.plot(x, y)
    ax2.set_xlabel('Time (days)')
    ax2.set_ylabel('Diseased people')
    st.pyplot(fig2)
