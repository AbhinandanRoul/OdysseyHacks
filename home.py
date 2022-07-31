import streamlit as st
import numpy as np
import pandas as pd
st.header("Farm.ai")
st.subheader("One stop solution for your farms")
st.image("logo.jpg")
# add_selectbox =st.sidebar.selectbox(
#     "NAVIGATION",  # Title of sidebar
#     (
#         "Farm Cattle", "Cattle Health", "Blah Blah", ))

# with st.sidebar:
#     btn1=st.button("Farm Cattle")
#     btn2=st.button("Cattle Health")
#     btn3=st.button("Soil Health")

col1, col2= st.columns(2)

with col1:
    st.header("Col 1")
    # st.image("https://static.streamlit.io/examples/cat.jpg")
    st.container()
    with st.container():
        st.write("This is inside the container 1.1,put anything here")
        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(10, 3))

    st.container()
    with st.container():
        st.write("This is inside the container 1.2,put anything here")
        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(10, 3))


with col2:
    st.header("Col 2")
    st.container()
    with st.container():
        st.write("This is inside the container 2.1,put anything here")
        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(20, 3))

    st.container()
    with st.container():
        st.write("This is inside the container 2.2,put anything here")
        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(20, 3))

# No columns are used here, render directly
st.container()
with st.container():
    st.write("This is inside the container 2.2,put anything here")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(20, 3))
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])



st.container()
with st.container():
    st.write("This is inside the container 2.2,put anything here")
    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(20, 3))
