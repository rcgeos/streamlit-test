import streamlit as st
import leafmap.foliumap as leafmap 
#import pyrcgeos.foliumap as pyrcgeos

#m = pyrcgeos.Map()

st.set_page_config(layout="wide")
dropdown = st.selectbox("Basemap",["HYBRID","ROADMAP","TERRAIN","SATELLITE"])

m = leafmap.Map()
m.add_basemap(dropdown)
# m.add_basemap('HYBRID')
# m.to_streamlit()


