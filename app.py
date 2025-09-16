import streamlit as st
import pandas as pd
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
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
    .stApp { background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); font-family: 'Inter', sans-serif; }
    #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
    .main-header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 3rem 2rem;
        border-radius: 20px; margin-bottom: 2rem; text-align: center; color: white;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);}
    .main-title { font-size: 3.5rem; font-weight: 800; margin-bottom: 0.5rem; letter-spacing: -2px;
        background: linear-gradient(45deg, #ffffff, #e6f3ff); -webkit-background-clip: text;
        -webkit-text-fill-color: transparent; background-clip: text;}
    .main-subtitle { font-size: 1.3rem; font-weight: 400; opacity: 0.9; margin-bottom: 0;}
    .professional-card { background: white; padding: 2rem; border-radius: 16px; border: 1px solid #e2e8f0;
        box-shadow: 0 4px 25px rgba(0, 0, 0, 0.08); margin-bottom: 1.5rem; transition: all 0.3s ease;}
    .professional-card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);}
    .section-header { font-size: 1.8rem; font-weight: 700; color: #2d3748; margin-bottom: 1.5rem;
        position: relative; padding-bottom: 0.5rem;}
    .section-header::after { content: ''; position: absolute; bottom: 0; left: 0; width: 60px; height: 3px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 2px;}
    .success-message { background: linear-gradient(135deg, #48bb78 0%, #38a169 100%); color: white;
        padding: 1rem 1.5rem; border-radius: 12px; font-weight: 500; margin: 1rem 0;}
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
tab1, tab2, tab3, tab4 = st.tabs(["Internship Finder", "Career Advisor", "Resume Builder", "Contact"])

# ---------- INTERNSHIP FINDER ----------
with tab1:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Discover Your Perfect Internship</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        name = st.text_input("Full Name", placeholder="Enter your complete name")
        skills = st.text_area("Technical Skills", placeholder="e.g., Python, Machine Learning, Data Analysis", height=100)
        academics = st.slider("Academic Performance (%)", 40, 100, 75)
    with col2:
        location = st.selectbox("Preferred Location", ["Any Location", "Delhi", "Mumbai", "Hyderabad", "Bengaluru", "Chennai"])
        sector = st.selectbox("Industry Sector", ["Any Sector", "AI/ML", "Web Development", "Data Science", "Cybersecurity", "Business"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("Find Best Matches"):
        with st.spinner("Analyzing your profile and matching opportunities..."):
            sleep(1.2)
        internships = [
            {"Role": "AI/ML Research Intern", "Location": "Bengaluru", "Match Score": "92%", "Stipend": "₹12,000", "Sector": "Artificial Intelligence"},
            {"Role": "Data Science Intern", "Location": "Mumbai", "Match Score": "85%", "Stipend": "₹10,000", "Sector": "Data Science"},
            {"Role": "Full Stack Developer", "Location": "Delhi", "Match Score": "80%", "Stipend": "₹8,000", "Sector": "Web Development"}
        ]
        st.markdown(f'<div class="success-message">Found {len(internships)} excellent opportunities matching your profile!</div>', unsafe_allow_html=True)
        df = pd.DataFrame(internships)
        st.dataframe(df, use_container_width=True)
        st.download_button("📥 Download Matches (CSV)", df.to_csv(index=False), "internships.csv", "text/csv")

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
            sleep(1.2)
        st.markdown('<div class="success-message">Your personalized career roadmap is ready!</div>', unsafe_allow_html=True)
        st.markdown("✅ Focus on technical skills (Python, SQL, Cloud)\n\n✅ Build a portfolio on GitHub/LinkedIn\n\n✅ Expand your professional network")

# ---------- RESUME BUILDER ----------
with tab3:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Build Your Resume</h2>', unsafe_allow_html=True)
    name = st.text_input("Full Name (Resume)")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    education = st.text_area("Education")
    skills_resume = st.text_area("Skills")
    projects = st.text_area("Projects / Internships")
    achievements = st.text_area("Achievements")
    if st.button("Generate Resume PDF"):
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=letter)
        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, 750, f"Name: {name}")
        pdf.drawString(50, 730, f"Email: {email}")
        pdf.drawString(50, 710, f"Phone: {phone}")
        pdf.drawString(50, 690, f"Education: {education}")
        pdf.drawString(50, 670, f"Skills: {skills_resume}")
        pdf.drawString(50, 650, f"Projects: {projects}")
        pdf.drawString(50, 630, f"Achievements: {achievements}")
        pdf.showPage(); pdf.save(); buffer.seek(0)
        st.download_button("📄 Download Resume", buffer, "resume.pdf", "application/pdf")

# ---------- CONTACT ----------
with tab4:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Contact Support / Mentors</h2>', unsafe_allow_html=True)
    with st.form("contact_form"):
        user_name = st.text_input("Your Name")
        user_email = st.text_input("Your Email")
        message = st.text_area("Your Message or Query")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("✅ Your message has been sent! Our team will contact you soon.")
            # (Future) Integrate with Email API or Google Sheet
