import streamlit as st

from streamlit_gallery import apps, components
from streamlit_gallery.utils.page import page_group

def main():
    st.components.vi.iframe("https://gist.github.com/ipeychev/7081314.js",height=600)

if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Based Code Editor Site", layout="wide")
    main()
