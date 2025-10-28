import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="CityScope — Denver MVP", layout="wide")

st.title("CityScope Predict — Denver MVP")
st.caption("Synthetic demo: incident risk heatmap & tiles (career-first portfolio)")

st.sidebar.header("Filters")
horizon = st.sidebar.slider("Forecast Horizon (minutes)", 15, 120, 60, step=15)
seed = st.sidebar.number_input("Random Seed", value=42, step=1)

st.write("### Risk Snapshot")
st.info("This MVP displays synthetic tile risks. Replace with model predictions later.")

# Fake tile centroids (rough bounding box around Denver)
rng = np.random.default_rng(int(seed))
n = 400
lats = rng.uniform(39.55, 39.88, n)
lons = rng.uniform(-105.15, -104.60, n)
risk = rng.beta(2,5, n)  # 0..1

df = pd.DataFrame({"lat": lats, "lon": lons, "risk": risk})
st.map(df.rename(columns={'lat':'latitude','lon':'longitude'}))

st.write("Top 10 highest risk tiles")
st.dataframe(df.sort_values('risk', ascending=False).head(10))
