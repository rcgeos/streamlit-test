import streamlit as st
import leafmap.foliumap as leafmap 
#import pyrcgeos.foliumap as pyrcgeos
#m = pyrcgeos.Map()

st.set_page_config(layout="wide")

col1, col2  = st.columns([4,1]) #80% col1 and 20% col2
with col2: 
    dropdown = st.selectbox("Basemap",["HYBRID","ROADMAP","TERRAIN","SATELLITE"])

m = leafmap.Map()
m.add_basemap(dropdown)
    # m.add_basemap('HYBRID')
    

with col1: 
   m.to_streamlit() # this should be the last line 
