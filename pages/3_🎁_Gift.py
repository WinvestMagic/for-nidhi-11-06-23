import streamlit as st

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.shutterstock.com/image-photo/purple-heartshaped-bokeh-background-260nw-372605212.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()




original_title = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 65px;">You finisheddd!!! 🎁</p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 30px;">Okie so now just put eveything in one nice long phrase :)</p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Times New Roman, cursive; color:Black; font-size: 20px;">It spells our message to you :)</p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
st.markdown("""

    """)

box1 = st.text_input("Enter your answer")

if box1 == ('WeLoV3YoUnidhi :)'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">And Yes hehe you are right :) </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again lolo :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

if box1 == 'WeLoV3YoUnidhi :)':
    original_title12 = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size: 40px;"> U DID IT :)</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size: 30px;">Hehe now here is a spedcial smth from us all :) </p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)

    original_title13 = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size: 30px;">Hehe now here is a spedcial smth from us all :) </p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)



#----------------------Hide Streamlit footer----------------------------
hide_menu = """
<style>
footer{
        visibility:hidden;
    }
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)
#--------------------------------------------------------------------