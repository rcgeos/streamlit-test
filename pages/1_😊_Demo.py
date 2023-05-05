import streamlit as st
import leafmap.folium as leafmap 
import pyrcgeos.folium as pyrcgeos

#m = pyrcgeos.Map()
m = leafmap.Map()
m.to_streamlit()
