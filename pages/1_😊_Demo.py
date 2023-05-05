import streamlit as st
import leafmap.foliumap as leafmap 
#import pyrcgeos.foliumap as pyrcgeos

#m = pyrcgeos.Map()

st.set_page_config(layout="wide")
m = leafmap.Map()
m.add_basemap('HYBRID')
m.to_streamlit()
