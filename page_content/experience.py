import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    st.markdown("## Professional Experience")
    
    st.markdown("""
    ### Commercial Advertising Product Operation Internship
    **Xiaohongshu Technology Co., Ltd.** | *Mar 2024-Jun 2024*
    
    - Data processing and analyzing: Responsible for advertising products operation, in-depth monitoring and analysis of delivery data effect, including Average Daily Consumption/ Optimization Range of Interactive Cost Comparison and Click, etc. In the internship period, the optimization target consumption increased from 240,000 in March to 1.8 million during 618, stabilizing at an average daily consumption of about 1 million in June, an increase of 300% y
    - Product optimization: Coordinate with internal resources, conduct product demand research, test and operation monitor, promote the continuous improvement of products. Troubleshoot the problem of positioning account Settings by drilling down the AD delivery account.
    - New Product Testing: Follow up the A/B Test process of anti-funnel expansion of new products throughout the process. Put forward product requirements in the early stage, conduct relevant customer brand research and feasibility analysis, and assist in writing PRD documents. Mid-term implementation, tracking and monitoring, optimizing the test effect, communicating and cooperating with the department to solve product testing problems.
    """)
    
    st.markdown("""
    ### Xiaohongshu advertising optimization - Data Intern
    **Inly Media Co., Ltd.** | *Nov 2023- Feb 2024*
    
    - Data processing: Proficient in using Excel pivot tables and VLOOKUP to complete various data reports, cooperated with the use of platforms, for preinvestment insight and post-investment review required for industry market data, product site data, competitive product analysis. Assisted in the completion of part of the investment plan and budget planning. During the internship, I participated in the investment FS plan of about 15 brands。
    - Social media delivery and optimization: familiar with Xiaohongshu's platform delivery rules and product planting logic, passed the professional ability certification of Xiaohongshu marketing talents. During the period of client advertising, cooperate with the product launch, build the advertising plan, observe the performance of the advertising, track and optimize the parameters of the advertising effect, like exposure, ctr, cpc, cpe,""")
    
    st.markdown("""
    ### University Department - Marketing Intern (Online)
    **Hygiene Heroes (a non-profit organization)** | *Jan 2025 - April 2025*
    
    - Content and marketing work: Responsible for Xiaohongshu content creation, format optimization, and KOL collaboration. Planned and executed marketing activities, designed promotional materials, and supported product brand building.
    - Community operation and market research: Operated and maintained a university student community, collected user feedback, organized community activities, and assisted in analyzing user needs and providing suggestions for product improvement.
    """)
    
    st.markdown("---")
    
    st.markdown("## Projects")
    
    projects = [
        {
            "title": "Undergraduate Innovation and Entrepreneurship Training Project",
            "time": "May 2021- Sep 2021",
            "character": "Core Member",
            "skills": ["Stata", "Entrepreneurship", "Market Research", "Data Analysis"],
        },
        {
            "title": "Star School College Youth Talent Training Camp by ICBC and ECNU",
            "time": "Jun 2021- May 2022",
            "character": "Core Member",
            "skills": ["Fiancial Management", "Business Acumen","Data Analysis","Project Management"],
        },
        {
            "title": "University of California, Berkeley International Cultural Festival",
            "time": "Mar 2023-Apr 2023",
            "character": "Core Member",
            "skills": ["Cross-Cultural Communication", "Intercultural Fluency", "Event Coordination/Organization", "Canva Design"],
        }
    ]
    
    for i, project in enumerate(projects):
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"**Time:** {project['time']}")
            st.markdown(f"**Character:** {project['character']}")
            st.markdown(f"**Skills Used:** {', '.join(project['skills'])}")
    
    # Add the interactive visualization demo
    with st.expander("Interactive Data Visualization Demo", expanded=False):
        st.markdown("**Description:** An interactive demonstration of various data visualization techniques.")
        display_interactive_chart()
    
    st.markdown("---")
    
    st.markdown("## Professional Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Technical Skills
        - **Programming Languages:** Python, R, SQL, JavaScript
        - **Machine Learning:** scikit-learn, TensorFlow, PyTorch
        - **Data Processing:** Pandas, NumPy, PySpark
        - **Visualization:** Matplotlib, Seaborn, Tableau, PowerBI
        - **Cloud Platforms:** Google Cloud
        """)
        
    with col2:
        st.markdown("""
        ### Soft Skills
        - **Communication:** Excellent written and verbal communication
        - **Teamwork:** Collaborative team player with experience in project management and leadership
        - **Problem-solving:** Skilled at identifying and resolving complex problems
        - **Time Management:** Efficient at prioritizing tasks
        - **Leadership:** Experience leading small teams and mentoring junior colleagues
        - **Adaptability:** Quick learner and flexible in changing environments
        """)
    
    st.markdown("---") 