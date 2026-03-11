import os
import streamlit as st
import pandas as pd
import plotly.express as px

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(BASE_DIR, "data", "flights.csv")

df = pd.read_csv(data_path)

st.title("✈ Airline Flight Data Analysis Dashboard")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Flight Delay by Airline")

delay = df.groupby("AIRLINE")["ARRIVAL_DELAY"].mean().reset_index()

fig = px.bar(delay,x="AIRLINE",y="ARRIVAL_DELAY")

st.plotly_chart(fig)

st.subheader("Monthly Delay Trend")

month = df.groupby("MONTH")["ARRIVAL_DELAY"].mean().reset_index()

fig2 = px.line(month,x="MONTH",y="ARRIVAL_DELAY")

st.plotly_chart(fig2)

st.subheader("Top 10 Busiest Airports")

airport = df["ORIGIN_AIRPORT"].value_counts().head(10).reset_index()

airport.columns=["Airport","Flights"]

fig3 = px.bar(airport,x="Airport",y="Flights")

st.plotly_chart(fig3)