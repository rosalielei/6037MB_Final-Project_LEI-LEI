import streamlit as st

def education_page():
    st.markdown("## Education")
    
    st.markdown(""" 
    ### Master Degree of Science in Marketing  
    **The Chinese University of Hong Kong (CUHK)**  
    **HongKong, China**| *Aug 2024 - July 2025*
    - GPA: 3.6/4.0
    - Course: Marketing Research, Buyer Behavior, Digital Marketing, Customer Analytics, Social Media Analytics, Marketing Analytics
    
    ### Bachelor of Economics
    **East China Normal University (ECNU)**  
    **Shanghai, China** | *Aug 2020 - July 2024*
    - GPA: 3.5/4.0
    - Course: Mathematical Analysis, Mathematical Statistic, Probability Theory, Linear Algebra, Econometrics, Data Base and Statistical Software, Game Theory
    
    ### Berkeley International Study Program
    **University of California, Berkeley (UCB)**  
    **California, United States** | *Jan 2023- May 2023*
    - GPA: 4.0/4.0
    - Course: Asset pricing and Portfolio Choice, Financial Accounting, Urban Economics
    """)
    
    st.markdown("---")
    
    st.markdown("## Certifications")
    
    cert1, cert2 = st.columns(2)
    
    with cert1:
        st.markdown("""
        ### Xiaohongshu Marketing Competence Certification：  
        #### Primary  
        **Xiaohongshu** | *November 2023*
        """)

    with cert2:
        st.markdown("""
        ### Putonghua Proficiency Test：  
        #### Grade 2, Class A  
        **Putonghua Proficiency Test** | *July 2024*
        
        """)
    
    st.markdown("---")
    
    st.markdown("## Academic Projects")
    
    st.markdown("""
    #### Successful Overseas Marketing Case of a Domestic Game —— "Black Myth: Wukong"
    Use Python and API crawlers to obtain the data performance of "Black Myth: Wukong" on YouTube, TikTok, and Steam. Then, conduct data analysis and visualization such as traffic analysis, text sentiment analysis, and word cloud charts. Compare the overseas performance of domestic games of the same type. Combine with the 4P theory to summarize the reasons for the successful overseas launch of "Black Myth: Wukong".
    
    #### Analysis and Suggestions on the Current Situation of Commercial Advertising Revenue on Bilibili
    Conduct a case analysis on the imperfect commercialization system of Bilibili's advertising. First, I collected and sorted out the annual reports of Bilibili over the years, and conducted data analysis using Excel and Stata. By comparing with competing products Based on the successful commercialization cases of the company, combined with the 4P theory and STP strategy, this paper explores Bilibili's market positioning, user profile and potential business opportunities. Personalized commercialization for Bilibili has been formulated
    """)
    
    st.markdown("---") 