import streamlit as st
import leafmap.foliumap as leafmap 
import pyrcgeos.foliumap as pyrcgeos

#m = pyrcgeos.Map()
m = leafmap.Map()
m.to_streamlit()
