import streamlit as st
from proj import finalfunc
from exp import explore
ide_ra,hush,res=0,0,0
st.set_page_config(layout="wide")
st.title("Products Comparison")
i=st.text_input(label='SEARCH HERE...')
if i:
    
    st.write(i+"Product searching")
    ide_ra,hush,res=finalfunc(i)
else:
    if ide_ra!=0:
        st.write(ide_ra[0][0])
    else:
        st.write("no input")
explore(ide_ra,hush)

