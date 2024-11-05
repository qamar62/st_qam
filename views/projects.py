import streamlit as st

st.title("--My Projects--")
st.caption("Here all my Ai and python projects")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("", anchor=False)
st.write(
    """
   - Travel system 
   - Car rental system 
   - CRM complete backend solution 
- AI Chat Integration for [Specific Project/Client Name]
Developed a custom AI-powered chatbot using NLP libraries, achieving a 95% accuracy in user intent recognition. Integrated seamlessly with Django back-end, processing real-time customer queries and providing instant solutions.

- Automated Workflow System for Social Media and booking
Created an automated workflow solution integrating Google APIs to streamline data entry, analysis, and reporting. Reduced manual processing time by over 50%, enhancing productivity and data accuracy.

- Dockerized Application Deployment
Deployed a containerized Django application using Docker, configuring CI/CD pipelines that reduced release time by 40%. Implemented monitoring solutions to ensure high availability and quick incident response.
    """
)

# Project Card Function
def project_card(title, description, link):
    st.markdown(f"<div style='border: 1px solid #ccc; border-radius: 10px; padding: 15px; margin: 10px;'>"
                 f"<h3 style='margin: 0;'>{title}</h3>"
                 f"<p>{description}</p>"
                 f"<a href='{link}' target='_blank' style='color: blue;'>View Project</a>"
                 f"</div>", unsafe_allow_html=True)

# Example project information
project_title = "Trave and Tour Booking App"
project_description = "A web application for booking tours with integrated payment processing and real-time availability."
project_link = "arabianknightstours.com"

# Create project card
project_card(project_title, project_description, project_link)
# Project Card Function
def project_card(title, description, link):
    st.markdown(f"<div style='border: 1px solid #ccc; border-radius: 10px; padding: 15px; margin: 10px;'>"
                 f"<h3 style='margin: 0;'>{title}</h3>"
                 f"<p>{description}</p>"
                 f"<a href='{link}' target='_blank' style='color: blue;'>View Project</a>"
                 f"</div>", unsafe_allow_html=True)

# Example project information
project_title = "Car Rental System backend/Frontend"
project_description = "A web application for booking car rental with integrated payment processing and real-time availability."
project_link = "justdrivecar.me"

# Create project card
project_card(project_title, project_description, project_link)