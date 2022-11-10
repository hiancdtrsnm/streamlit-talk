import streamlit as st
import pandas as pd
import altair as alt

@st.cache
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

df = get_UN_data()
countries = st.multiselect(
    "Selecciona los países:", list(df.index), ["China", "United States of America", "Spain"]
)
if not countries:
    st.error("Debes seleccionar al menos un país.")
else:
    data = df.loc[countries]
    data /= 1000000.0
    st.write("### Producción Agrícola ($B)", data.sort_index())

    data = data.T.reset_index()
    data = pd.melt(data, id_vars=["index"]).rename(
        columns={"index": "year", "value": "Producción Agrícola ($B)"}
    )
    chart = (
        alt.Chart(data)
        .mark_area(opacity=0.3)
        .encode(
            x="year:T",
            y=alt.Y("Producción Agrícola ($B):Q", stack=None),
            color="Region:N",
        )
    )
    st.altair_chart(chart, use_container_width=True)

if st.checkbox("Mostrar código"):
    st.code(
        """
import streamlit as st
import pandas as pd
import altair as alt

@st.cache
def get_UN_data():
    AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
    df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
    return df.set_index("Region")

df = get_UN_data()
countries = st.multiselect(
    "Selecciona los países:", list(df.index), ["China", "United States of America", "Spain"]
)
if not countries:
    st.error("Debes seleccionar al menos un país.")
else:
    data = df.loc[countries]
    data /= 1000000.0
    st.write("### Producción Agrícola ($B)", data.sort_index())

    data = data.T.reset_index()
    data = pd.melt(data, id_vars=["index"]).rename(
        columns={"index": "year", "value": "Producción Agrícola ($B)"}
    )
    chart = (
        alt.Chart(data)
        .mark_area(opacity=0.3)
        .encode(
            x="year:T",
            y=alt.Y("Producción Agrícola ($B):Q", stack=None),
            color="Region:N",
        )
    )
    st.altair_chart(chart, use_container_width=True)
"""
    )