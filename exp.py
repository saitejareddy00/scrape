import streamlit as st
import pandas as pd
import numpy as np
def explore(ide_ra,hush):
    if ide_ra and hush:
        col1, col2 = st.columns(2)

        with col1:
            
            for i in range(5):
                st.header(ide_ra[i][0])
                st.write("AMAZON")
                st.markdown("<style>.big-font {color:red;font-size:25px;}.d{font-size:20px;}</style>", unsafe_allow_html=True)
                st.markdown("<p class=\"big-font\">Price: "+ide_ra[i][1]+"</p>", unsafe_allow_html=True)
                st.markdown("<p class=\"d\">Price: "+ide_ra[i][2]+"</p>", unsafe_allow_html=True)
                st.markdown("<p class=\"d\">Review Count: "+ide_ra[i][3]+"</p>", unsafe_allow_html=True)
                st.write("click this [link]("+ide_ra[i][4]+")")
                                

        with col2:
            #st.subheader("FLIPKART")
        
            for i in range(5):
                if True:
                    st.header(ide_ra[i][0])
                    st.write("FLIPKART")
                    st.markdown("<style>.big-font {color:red;font-size:25px;}.d{font-size:20px}</style>", unsafe_allow_html=True)
                    st.markdown("<p class=\"big-font\">Price: "+hush[i][0]+"</p>", unsafe_allow_html=True)
                    st.markdown("<p class=\"d\">Price: "+hush[i][1]+"</p>", unsafe_allow_html=True)
                    st.markdown("<p class=\"d\">Review Count: "+hush[i][2]+"</p>", unsafe_allow_html=True)
                    st.write("click this [link]("+hush[i][3]+")")
    else:
        st.write("no input")
        
