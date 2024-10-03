import streamlit as st
import folium
from streamlit_folium import folium_static

# Buat peta dasar
m = folium.Map(location=[-37.8136, 144.9631], zoom_start=13)

# Tambahkan marker
folium.Marker([-37.8136, 144.9631], popup="Melbourne").add_to(m)

# Tampilkan peta di Streamlit
folium_static(m)
