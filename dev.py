import streamlit as st
import os
from PIL import Image

# Set page to wide mode
st.set_page_config(layout="wide")

# Custom CSS to maximize space and style radio captions
custom_css = """
    <style>
    /* Remove Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Maximize content width */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }
    
    /* Center and style title */
    .title-container {
        display: flex;
        justify-content: center;
        width: 100%;
        margin-bottom: 2rem;
    }
    
    .title-text {
        font-size: 2.5rem !important;
        font-weight: bold;
        white-space: nowrap;
        text-align: center;
    }
    
    /* Style radio buttons and labels */
    div[data-testid="stRadio"] > label {
        font-size: 1.5rem !important;
        padding-bottom: 1rem;
        font-weight: bold !important;  /* Make captions bold */
    }
    
    /* Make radio options horizontal */
    div[data-testid="stRadio"] > div {
        display: flex !important;
        flex-direction: row !important;
        gap: 1rem !important;
    }
    
    /* Style individual radio options */
    div[data-testid="stRadio"] > div > div {
        margin-right: 1rem !important;
    }

    .radio-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 100%;
    }
    
    /* Ensure images scale properly */
    img {
        width: 100% !important;
        height: auto !important;
    }
    
    /* Adjust caption size */
    .caption {
        font-size: 1.2rem !important;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Display centered title
st.markdown(
    '<div class="title-container"><div class="title-text">Likelihood of South African Load Shedding</div></div>',
    unsafe_allow_html=True
)

# Add vertical spacing
st.write("")
st.write("")

# Define the folder containing the images
image_folder = "grid_imgs"
leg_file = "legend.png"

# Define label mappings
demand_options = ["None", "High"]
fuel_options = ["100% of 2024", "60% of 2024"]
delay_options = ["No delay", "12-month delay"]

key_demand = {"None": "D3", "High": "D5"}
key_fuel = {"100% of 2024": "125TJ", "60% of 2024": "75TJ"}
key_delay = {"No delay": "ND", "12-month delay": "12D"}

# Create a three-column layout for main content
col1, col2, col3 = st.columns([2, 2, 2])

with col1:  # Left column for description image and selections
    image = Image.open('grid_imgs/text_description.png')
    st.image(image)

    # New columns for radio buttons

    rcol1, rcol2, rcol3 = st.columns([1,2,1])

    with rcol2:
    
        st.write("")
        
        # Radio buttons with horizontal options and bold captions
        index1 = st.radio(
            "**Annual electricity demand growth**",
            options=demand_options,
            index=0,
            key="demand_radio"
        )
        index2 = st.radio(
            "**OCGT daily diesel consumption limit**",
            options=fuel_options,
            index=1,
            key="fuel_radio"
        )
        index3 = st.radio(
            "**New-build commissioning delay**",
            options=delay_options,
            index=1,
            key="delay_radio"
        )

with col3:  # Right column for legend
    leg_path = os.path.join(image_folder, leg_file)
    st.image(leg_path)

# Construct the image filename
image_file = os.path.join(image_folder, f"{key_demand[index1]} {key_fuel[index2]} {key_delay[index3]}.png")

with col2:  # Middle column for the main image
    if os.path.exists(image_file):        
        # Create placeholder for image
        image_placeholder = st.empty()
        
        # Load and display the new image directly
        image = Image.open(image_file)
        image_placeholder.image(image, caption="")
            
    else:
        st.error("Image file not found. Make sure the images exist in the script directory.")