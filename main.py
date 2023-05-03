import streamlit as st
import plotly.express as px
from get_scores import get_scores

pos_data, neg_data, dates = get_scores()

st.title("Diary Tone")

st.subheader("Positivity")
pos_figure = px.line(x=dates, y=pos_data,
                     labels={"x": "Dates", "y": "Positivity"})
st.plotly_chart(pos_figure)

st.subheader("Negativity")
pos_figure = px.line(x=dates, y=neg_data,
                     labels={"x": "Dates", "y": "Negativity"})
st.plotly_chart(pos_figure)
