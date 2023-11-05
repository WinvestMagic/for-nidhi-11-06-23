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

#navbarrr

original_title = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 80px;">Welcome :)</p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 50px;">Happy Birthday Nidhi 💜</p></em><b>'
original_title4 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 40px;">Back to the softwaress</p></em><b>'
original_title3 = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 35px;"> and this time i brought friendsss :) (they actually urs heh 💖) Enjoy!</p></em><b>'
original_title6 = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size: 30px;"> i love you :)</p></em><b>'

st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
st.markdown(original_title4, unsafe_allow_html=True)
st.markdown(original_title3, unsafe_allow_html=True)
st.markdown(original_title6, unsafe_allow_html=True)

st.markdown("""
    """)


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

