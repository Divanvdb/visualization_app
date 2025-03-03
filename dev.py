import streamlit as st
import os
from PIL import Image
import time

# Set page to wide mode
st.set_page_config(layout="wide")

# Custom CSS to maximize space and increase element sizes
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
    
    /* Increase title font size */
    .title-text {
        font-size: 2.5rem !important;
        font-weight: bold;
        white-space: nowrap;
    }
    
    /* Increase slider label size */
    .stSelectSlider label {
        font-size: 1.5rem !important;
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

# Display title
st.markdown('<div class="title-text">Likelihood of South African Load Shedding</div>', unsafe_allow_html=True)

# Add vertical spacing
st.write("")
st.write("")

# Define the folder containing the images
image_folder = "grid_imgs"
leg_file = "legend.png"

# Define label mappings for the sliders
demand_options = ["Base", "High"]
fuel_options = ["Base", "Constrained"]
delay_options = ["No Delay", "12 Month Delay"]

key_demand = {"Base": "D3", "High": "D5"}
key_fuel = {"Base": "125TJ", "Constrained": "75TJ"}
key_delay = {"No Delay": "ND", "12 Month Delay": "12D"}

# Create a four-column layout with wider ratios
col1, col2, col3, col4 = st.columns([2, 4, 2, 2])  # Adjusted ratios for better space usage

with col1:  # Left column for description image
    image = Image.open('grid_imgs/text_description.png')
    st.image(image)

with col3:  # Right column for sliders
    index1 = st.select_slider(
        "2025 Demand", 
        options=demand_options, 
        value="High",
        key="demand_slider"
    )
    index2 = st.select_slider(
        "OCGT Fuel Consumption", 
        options=fuel_options, 
        value="Constrained",
        key="fuel_slider"
    )
    index3 = st.select_slider(
        "New-build Delay", 
        options=delay_options, 
        value="12 Month Delay",
        key="delay_slider"
    )

with col4:  # Right column for legend
    leg_path = os.path.join(image_folder, leg_file)
    st.image(leg_path)

# Construct the image filename
image_file = os.path.join(image_folder, f"{key_demand[index1]} {key_fuel[index2]} {key_delay[index3]}.png")

with col2:  # Middle column for the main image
    if os.path.exists(image_file):
        image = Image.open(image_file)
        image_placeholder = st.empty()

        im20 = Image.open('grid_imgs/20percent.png')
        im40 = Image.open('grid_imgs/40percent.png')
        im80 = Image.open('grid_imgs/80percent.png')

        # Update the caption in the same image placeholder
        image_placeholder.image(im20, caption="Contacting Plexos server...")
        time.sleep(0.5)
        image_placeholder.image(im40, caption="Simulating...")
        time.sleep(1)
        image_placeholder.image(im80, caption="Rendering...")
        time.sleep(0.3)
        image_placeholder.image(image, caption="Done!")
    else:
        st.error("Image file not found. Make sure the images exist in the script directory.")