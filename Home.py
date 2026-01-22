import streamlit as st

st.set_page_config( page_title="CottonExpelOilYieldPred", initial_sidebar_state="expanded", layout="wide")
col1, col2 = st.columns([1.5, 20])

with col1:
    st.image("static/images/icarlogo.png", width=150)

with col2:
    st.markdown("<h1 style='text-align:center;'> CottonExpelOilYieldPred: A Machine Learning-Based Web Resource for Estimation of Cottonseed Oil Yield</h1>", unsafe_allow_html=True)


st.markdown("---")
st.text("")

st.header("Welcome to CottonExpelOilYieldPred")
st.markdown("""
**CottonExpelOilYieldPred** focuses on developing an easy-to-use portal that helps estimate cottonseed oil yield based on key factors like the moisture content of the cottonseed, the type of expeller used, the screw speed and cake thickness. 

By entering these details into the system, users can quickly get an idea of how much oil can be produced. 

The portal is designed to support researchers, and oil mill operators in making better decisions and improving the efficiency of the oil extraction process.

CottonExpelOilYieldPred is freely accessible to the academic community at: **https://cottonseed-dss.streamlit.app/**
""")

st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2026 ICAR-Central Institute for Research on Cotton Technology, Mumbai-400019. All rights reserved.</p></div>", unsafe_allow_html=True)
