import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import pandas as pd

loc_button = Button(label="Get Soil Profile", align = "center", background= "lightblue")
loc_button.js_on_event("button_click", CustomJS(code="""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
        }
    )
    """))
result = streamlit_bokeh_events(
    loc_button,
    events="GET_LOCATION",
    key="get_location",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    st.title("Soil Profile: Sandy Loam Soils")
    # import image from local directory (not from the web)
    st.image("data/soil_profiles/Sandy_Loam_Soils.jpeg")
    st.caption("Sandy loam soils have visible particles of sand mixed into the soil. When sandy loams soils are compressed, they hold their shape but break apart easily. Sandy loam soils have a high concentration of sand that gives them a gritty feel. In gardens and lawns, sandy loam soils are capable of quickly draining excess water but can not hold significant amounts of water or nutrients for your plants. Plants grown in this type of soil will require more frequent irrigation and fertilization than soils with a higher concentration of clay and sediment. Sandy loam soils are often deficient in specific micronutrients and may require additional fertilization to support healthy plant growth.")
    st.subheader("Crops to grow in this soil")
    st.write(
        "->Sweet corn")
    st.write("->Okra")
    st.write("->Radishes")
    st.write("->Eggplant")
    st.write("->Carrots")
    st.write("->Pole beans")
    st.write("->Greens")
    st.write("->Spinach")
    st.caption("In general, root vegetables, and leafy vegetable plants to do well in sandy loam. Fruits that can grow in loam soil include Strawberries, Blackberries, and Blueberries.")
    st.map((pd.DataFrame(result).T))
