import streamlit as st
import pandas as pd
import io
from time import sleep

# ========================
# PAGE CONFIG
# ========================
st.set_page_config(page_title="PM Internship Finder", page_icon="🔎", layout="wide")

# ========================
# CUSTOM CSS
# ========================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
}
.section-header {
    font-size: 26px;
    font-weight: bold;
    color: #2c3e50;
    margin-bottom: 15px;
}
.professional-card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.stTabs [data-baseweb="tab-list"] {
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

# ========================
# HEADER
# ========================
st.title("Internship Finder & Career Assistant")
st.markdown("Helping students discover the **right internships, career advice, and resume tools**.")

# ========================
# TABS
# ========================
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Internship Finder", "🧭 Career Advisor", "📝 Resume Builder", "📞 Contact"])

# ========================
# TAB 1: INTERNSHIP FINDER
# ========================
with tab1:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Find Matching Internships</h2>', unsafe_allow_html=True)

    skills = st.text_area("Enter your skills (comma separated)", "Python, Data Analysis, SQL")
    role = st.selectbox("Preferred Role", ["Data Scientist", "ML Engineer", "Software Developer", "Product Manager"])

    if st.button("Find Internships"):
        with st.spinner("🔎 Searching best matches..."):
            sleep(1.5)

        data = {
            "Internship Role": ["Data Analyst", "Software Intern", "ML Engineer", "Product Manager Intern"],
            "Company": ["TCS", "Infosys", "Google", "Flipkart"],
            "Location": ["Hyderabad", "Bangalore", "Remote", "Mumbai"],
            "Match Score": ["92%", "85%", "78%", "88%"]
        }
        df = pd.DataFrame(data)

        st.success("✅ Found best internships for you!")
        st.dataframe(df, use_container_width=True)

        st.download_button("📥 Download Matches (CSV)", df.to_csv(index=False), "internships.csv", "text/csv")

    st.markdown('</div>', unsafe_allow_html=True)

# ========================
# TAB 2: CAREER ADVISOR
# ========================
with tab2:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">AI Career Advisor</h2>', unsafe_allow_html=True)

    role = st.selectbox("Choose your target role", ["Data Scientist", "ML Engineer", "Software Developer", "Product Manager"])
    if st.button("Get Career Advice"):
        if role == "Data Scientist":
            st.info("📌 Learn Python, SQL, Machine Learning, Statistics, and build Kaggle projects.")
        elif role == "ML Engineer":
            st.info("📌 Focus on TensorFlow/PyTorch, deep learning, deployment (FastAPI/Streamlit).")
        elif role == "Software Developer":
            st.info("📌 Master DSA, system design, and contribute to open-source projects.")
        elif role == "Product Manager":
            st.info("📌 Build leadership, problem-solving, user research, and agile methodology skills.")

    st.markdown('</div>', unsafe_allow_html=True)

# ========================
# TAB 3: RESUME BUILDER
# ========================
with tab3:
    st.markdown('<div class="professional-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">Build Your Resume</h2>', unsafe_allow_html=True)

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    education = st.text_area("Education (e.g., B.Tech CSE, VFSTR University, 2022-2026)")
    skills = st.text_area("Skills")
    projects = st.text_area("Projects / Internships")
    achievements = st.text_area("Achievements")

    if st.button("Preview Resume"):
        st.subheader("Resume Preview")
        resume_md = f"""
# {name}

{email} |  {phone}

## Education
{education}

## Skills
{skills}

## Projects & Internships
{projects}

## Achievements
{achievements}
"""
        st.markdown(resume_md)

        buffer = io.BytesIO()
        buffer.write(resume_md.encode("utf-8"))
        buffer.seek(0)

        st.download_button(
            label=" Download Resume (Text)",
            data=buffer,
            file_name="resume.txt",
            mime="text/plain"
        )

    st.markdown('</div>', unsafe_allow_html=True)

# ========================
# TAB 4: CONTACT
# ========================
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

    st.markdown("""
    ---
     support@internfinder.in  
     [LinkedIn](https://linkedin.com) | [GitHub](https://github.com) | [Website](https://Pm internship.com)
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
