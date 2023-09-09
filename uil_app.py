import streamlit as st
import numpy as np
import pandas as pd
from streamlit_gallery import apps, components

tab1, tab2 = st.tabs(["Leaderboard", "Code Editor"])

tab1.subheader("A place to see where you stand")
df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))
tab1.table(df)

with tab2:
   tab2.subheader("A place to write code")
   st.components.ace_editor
