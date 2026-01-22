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
        #colInCon_1, colInCon_2 = st.columns([1, 3])
        #with colInCon_1:
        #    pass
            #st.image("static/images/Sneha_murmu.png")
        #with colInCon_2:
        st.markdown('''<h4 style='text-align:center;'>Director</h4></br>  
                    <p style='text-align:center;'>ICAR-Central Institute for Research on Cotton Technology,</br>  
                    Mumbai, Maharashtra-400019, India.</br>  
                    Contact mail: director-circot@icar.org.in</p>''', unsafe_allow_html=True)

with col2_1:
     with st.container(border=True):
        #colInCon_1, colInCon_2 = st.columns([1, 3])
        #with colInCon_1:
        #    pass
            #st.image("static/images/himanshu_pic.jpeg")
        #with colInCon_2:
        st.markdown('''<h4 style='text-align:center;'>Head</h4>  
                    <p style='text-align:center;'>Chemical and Biochemical Processing Division</br>  
                    ICAR - Central Institute for Research on Cotton Technology,</br>  
                    Mumbai, Maharashtra-400019, India.</br>  
                    Contact mail: nvw75@yahoo.com</p>''', unsafe_allow_html=True)



st.text("")
st.markdown("<div style='background-color:#32CD32; text-align:center'><p style='color:white'>Copyright © 2026 ICAR-Central Institute for Research on Cotton Technology, Mumbai-400019. All rights reserved.</p></div>", unsafe_allow_html=True)