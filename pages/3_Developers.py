import streamlit as st

st.set_page_config( page_title="CottonExpelOilYieldPred", initial_sidebar_state="expanded", layout="wide")
col1, col2 = st.columns([1.5, 20])

with col1:
    st.image("static/images/icarlogo.png", width=150)

with col2:
    st.markdown("<h1 style='text-align:center;'> CottonExpelOilYieldPred: A Machine Learning-Based Web Resource for Estimation of Cottonseed Oil Yield</h1>", unsafe_allow_html=True)


st.markdown("---")
st.text("")

col1_1, col2_1 = st.columns([1, 1])

with col1_1:
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/jyoti.jpeg")
        with colInCon_2:
            st.markdown('''**Dr. Jyoti Dhakane-Lad**  
                        Scientist (Agricultural Structures & Process Engineering)  
                        Chemical and Biochemical Processing Division  
                        ICAR-Central Institute for Research on Cotton Technology  
                        Mumbai-400019, India.  
                        Contact mail: jyotip.dhakane@gmail.com''')

    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/kirti.jpeg")
        with colInCon_2:
            st.markdown('''**Dr. Kirti Jalgaonkar**  
                        Sr. Scientist (Agricultural Structures & Process Engineering)  
                        Quality Evaluation & Improvemnet Division  
                        ICAR - Central Institute for Research on Cotton Technology,  
                        Mumbai, Maharashtra-400019, India.  
                        Contact mail: jalgaonkar.kirti@gmail.com''')

with col2_1:
    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/himanshu.jpeg")
        with colInCon_2:
            st.markdown('''**Dr. Himanshushekhar Chaurasia**  
                        Scientist (Computer Application & IT)  
                        Mechanical Processing Division  
                        ICAR - Central Institute for Research on Cotton Technology,  
                        Mumbai, Maharashtra-400019, India.  
                        Contact mail: h.chaurasia@icar.org.in''')
            

    with st.container(border=True):
        colInCon_1, colInCon_2 = st.columns([1, 3])
        with colInCon_1:
            st.image("static/images/kanika.jpeg")
        with colInCon_2:
            st.markdown('''**Dr. Kanika Sharma**  
                        Scientist (Plant Biochemistry)  
                        Chemical and Biochemical Processing Division  
                        ICAR - Central Institute for Research on Cotton Technology,  
                        Mumbai, Maharashtra-400019, India.  
                        Contact mail: sharmakanika.bch@gmail.com''')


st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2026 ICAR-Central Institute for Research on Cotton Technology, Mumbai-400019. All rights reserved.</p></div>", unsafe_allow_html=True)