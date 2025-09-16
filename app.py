import streamlit as st
import pandas as pd
from time import sleep

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="SmartAssigners | Internship Platform", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- ENHANCED STYLING ----------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main Header Styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        text-align: center;
        color: white;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
    }
    
    .main-title {
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -2px;
        background: linear-gradient(45deg, #ffffff, #e6f3ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .main-subtitle {
        font-size: 1.3rem;
        font-weight: 400;
        opacity: 0.9;
        margin-bottom: 0;
    }
    
    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
        padding: 1rem 0;
        border-bottom: 2px solid #e1e5e9;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        padding: 0 2rem;
        background-color: white;
        border-radius: 12px;
        border: 2px solid #e1e5e9;
        font-weight: 600;
        font-size: 1.1rem;
        color: #4a5568;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border-color: transparent;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
    }
    
    /* Card Components */
    .professional-card {
        background: white;
        padding: 2rem;
        border-radius: 16px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .professional-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
    }
    
    .section-header {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 1.5rem;
        position: relative;
        padding-bottom: 0.5rem;
    }
    
    .section-header::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        width: 60px;
        height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 2px;
    }
    
    /* Enhanced Form Styling */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div > select {
        border-radius: 10px !important;
        border: 2px solid #e2e8f0 !important;
        padding: 12px 16px !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1) !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 12px 32px;
        font-weight: 600;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        width: 100%;
        height: 55px;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    
    /* Success Message */
    .success-message {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 12px;
        font-weight: 500;
        margin: 1rem 0;
    }
    
    /* Data Table Styling */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }
    
    /* Internship Cards */
    .internship-card {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .internship-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
    }
    
    .internship-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 1rem;
    }
    
    .internship-detail {
        display: flex;
        align-items: center;
        margin-bottom: 0.5rem;
        color: #4a5568;
        font-size: 0.95rem;
    }
    
    .match-score {
        background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
        display: inline-block;
        margin-top: 0.5rem;
    }
    
    /* Career Advice Cards */
    .advice-card {
        background: white;
        border-radius: 16px;
        padding: 2rem;
        border-left: 5px solid;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .advice-card:hover {
        transform: translateX(5px);
    }
    
    .advice-primary {
        border-color: #667eea;
    }
    
    .advice-secondary {
        border-color: #ed8936;
    }
    
    .advice-tertiary {
        border-color: #38b2ac;
    }
    
    .advice-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 0.8rem;
    }
    
    .advice-content {
        color: #4a5568;
        line-height: 1.6;
        font-size: 1rem;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2.5rem;
        }
        
        .main-header {
            padding: 2rem 1rem;
        }
        
        .professional-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="main-header">
    <div class="main-title">SmartAssigners</div>
    <div class="main-subtitle">Intelligent Internship Allocation & Career Development Platform</div>
</div>
""", unsafe_allow_html=True)

# ---------- TABS ----------
tab1, tab2, tab3, tab4 = st.tabs(["Internship Finder", "Career Advisor", "Resume Builder", "Contact Us"])

# ---------- INTERNSHIP FINDER ----------
with tab1:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Discover Your Perfect Internship</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        name = st.text_input("Full Name", placeholder="Enter your complete name")
        skills = st.text_area("Technical Skills", placeholder="e.g., Python, Machine Learning, Data Analysis", height=100)
        academics = st.slider("Academic Performance (%)", 40, 100, 75, help="Your overall academic percentage")
    
    with col2:
        location = st.selectbox("Preferred Location", 
                               ["Any Location", "Delhi", "Mumbai", "Hyderabad", "Bengaluru", "Chennai"],
                               help="Select your preferred internship location")
        sector = st.selectbox("Industry Sector", 
                             ["Any Sector", "AI/ML", "Web Development", "Data Science", "Cybersecurity", "Business"],
                             help="Choose your area of interest")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Find Best Matches"):
        with st.spinner("Analyzing your profile and matching opportunities..."):
            sleep(1.8)

            # Load CSV
            df_internships = pd.read_csv("data/internship.csv")

            matched_internships = []

            for idx, intern in df_internships.iterrows():
                score = 50  # base score

                # Location match
                if location != "Any Location" and location == intern["Location"]:
                    score += 20

                # Sector match
                if sector != "Any Sector" and sector.lower() in intern["Sector"].lower():
                    score += 25

                # Skills/Requirements match
                user_skills = [s.strip().lower() for s in skills.split(",")]
                intern_skills = [s.strip().lower() for s in str(intern.get("Requirements","")).split(",")]
                if intern_skills:
                    skill_matches = len(set(user_skills) & set(intern_skills))
                    score += skill_matches * 5  # 5 points per matching skill

                # Academic performance vs MinPercent
                min_percent = intern.get("MinPercent", 0)
                if academics >= min_percent:
                    score += 10  # extra points if eligible
                else:
                    score -= 20  # penalize if below requirement

                matched_internships.append({
                    "Role": intern["Title"],
                    "Location": intern["Location"],
                    "Match Score": f"{min(max(score,0),100)}%",
                    "Stipend": intern["Stipend"],
                    "Sector": intern["Sector"]
                })

            # Sort by Match Score
            matched_internships = sorted(matched_internships, key=lambda x: int(x["Match Score"].replace("%","")), reverse=True)

            # Display top 3
            internships = matched_internships[:3]

            st.markdown(f'<div class="success-message">Found {len(internships)} excellent opportunities matching your profile!</div>', unsafe_allow_html=True)

            # Comparison Table
            st.markdown('<div class="professional-card">', unsafe_allow_html=True)
            st.markdown('<h3 class="section-header">Opportunity Comparison</h3>', unsafe_allow_html=True)
            df = pd.DataFrame(internships)
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.markdown('</div>', unsafe_allow_html=True)

            
# Detailed Cards
st.markdown('<div class="professional-card">', unsafe_allow_html=True)
st.markdown('<h3 class="section-header">Detailed View</h3>', unsafe_allow_html=True)

cols = st.columns(len(internships))  # <-- fixed indentation
for col, internship in zip(cols, internships):
    with col:
        st.markdown(f"""
        <div class="internship-card">
            <div class="internship-title">{internship['Role']}</div>
            <div class="internship-detail">📍 {internship['Location']}</div>
            <div class="internship-detail">💰 {internship['Stipend']}</div>
            <div class="internship-detail">🏢 {internship['Sector']}</div>
            <div class="match-score">Match: {internship['Match Score']}</div>
        </div>
        """, unsafe_allow_html=True)

# Close the parent div outside of the for loop
st.markdown('</div>', unsafe_allow_html=True)

# ---------- CAREER ADVISOR ----------
with tab2:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Personalized Career Guidance</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        role = st.text_input("Target Role", placeholder="e.g., Data Scientist, Software Engineer")
        skills_list = st.text_area("Current Skill Set", placeholder="List your current technical and soft skills", height=120)
    
    with col2:
        experience = st.selectbox("Experience Level", ["Entry Level", "Mid Level", "Senior Level"])
        
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Get Career Roadmap"):
        with st.spinner("Creating your personalized career development plan..."):
            sleep(1.8)

        st.markdown('<div class="success-message">Your personalized career roadmap is ready!</div>', unsafe_allow_html=True)

        # Career Advice Cards
        advice_items = [
            {
                "title": "Strengthen Technical Foundation",
                "content": "Focus on mastering core technologies like Python, SQL, and cloud platforms. Build hands-on projects that demonstrate your expertise and problem-solving abilities.",
                "class": "advice-primary"
            },
            {
                "title": "Develop Professional Portfolio",
                "content": "Create a compelling portfolio showcasing your best work. Include detailed case studies, code repositories on GitHub, and maintain an active professional presence on LinkedIn.",
                "class": "advice-secondary"
            },
            {
                "title": "Expand Professional Network",
                "content": "Engage with industry professionals through conferences, meetups, and online communities. Consider mentorship opportunities and contribute to open-source projects.",
                "class": "advice-tertiary"
            }
        ]

        for advice in advice_items:
            st.markdown(f"""
            <div class="advice-card {advice['class']}">
                <div class="advice-title">{advice['title']}</div>
                <div class="advice-content">{advice['content']}</div>
            </div>
            """, unsafe_allow_html=True)

# ---------- RESUME BUILDER ----------
with tab3:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Resume Builder</h2>', unsafe_allow_html=True)

    r_name = st.text_input("Full Name", key="r_name")
    r_email = st.text_input("Email", key="r_email")
    r_phone = st.text_input("Phone Number", key="r_phone")
    r_linkedin = st.text_input("LinkedIn URL", key="r_linkedin")
    r_summary = st.text_area("Career Summary", key="r_summary")
    r_education = st.text_area("Education Details", key="r_education")
    r_experience = st.text_area("Experience Details", key="r_experience")
    r_skills = st.text_area("Skills (comma separated)", key="r_skills")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Generate Resume"):
        if r_name and r_email:
            resume_text = f"""
{r_name}
Email: {r_email} | Phone: {r_phone} | LinkedIn: {r_linkedin}

Summary:
{r_summary}

Education:
{r_education}

Experience:
{r_experience}

Skills:
{r_skills}
"""
            st.subheader("Preview")
            st.text(resume_text)
            st.download_button("Download Resume", data=resume_text, file_name="resume.txt")
        else:
            st.error("Please fill at least Name and Email.")

# ---------- CONTACT US ----------
with tab4:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Contact Us</h2>', unsafe_allow_html=True)

    c_name = st.text_input("Your Name", key="c_name")
    c_email = st.text_input("Your Email", key="c_email")
    c_message = st.text_area("Message", key="c_message")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Send Message"):
        if c_name and c_email and c_message:
            st.success("Message sent successfully! We'll contact you soon.")
        else:
            st.error("Please fill all fields.")

# ---------- FOOTER ----------
st.markdown("""
<hr style="border:1px solid #e2e8f0">
<div style="text-align:center; color:#4a5568; font-size:0.9rem; margin-top:10px;">
    Need Help? Contact us at 
    <a href="mail to:support@smartAssigners.com">support@smartassigners.com</a>
</div>
""", unsafe_allow_html=True)



    st.markdown("</div>", unsafe_allow_html=True)


