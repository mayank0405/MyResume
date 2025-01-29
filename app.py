import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout="wide")


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coder_url = "https://drive.google.com/uc?id=1Tv5lkJob2RcYpXKFbNZOOeteqzstiDVa"
lottie_contact_url = "https://drive.google.com/uc?id=149pcw-_hRrtHzl6kjtYXKPgPSkHeTU-9"
image1 = Image.open("Technologies.png")


lottie_coder = load_lottie_url(lottie_coder_url)
lottie_contact = load_lottie_url(lottie_contact_url)

st.write("##")
st.subheader("Hey Guys :wave:")
st.title("My Portfolio Website")

st.write('---')

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About', 'Projects', 'Contact'],
        icons = ['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

if selected == 'About':
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Mayank Singh")
            st.title("Pursuing M.S. in Computer Science(ML Track)")
        
        with col2:
            if lottie_coder:
                st_lottie(lottie_coder, width=300, height=300)
        
        st.write("---")

        with st.container():
            col3, col4 = st.columns(2)
            with col3:
                st.subheader("""
                Education
                - Woolf X Scaler
                    - M.S in Computer Science (Data Science and Machine Learning)
                    - Grade: Not yet finished
                - Amity University Noida
                    -Bachelor of Technology - Computer Science
                    -Grade: 7.85/10.0 (First Division)
                """)
        
            with col4:
                st.subheader("Experience")
                st.write("""
                    - IQVIA ~ Apprenticeship
                    - 9 Months
                    - Bengaluru
                """)

if selected == "Projects":
    with st.container():
        width = 400
        height = int(image1.height * (width/image1.width))
        resized_image = image1.resize((width, height))    
        st.header("My Projects")
        st.write("##")
        col5, col6 = st.columns((1,2))
        with col5:
            st.image(resized_image)

        with col6:
            st.markdown("[Visit github Repo](https://github.com/mayank0405)")


if selected == "Contact":
    st.header("Get in touch")

    contact_form = """<form action="https://formsubmit.co/mayank.singh.work00@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <div style="margin-bottom: 10px;">
        <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
    </div>
    <div style="margin-bottom: 10px;">
        <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
    </div>
    <div style="margin-bottom: 10px;">
        <textarea name="message" placeholder="Your message" required style="width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;"></textarea>
    </div>
    <button type="submit" style="padding: 10px 20px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">
        Send
    </button>
    </form>"""

    left_col, right_col = st.columns((2,1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(lottie_contact, height = 300)







                

