import streamlit as st

from streamlit_gallery import apps, components
#from streamlit_gallery.utils.page import page_group

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")

with tab2:
   st.header("A dog")

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
