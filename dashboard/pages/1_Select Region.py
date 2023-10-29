import ee
import folium
import geemap.colormaps as cm
import geemap.foliumap as geemap
from datetime import date
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

ee.Initialize()

# Define a function to display a map
def getMap():
    Map = geemap.Map(
    basemap="HYBRID",
    plugin_Draw=True,
    Draw_export=True,
    locate_control=True,
    plugin_LatLngPopup=False,
    )
    return Map

display_map = getMap()

# Define a function to select a region of interest
def select_roi():
    # Prompt the user to draw a shape on the map
    st.warning("Please draw a shape on the map to select your region of interest.")
    # Wait for the user to draw a shape
    shape = ee.Geometry.Polygon(st.draw_features())
    # Return the selected shape
    return shape

# Call the select_roi function to select a region of interest
roi = select_roi()

# Print the selected region of interest
st.write("Selected region of interest:", roi)
