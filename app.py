import streamlit as st
import pandas as pd
from time import sleep
import io

# ------------------- Your existing PAGE CONFIG and STYLING -------------------
st.set_page_config(
    page_title="SmartAssigners | Internship Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# (keep all your previous <style> block unchanged)
# ------------------- HEADER -------------------
st.markdown("""
<div class="main-header">
    <div class="main-title">SmartAssigners</div>
    <div class="main-subtitle">Intelligent Internship Allocation & Career Development Platform</div>
</div>
""", unsafe_allow_html=True)

# ------------------- TABS -------------------
tab1, tab2, tab3, tab4 = st.tabs(["Internship Finder", "Career Advisor", "Resume Builder", "Contact Us"])

# ------------------- INTERNSHIP FINDER -------------------
with tab1:
    # (keep all your existing Internship Finder code exactly as is)
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
        internships = [
            {"Role": "AI/ML Research Intern", "Location": "Bengaluru", "Match Score": "92%", "Stipend": "₹12,000", "Sector": "Artificial Intelligence"},
            {"Role": "Data Science Intern", "Location": "Mumbai", "Match Score": "85%", "Stipend": "₹10,000", "Sector": "Data Science"},
            {"Role": "Full Stack Developer", "Location": "Delhi", "Match Score": "80%", "Stipend": "₹8,000", "Sector": "Web Development"}
        ]
        st.markdown(f'<div class="success-message">Found {len(internships)} excellent opportunities matching your profile!</div>', unsafe_allow_html=True)
        st.markdown('<div class="professional-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="section-header">Opportunity Comparison</h3>', unsafe_allow_html=True)
        df = pd.DataFrame(internships)
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="professional-card">', unsafe_allow_html=True)
        st.markdown('<h3 class="section-header">Detailed View</h3>', unsafe_allow_html=True)
        cols = st.columns(len(internships))
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
        st.markdown('</div>', unsafe_allow_html=True)

# ------------------- CAREER ADVISOR -------------------
with tab2:
    # (keep all your existing Career Advisor code exactly as is)
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Personalized Career Guidance</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns([1,1])
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
        advice_items = [
            {"title":"Strengthen Technical Foundation","content":"Focus on mastering core technologies like Python, SQL, and cloud platforms. Build hands-on projects that demonstrate your expertise and problem-solving abilities.","class":"advice-primary"},
            {"title":"Develop Professional Portfolio","content":"Create a compelling portfolio showcasing your best work. Include detailed case studies, code repositories on GitHub, and maintain an active professional presence on LinkedIn.","class":"advice-secondary"},
            {"title":"Expand Professional Network","content":"Engage with industry professionals through conferences, meetups, and online communities. Consider mentorship opportunities and contribute to open-source projects.","class":"advice-tertiary"}
        ]
        for advice in advice_items:
            st.markdown(f"""
            <div class="advice-card {advice['class']}">
                <div class="advice-title">{advice['title']}</div>
                <div class="advice-content">{advice['content']}</div>
            </div>
            """, unsafe_allow_html=True)

# ------------------- RESUME BUILDER -------------------
with tab3:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Resume Builder</h2>', unsafe_allow_html=True)
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn URL")
    summary = st.text_area("Career Summary")
    education = st.text_area("Education Details")
    experience = st.text_area("Experience Details")
    skills = st.text_area("Skills (comma separated)")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Generate Resume"):
        if name and email:
            resume_text = f"""
{name}
Email: {email} | Phone: {phone} | LinkedIn: {linkedin}

Summary:
{summary}

Education:
{education}

Experience:
{experience}

Skills:
{skills}
"""
            st.subheader("Preview")
            st.text(resume_text)
            st.download_button("Download Resume", data=resume_text, file_name="resume.txt")
        else:
            st.error("Please fill at least Name and Email.")

# ------------------- CONTACT US -------------------
with tab4:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Contact Us</h2>', unsafe_allow_html=True)
    cname = st.text_input("Your Name")
    cemail = st.text_input("Your Email")
    cmessage = st.text_area("Message")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Send Message"):
        if cname and cemail and cmessage:
            st.success("✅ Message sent successfully! We'll contact you soon.")
        else:
            st.error("⚠️ Please fill all fields.")
