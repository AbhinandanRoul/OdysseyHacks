import streamlit as st

st.title("Cattle Monitoring")
col1, col2 = st.columns(2)

with col1:
    st.container()
    with st.container():
        st.header("Cow 1")
        st.image("data/soil_profiles/cow1.jpeg")
        st.subheader("Health")
        st.write("✅Healthy")
        st.subheader("Location")
        st.write("📍47.5°N, -122.3°W")
        st.subheader("Feeding time")
        st.write("🕒in 2 hours")
        st.subheader("Insimination time")
        st.write("🕒in 27 days")
    
    st.container()
    with st.container():
        st.header("Cow 2")
        st.image("data/soil_profiles/cow2.png")
        st.subheader("Health")
        st.write("❌Need Attention")
        st.subheader("Location")
        st.write("📍48.5°N, -122.3°W")
        st.subheader("Feeding time")
        st.write("🕒in 1 hours")
        st.subheader("Insimination time")
        st.write("🕒in 3 days")

with col2:
    st.container()
    with st.container():
        st.header("Cow 3")
        st.image("data/soil_profiles/cow3.jpeg")
        st.subheader("Health")
        st.write("✅Healthy")
        st.subheader("Location")
        st.write("📍47.5°N, -123.3°W")
        st.subheader("Feeding time")
        st.write("Now!!")
        st.subheader("Insimination time")
        st.write("🕒in 10 days")
    
    st.container()
    with st.container():
        st.header("Cow 4")
        st.image("data/soil_profiles/cow4.jpeg")
        st.subheader("Health")
        st.write("✅Healthy")
        st.subheader("Location")
        st.write("📍48.5°N, -126.3°W")
        st.subheader("Feeding time")
        st.write("🕒1 hour late")
        st.subheader("Insimination time")
        st.write("🕒in 1 day")
