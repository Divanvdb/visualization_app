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

    /* Hide the slider value label (red text) */
    .stSelectSlider .stSliderValue {
        display: none !important;
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Display title
st.markdown('<div class="title-text">Likelihood of South African Load Shedding</div>', unsafe_allow_html=True)

# Add vertical spacing
st.write("")
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
col1, col2, col3 = st.columns([2, 2, 2])  # Adjusted ratios for better space usage

with col1:  # Left column for description image
    image = Image.open('grid_imgs/text_description.png')
    st.image(image)
    
    st.write("")
    st.write("")

    index1 = st.select_slider(
        "Electricity demand growth (None / High)", 
        options=demand_options, 
        value="Base",
        key="demand_slider",
        
    )
    index2 = st.select_slider(
        "OCGT daily diesel consumption (100% of 2024 / 60% of 2024)", 
        options=fuel_options, 
        value="Constrained",
        key="fuel_slider"
    )
    index3 = st.select_slider(
        "New-build delay (No delay / 12 month delay)", 
        options=delay_options, 
        value="12 Month Delay",
        key="delay_slider"
    )

with col3:  # Right column for legend
    leg_path = os.path.join(image_folder, leg_file)
    st.image(leg_path)

# Construct the image filename
image_file = os.path.join(image_folder, f"{key_demand[index1]} {key_fuel[index2]} {key_delay[index3]}.png")

with col2:  # Middle column for the main image
    if os.path.exists(image_file):
        save_path = os.path.join(image_folder, "path.txt")
        # Open prev_image
        with open(save_path, "r") as f:
            prev_image_path = f.read()

        # Replace \ with / for Windows paths

        prev_image_path = prev_image_path.replace("\\", "/")

        print(prev_image_path)
        print(image_file)
        prev_image = Image.open(prev_image_path)
        image = Image.open(image_file)

        image_placeholder = st.empty()

        # Update the caption in the same image placeholder
        image_placeholder.image(prev_image, caption="Contacting Plexos server...")
        time.sleep(1)
        image_placeholder.image(prev_image, caption="Simulating...")
        time.sleep(1)
        image_placeholder.image(prev_image, caption="Rendering...")
        time.sleep(0.3)
        image_placeholder.image(image, caption="")

        # Overwrite image path to file
        
        with open(save_path, "w") as f:
            f.write(image_file)
            
    else:
        st.error("Image file not found. Make sure the images exist in the script directory.")