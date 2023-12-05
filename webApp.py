import streamlit as st
# from streamlit_extras.app_logo import add_logo

import pandas as pd

from classe_cadastro import Cadastro

import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly_dark"

# add kitten logo
# add_logo("https://placekitten.com/100/100")

# add sidebar buttons
st.sidebar.button("plotly_dark")
st.sidebar.button("Button 2")

# add sidebar filters
st.sidebar.slider("Slider", 0, 100, 50)
st.sidebar.date_input("Date Input")


with st.sidebar:
    st.image("https://www.pixenli.com/image/fm0aEpMI", width=150)


uploaded_file = st.file_uploader("Upload your file here...", type=['csv'])

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file, encoding='latin-1', sep=';')
    st.write(dataframe)
    print(dataframe)
    cadastro = Cadastro(dataframe, 11+(29/60), False)
    cadastro.dataframe

    cadastro.printInfo()

    # cadastro.plotQuantitativo()
