import streamlit as st
import os
from PIL import Image

# Title of the app
st.title("Image Viewer with Slider")

# Define the image path
image_folder = "images"

# Create a two-column layout
col1, col2 = st.columns([10, 5])  # Adjust width ratio (image column is twice as wide)

with col2:  # Right column for sliders
    index1 = st.slider("Select x", 0, 3, 1) 
    index2 = st.slider("Select y", 0, 3, 1)
    index3 = st.slider("Select z", 0, 3, 1)

# Construct the image filename
image_file = os.path.join(image_folder, f"{index1}{index2}{index3}.png")

with col1:  # Left column for the image
    if os.path.exists(image_file):
        image = Image.open(image_file)
        st.image(image, caption=f"Displaying {image_file}")
    else:
        st.error("Image file not found. Make sure the images exist in the script directory.")
