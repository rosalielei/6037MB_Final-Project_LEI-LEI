import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>LEI LEI</h4>
        Status: Recent Master's Graduate in Marketing<br>
        Graduate: Chinese University of Hong Kong<br>
        Address: 8 Shan Tong Road, Mid-Levels, Tai Po, New Territories, Hong Kong<br>
        Email: <a href="mailto:sarah.johnson@example.com">lleirosalie@163.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join("static", "images", "image.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### About Me
        - Master of Marketing from The Chinese University of Hong Kong (ranked 36th in QS), Bachelor of Economics from East China Normal University (985 and Double First-Class). 
        - I am passionate about the Internet industry, familiar with the commercialization logic of Internet products and the logic of optimizing advertising placement effects. I have internship experience in the operation of commercial seeding advertising products on Xiaohongshu. I possess strong logical thinking ability, problem-solving skills and document writing skills 
        - Understand the gameplay and rules of various social media community platforms, have a marketing talent certification from Xiaohongshu and a student certificate of product operation experience Officer from NetEase 
        - Sensitive to data, proficient in using office, Python, SQL and other tools for data analysis, with strong learning ability 
        - Fluent in English, with a CET-6 score of 524 and a TOEFL score of 95. Has overseas exchange experience at the University of California, Berkeley (ranked among the top 20 by QS) 
        - Outgoing in personality, good at cooperation, patient, meticulous and responsible in work"""
    )

    st.markdown(
        """
        ### Skills
        - **Marketing**: Proficient in Advertising, SEO, SEM, Data Analysis, etc.
        - **Coding**: Proficient in Offices, Python, Stata, R, Web Crawling, etc.
        - **Language**: Chinese(native), English (TOEFL 95), GRE (315+) 
        - **Certification**: Xiaohongshu Marketing Competence Certification: Primary
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page 