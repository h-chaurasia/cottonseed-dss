import streamlit as st
import numpy as np
import joblib
import pandas as pd


st.set_page_config( page_title="CottonExpelOilYieldPred", initial_sidebar_state="expanded", layout="wide")
col1, col2 = st.columns([1.5, 20])

with col1:
    st.image("static/images/icarlogo.png", width=150)

with col2:
    st.markdown("<h1 style='text-align:center;'> CottonExpelOilYieldPred: A Machine Learning-Based Web Resource for Estimation of Cottonseed Oil Yield</h1>", unsafe_allow_html=True)


st.markdown("---")
st.text("")

st.header("Predict Cottonseed Oil Yield")

@st.cache_resource
def load_models():
    models = {
        "Cake Yield (%)": joblib.load("static/models/cake_yield_model.pkl"),
        "Oil Yield (%)": joblib.load("static/models/oil_yield_model.pkl"),
        #"Protein in Cottonseed (%)": joblib.load("static/models/protein_cottonseed_model.pkl"),
        "Protein in Cake (%)": joblib.load("static/models/protein_cake_model.pkl"),
    }
    return models

models = load_models()

# -----------------------------
# INPUT SECTION
# -----------------------------
st.subheader("🔢 Input Following Values")

# 1–3: numeric inputs
x1 = st.number_input(
    "CottonSeed Moisture (%wb)",
    min_value=6,
    step=1,
    #value=0,
    max_value=16
)

x2 = st.number_input(
    "Screw Speed (RPM)",
    min_value=12,
    step=1,
    #value=0,
    max_value=20
)

x3 = st.number_input(
    "Avg Cake Thickness (mm)",
    min_value=12,
    step=1,
    #value=0,
    max_value=20
)


# 4: Seed quality (radio)
seed_quality = st.radio(
    "Seed Quality",
    options=["Very good", "Good"],
    horizontal=True
)
x4 = 1 if seed_quality == "Very good" else 0

# 5: Number of bolts (radio)
bolts = st.radio(
    "No. of Bolts",
    options=["12", "9"],
    horizontal=True
)
x5 = 1 if bolts == "12" else 0

# 6: Moisture type (radio)
moisture_type = st.radio(
    "Moisture type",
    options=["Natural", "Added"],
    horizontal=True
)
x6 = 1 if moisture_type == "Natural" else 0

# Final input array (ORDER MUST MATCH TRAINING)
X_input = np.array([[x1, x2, x3, x4, x5, x6]])

# -----------------------------
# PREDICTION
# -----------------------------
prediction_std = {
    "Cake Yield (%)": 0.80,
    "Oil Yield (%)": 0.37,
    #"Protein in Cottonseed (%db)": 0.29,
    "Protein in Cake (%)": 0.72
}


if st.button("🔮 Predict All Parameters"):
    st.subheader("📊 Predicted Outputs")
    predictions = {}

    for target, model in models.items():
        predictions[target] = model.predict(X_input)[0]

    results_df = pd.DataFrame(
        predictions.items(),
        columns=["Output Parameter", "Predicted Value"]
    )

    st.success("Prediction successful!")
    #st.table(results_df)

    for k, v in predictions.items():
        sd = prediction_std.get(k, 0.0)
        st.metric(label=k, value=f"{v:.2f} ± {sd:.2f}")




st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2026 ICAR-Central Institute for Research on Cotton Technology, Mumbai-400019. All rights reserved.</p></div>", unsafe_allow_html=True)
