import streamlit as st

# ========== PAGE CONFIG ==========
st.set_page_config(page_title="My Resume", page_icon="📄", layout="wide")

# ========== HEADER ==========
st.title("📄 My Resume")
st.write("Welcome to my interactive resume built with Streamlit!")

# ========== PERSONAL INFO ==========
st.header("👤 Personal Information")
st.subheader("John Doe")
st.write("""
- 📧 Email: johndoe@example.com  
- 📱 Phone: +123 456 7890  
- 🔗 [LinkedIn](https://www.linkedin.com/in/johndoe)  
- 💻 [GitHub](https://github.com/johndoe)
""")

# ========== EDUCATION ==========
st.header("🎓 Education")
st.write("""
**Bachelor of Computer Science**  
University of Technology, 2019 – 2023  
- Graduated with First Class Honors
""")

# ========== WORK EXPERIENCE ==========
st.header("💼 Work Experience")
st.write("""
**Software Engineer – ABC Tech** (2023 – Present)  
- Developed web applications using Python, Django, and React.  
- Improved API response time by 30% with optimized database queries.  

**Intern – XYZ Solutions** (2022 – 2023)  
- Assisted in building data pipelines using Pandas & SQL.  
- Contributed to client dashboards with Streamlit.
""")

# ========== SKILLS ==========
st.header("🛠 Skills")
skills = ["Python", "Django", "Streamlit", "React", "SQL", "Machine Learning", "Git/GitHub"]
st.write(", ".join(skills))

# ========== PROJECTS ==========
st.header("🚀 Projects & Achievements")
st.write("""
- **Smart Irrigation System (IoT Project):** Automated watering using soil sensors.  
- **E-commerce Platform:** Developed full-stack web app for online shopping.  
- **Hackathon Winner:** 1st place at TechHack 2022 for AI-powered chatbot.
""")

# ========== FOOTER ==========
st.write("---")
st.caption("Made with ❤️ using Streamlit")
