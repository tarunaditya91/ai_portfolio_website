import streamlit as st
import google.generativeai as genai
import os


api_keyy=st.secrets["GOOGLE_API_KEY"]

genai.configure(api_key=api_keyy)

model = genai.GenerativeModel('gemini-1.5-flash')

persona="""You are Tarun Aditya AI bot. You help people answer questions about yourself (i.e., Tarun). Answer as if you are responding. Don't answer in the second or third person. If you don't know the answer, simply say "That's a secret."

Here is more info about Tarun:

I am Tarun Aditya, an Artificial and Machine Learning Intern at AITEUR in Bengaluru. I have hands-on experience in collecting, curating, and preprocessing high-quality image datasets, fine-tuning pre-trained models using SDXL LoRA, and deploying models for practical use. Previously, I worked as a Full-Stack Developer Intern at TATA Aerospace and Defence in Hyderabad, where I led the development of a community app and integrated RESTful APIs.

I have worked on projects like Image Generation using Stable Diffusion XL (Dreambooth) and Automatic Number Plate Recognition (ANPR) with Python, YOLOv8, and EasyOCR. I hold a B.Tech in Computer Science and Machine Learning from B V Raju Institute of Technology, expected to graduate in 2024. My technical skills include proficiency in C, C++, Python, HTML, CSS, JavaScript, and frameworks like ReactJs and Node.Js.

LinkedIn: Shanker Tarun Aditya
Email: tarunaditya91@gmail.com
GitHub: tarunaditya91
LeetCode: tarunaditya91
HackerRank: 20211a6651
CodeStudio: tarunaditya91
"""
col1,col2=st.columns(2)


with col1:
    st.subheader('Hi:wave:')
    st.title('I am Shanker Tarun Aditya')

with col2:
    st.image('images/tar3.JPG ')

st.title(' ')
st.title(' Shanker Tarun Aditya AI Bot' )
st.write('- Ask anything about me')
user_question=st.text_input('')
if st.button('ASK',use_container_width=400):
    prompt=persona+user_question
    response = model.generate_content(prompt)
    st.write(response.text )




st.subheader('Key Highlights')
st.markdown("""
    - **Artificial and Machine Learning Intern at AITEUR, Bengaluru**
    - **Full-Stack Developer Intern at TATA Aerospace and Defence, Hyderabad**
    - **Project: Image Generation Using Stable Diffusion XL (Dreambooth)**
    - **Project: Automatic Number Plate Recognition (ANPR) with Python, YOLOv8, and EasyOCR**
    """)

st.title('Improve_Video/Image_quality')
st.image('images/g1.png')
st.write('- Github Link:https://github.com/tarunaditya91/Improve_Video-Image_quality')


st.subheader('My Skills')
st.slider("C++",0,10,6)
st.slider("Python",0,10,8)
st.slider("Web Development",0,10,9)
st.slider("Mendix",0,10,5)


st.subheader('For any inquires,please contact me')
st.write('LinkedIn: https://www.linkedin.com/in/tarun-aditya-shanker-a13913242/')
st.write('Email: 20211a6651@bvrit.ac.in')



