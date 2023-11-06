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




original_title = '<b><em class = "word break"><p style="font-family:Roboto, cursive; color:Black; font-size: 65px;">Happy Birthday!!! :tada:</p></em><b>'
original_title2 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 30px;">Okie so its pretty simple: I give you this software for you to type all the awnsers you collect over the day in here, and then you get special suprise :)</p></em><b>'
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(original_title2, unsafe_allow_html=True)
original_title100 = '<b><em class = "word break"><p style="font-family:Times New Roman, cursive; color:Black; font-size: 20px;">Make sure to do it with the numbers you get from peeps! (Awnser with normal captialization rules). When you get it rightt a letter will appear. Connect it and build the phrase and type it on the next and final page :)  i love you so much nidhi :) and i hope you have fun :)</p></em><b>'
st.markdown(original_title100, unsafe_allow_html=True)
st.markdown("""

    """)

box1 = st.text_input("1: Normal Captilization rules (two words) ")

if box1 == ('Girl Scout'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correct :) This one is from Aadya, and the letter is "W" </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again lolo :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box2 = st.text_input(" 2: Lowercase ")
if box2 == ('e'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Correctsss! From Anuva, Your letter is well, "e"! </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:BAriel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again lolo :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box3 = st.text_input(" 3: Lowercase")
if box3 == ('cooper'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">hehe he is indeed :) that was all Anvi,  and your letter is "L" </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again loly :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box4 = st.text_input("4: Lowercase")
if box4 == ('diya'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Correctt that is from Diya, your letter is "o"</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try againnnn :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box5 = st.text_input("5: lowercase (2 words) ")
if box5 == ('your breath'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">> Yup you are rightt that is from your Hasini lolo, your letter is "V"</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again oop :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box6 = st.text_input("6: First letter captial ")
if box6 == ('Christmas'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Very correcto :) That one is Pramiti, and your number actually is "3" </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box7 = st.text_input("7: Lowercase (two words) ")
if box7 == ('carrot eraser'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Noice you got ittt :) From my homey Sammith, your letter is "Y" </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box8 = st.text_input("8: Lowercase")
if box8 == ('sand'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Yess there you goo, that is from Shirya, and your letter is "o" </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Tryyyy againss  :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box9 = st.text_input("9: Lowercase")
if box9 == ('trisha'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">Correcct ineeed, from Trisha, and your letter is a big "U" </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again again :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box10 = st.text_input("10: Capital first letter, lowercase rest")
if box10 == ('Unsanskari'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Oh yes actually wild, this one is from Tej ofc, and your letter is "n"</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try againnnn :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)

box11 = st.text_input("11: Lowercase")
if box11 == ('frog'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Yepp you got it, this one is from Ananya, and your letter is "i" </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again yaaa :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box12 = st.text_input("12: Lowercase")

if box12 == ('fire'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Righttt, form Rishima, your letter is "d" </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again lolz :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box13 = st.text_input("13: Lowercase")

if box13 == ('chinmaya'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> You are corrrecttt, this one is from Smithi, and your letter is "h" </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box14 = st.text_input("14: Lowercase")

if box14 == ('dora'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Yup loly correcttt, this is from Sruthi, and your letter is another "i" </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box15 = st.text_input("15: Lowercase")

if box15 == ('me'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> Correcctt: This is from ____ and your symbol is a simple space " " </span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box16 = st.text_input("16: Lowercase")

if box16 == ('me'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">  Rightyyy, Your symbol is  ":" :)</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)
box17 = st.text_input("17: first letter captial, lowercase")

if box17 == ('Cancun :)'):
    original_title4 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E"> And finally ofc :) This one hehe perfect from me :) Your final symbol is ")"</span></p></em><b>'
    st.markdown(original_title4, unsafe_allow_html=True)
else:
    original_title5 = '<b><em class = "word break"><p style="font-family:Ariel, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
    st.markdown(original_title5, unsafe_allow_html=True)




if box1 == 'PANEER' and box2 == 'PISCES' and box3 == 'ROBOTICS' and box4 == 'CANCUN,PORTUGAL,LONDON,TURKEY' and box5 == '03/19/2022' and box6 == '03/05/2022' and box7 == 'DHIR,ASHAR,MURTAZA' and box8 == '03/27/2022' and box9 == 'CUTE,HOT,SEXY' and box10 == 'THEM ALL':
    original_title12 = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size: 40px;"> BABY U DID IT :))))))</p></em><b>'
    st.markdown(original_title12, unsafe_allow_html=True)
    original_title13 = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size: 30px;">yayayyay u finisheeeeeeeed :)) now u getty lovey letter :)))</p></em><b>'
    st.markdown(original_title13, unsafe_allow_html=True)
    box11 = st.text_input("Final: Hehe whattt doesss it spelllll?")
    if box11 == ('MOON PALACE'):
        original_title4 = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Black; font-size: 18px;"><span style="background-color:#2EFE2E">heheh :) i love you baby :)</span></p></em><b>'
        st.markdown(original_title4, unsafe_allow_html=True)
        st.subheader("[We aer for life :heart:]"
                         "(https://docs.google.com/document/d/1iZCTgmPf1CPh7ywMklvJxHaEGrvf0ZvXuzb6A1fuotg/edit?usp=sharing)")
    else:
        original_title5 = '<b><em class = "word break"><p style="font-family:Brush Script MT, cursive; color:Red; font-size: 18px;"><span style="background-color:#000000">Try again hehe :))</span></p></em><b>'
        st.markdown(original_title5, unsafe_allow_html=True)



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
