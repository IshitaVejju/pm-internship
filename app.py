import streamlit as st
import pandas as pd
import io

# -----------------------------
# Load internship data
# -----------------------------
@st.cache_data
def load_data():
    try:
        return pd.read_csv("data/internship.csv")
    except FileNotFoundError:
        return pd.DataFrame(columns=["Title", "Company", "Location", "Apply_Link"])

# -----------------------------
# Internship Finder Page
# -----------------------------
def internship_finder():
    st.title("Internship Finder")
    st.write("Search and explore internships available for you.")

    df = load_data()
    if df.empty:
        st.warning("No internship data found. Please upload internship.csv in the `data/` folder.")
        return

    search = st.text_input("🔎 Search internships (by title, company, or location)").lower()

    if search:
        results = df[
            df.apply(lambda row: search in str(row.values).lower(), axis=1)
        ]
    else:
        results = df

    st.subheader("Results")
    st.dataframe(results)

    if not results.empty:
        for _, row in results.iterrows():
            st.markdown(
                f"""
                **{row['Title']}** at *{row['Company']}*  
                {row['Location']}  
                [Apply Here]({row['Apply_Link']})
                ---
                """
            )

# -----------------------------
# Career Advisor Page
# -----------------------------
def career_advisor():
    st.title("Career Advisor")
    st.write("Get simple AI-powered career advice.")

    role = st.text_input("Enter your dream role (e.g., Data Scientist, Web Developer)")
    skills = st.text_area("Enter your skills (comma separated)")

    if st.button("Get Advice"):
        if role and skills:
            st.success(f"Advice for becoming a **{role}**:")
            st.markdown(f"""
            - Keep improving your skills in **{skills}**  
            - Build a portfolio with real projects  
            - Apply for internships in related fields  
            - Network with professionals on LinkedIn  
            - Stay consistent and keep learning 
            """)
        else:
            st.error("⚠️ Please enter both role and skills.")

# -----------------------------
# Resume Builder Page
# -----------------------------
def resume_builder():
    st.title("📝 Resume Builder")
    st.write("Fill in your details and download your resume instantly.")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    linkedin = st.text_input("LinkedIn Profile")
    summary = st.text_area("Career Summary")

    st.subheader("Education")
    education = st.text_area("Enter education details")

    st.subheader("Experience")
    experience = st.text_area("Enter experience details")

    st.subheader("🛠 Skills")
    skills = st.text_area("List your skills (comma separated)")

    if st.button("Generate Resume"):
        if name and email and summary:
            resume_md = f"""
# {name}
📧 {email} | 📞 {phone} | 🔗 {linkedin}

---

## Career Summary
{summary}

## Education
{education}

## Experience
{experience}

## Skills
{skills}
"""
            st.subheader("Preview")
            st.markdown(resume_md)

            # Download option
            buffer = io.BytesIO()
            buffer.write(resume_md.encode("utf-8"))
            buffer.seek(0)

            st.download_button(
                label="Download Resume (Text Format)",
                data=buffer,
                file_name="resume.txt",
                mime="text/plain"
            )
        else:
            st.error("‼️Please fill in at least Name, Email, and Summary.")

# -----------------------------
# Contact Us Page
# -----------------------------
def contact_us():
    st.title("📞 Contact Us")
    st.write("Need help? Reach out below.")

    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if name and email and message:
            st.success("Thank you! Your message has been sent. We’ll get back to you soon.")
        else:
            st.error("⚠️ Please fill all fields before submitting.")

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
choice = st.sidebar.radio(
    "Go to",
    ["Internship Finder", "Career Advisor", "Resume Builder", "Contact Us"]
)

if choice == "Internship Finder":
    internship_finder()
elif choice == "Career Advisor":
    career_advisor()
elif choice == "Resume Builder":
    resume_builder()
elif choice == "Contact Us":
    contact_us()
