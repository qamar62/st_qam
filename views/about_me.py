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
    if st.button("✉️ Contact Me"):
        show_contact_form()


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
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python (Django, Streamlit, DevOps, Cloud Computing)
    - SEM, SEO, 
    - Automation, Server Deployment , Ai chat integration, Whatsapp Bot 
    - Digital Ocean project Deployment: 
    - Databases: Postgres
    """
)
