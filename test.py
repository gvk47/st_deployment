import streamlit as st
import pandas as pd
st.markdown("""
            <style>
            .css-erpbzb.e1ewe7hr3
            {
                visibility: hidden;
            }
            .css-cio0dv.e1g8pov61
            {
                visibility: hidden;
            }
            </style>
            """,unsafe_allow_html=True)
table = pd.DataFrame({"column1":[1,2,3],"column2":[4,5,6]})
st.title(" Hi this is streamlit web app ")
st.header("Header")
st.subheader("SubHeader")
st.text("its my pleasure to use streamlit instead of html and css ")
st.markdown(" hello world! ")
st.markdown("[google](https://www.google.com)")
hello_world_code = """
print("Hello world!")
"""
st.code(hello_world_code)
st.metric(label = "ball speed",value = "120ms⁻¹",delta="-1.4ms⁻¹")
st.write(""" ## hello world!
         > Hi
         **Bold**
         *Italic*
         """)
st.table(table)
st.dataframe(table)
# st.image("image.jpg", caption="this is my image",width=400)

