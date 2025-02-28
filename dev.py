import streamlit as st
import os
from PIL import Image

# Custom CSS to prevent text wrapping
st.markdown(
    """
    <style>
        .title-text {
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
            font-size: 32px;
            font-weight: bold;
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True
)

# Display title without wrapping
st.markdown('<div class="title-text">Scenario-based Load Shedding Risk</div>', unsafe_allow_html=True)

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

# Create a two-column layout
col1, col2 = st.columns([15, 6])  # Adjust width ratio (image column is twice as wide)

with col2:  # Right column for sliders
    index1 = st.select_slider(
        "2025 Demand", 
        options=demand_options, 
        value="High"
    )
    index2 = st.select_slider(
        "OCGT Fuel Consumption", 
        options=fuel_options, 
        value="Constrained"
    )
    index3 = st.select_slider(
        "New-build Delay", 
        options=delay_options, 
        value="12 Month Delay"
    )

    # Add in space
    st.write("")

    leg_path = os.path.join(image_folder, leg_file)
    st.image(leg_path, caption="Legend")

# Construct the image filename
image_file = os.path.join(image_folder, f"{key_demand[index1]} {key_fuel[index2]} {key_delay[index3]}.png")

with col1:  # Left column for the image
    if os.path.exists(image_file):
        image = Image.open(image_file)
        st.image(image, caption=f"Displaying {image_file}")
    else:
        st.error("Image file not found. Make sure the images exist in the script directory.")

