import streamlit as st
import pandas as pd
import numpy as np

# [pd]
# ignore_missing_imports = True

st.text("hello, world")
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [5, 6, 7, 8]})

df
st.write(df)
st.table(df)
st.dataframe(df)

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))
