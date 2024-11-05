import streamlit as st

from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/pic.jpg", width=230)

with col2:
    st.title("Qamar Ibrahim", anchor=False)
    st.write(
        "Senior Web Developer , Digital Marketing Expert."
    )
    st.caption(
        "+971529733130 , qam600@gmail.com"
    )
    if st.button("✉️ Contact Me"):
        show_contact_form()


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Professional Summary", anchor=False)
st.write(
    """
    Professional Summary
    Python Django Developer and DevOps Engineer with extensive experience in AI chat integration, automation workflows, and cloud computing. Proficient in digital marketing, Google API integration, and containerized application deployment using Docker. Strong understanding of front-end technologies (React) with hands-on experience in troubleshooting and optimizing workflows. Passionate about delivering high-impact solutions that streamline operations and drive user engagement.
    """
)
# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 7 Years experience Web development and Digital marketing 
    - Strong hands-on experience and knowledge in Python and Flutter
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
)

# --- SKILLS ---
st.write("\n")
st.subheader(" Technical Skills", anchor=False)
st.write(
    """
   
- Languages & Frameworks  : Python, Django, HTML, CSS, JavaScript, React (basic)
- DevOps & Cloud          : Docker, GitHub, CI/CD, Google Cloud Platform (GCP), AWS, Microsoft Azure
- Automation & Integration: AI Chat Integration, Google API, Workflow Automation
- Digital Marketing       : SEO, Google Analytics, AdWords, Social Media Marketing
- Other                   : Windows troubleshooting, basic Linux, REST APIs, Version Control
    """
)
