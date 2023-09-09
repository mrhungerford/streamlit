import streamlit as st
import numpy as np
import pandas as pd
from streamlit_gallery import apps, components
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

def main():
   tab1, tab2 = st.tabs(["Leaderboard", "Code Editor"])
   tab1.subheader("A place to see where you stand")
   df = pd.DataFrame(
      np.random.randn(10, 5),
      columns=('col %d' % i for i in range(5)))
   tab1.table(df)
   
   with tab2:
      tab2.subheader("A place to write code")
      c1, c2 = st.columns([3, 1])
   
      c2.subheader("Parameters")
   
      with c1:
         with st.container:
           content = st_ace(
              placeholder="Write your code here",
              language="java",
              theme=c2.selectbox("Theme", options=THEMES, index=35),
              keybinding="vscode",
              font_size=c2.slider("Font size", 5, 24, 14),
              tab_size=4,
              show_gutter=True,
              #show_print_margin=c2.checkbox("Show print margin", value=False),
              wrap=c2.checkbox("Wrap enabled", value=False),
              #auto_update=c2.checkbox("Auto update", value=False),
              #readonly=c2.checkbox("Read-only", value=False),
              min_lines=20,
              max_lines=20,
              key="ace",
         )
         with c2:
            st.subheader("Content")
            st.text(content)
def _max_height_(prcnt_height: int = 75):
   max_height_str = f"max-height: {prcnt_height}vh;"
   st.markdown(f""" 
                <style> 
                .reportview-container .main .block-container{{{max_height_str}}}
                </style>    
                """, 
                unsafe_allow_html=True,
   )
   padding = 0
   css = """ <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        [data-testid="ScrollToBottomContainer"] {
        overflow: hidden;}
    }} </style> """
   st.markdown(css, unsafe_allow_html=True)
if __name__ == "__main__":
   st.set_page_config(page_title="UIL Code Editor", layout="wide")
   # Call the _max_height_ function with the desired percentage height
   _max_height_(60)  # Set maximum height to 75%
   hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
   st.markdown(hide_default_format, unsafe_allow_html=True)
   main()
