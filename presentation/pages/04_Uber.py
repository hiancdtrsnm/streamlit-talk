import streamlit as st
import pandas as pd
import pydeck as pdk

"# Uber Pickups in New York City"


@st.experimental_singleton
def load_data():
    data = pd.read_csv(
        "./uber-raw-data-sep14.csv.gz",
        nrows=100000,  # approx. 10% of data
        names=[
            "date/time",
            "lat",
            "lon",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=[
            "date/time"
        ],  # set as datetime instead of converting after the fact
    )

    return data


df_original = load_data()

col1, col2 = st.columns(2)
with col1:
    hour_selected = st.slider(
        "Hora de Recogida",
        0,
        23,
        key="pickup_hour",
    )


with col2:
    st.write(
        "#### Selecciona la hora y observa como se distribuyen los viajes de Uber en Nueva York."
    )

df = df_original[df_original["date/time"].dt.hour == hour_selected]

jfk = [40.6650, -73.7821]

col1, col2 = st.columns([.6, .4])

with col1:
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": jfk[0],
                "longitude": jfk[1],
                "zoom": 12,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=df,
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )

with col2:
    df

if st.checkbox("Mostrar código"):
    st.code("""
import streamlit as st
import pandas as pd
import pydeck as pdk

"# Uber Pickups in New York City"


@st.experimental_singleton
def load_data():
    data = pd.read_csv(
        "./uber-raw-data-sep14.csv.gz",
        nrows=100000,  # approx. 10% of data
        names=[
            "date/time",
            "lat",
            "lon",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=[
            "date/time"
        ],  # set as datetime instead of converting after the fact
    )

    return data


df_original = load_data()

col1, col2 = st.columns(2)
with col1:
    hour_selected = st.slider(
        "Hora de Recogida",
        0,
        23,
        key="pickup_hour",
    )


with col2:
    st.write(
        "## Selecciona la hora y observa como se distribuyen los viajes de Uber en Nueva York."
    )

df = df_original[df_original["date/time"].dt.hour == hour_selected]

jfk = [40.6650, -73.7821]

col1, col2 = st.columns([.6, .4])

with col1:
    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": jfk[0],
                "longitude": jfk[1],
                "zoom": 12,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=df,
                    get_position=["lon", "lat"],
                    radius=100,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    extruded=True,
                ),
            ],
        )
    )

with col2:
    df

""")