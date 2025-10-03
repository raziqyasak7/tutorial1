import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(page_title="My Resume", page_icon="📄", layout="wide")

# ================= HEADER =================
st.markdown("<h1 style='text-align: center;'>📄 My Resume</h1>", unsafe_allow_html=True)
st.write("")

# ================= PERSONAL INFO =================
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://via.placeholder.com/150", caption="Your Photo", width=150)  # Replace with your image URL

with col2:
    st.subheader("John Doe")
    st.write("""
    - 📧 **Email:** johndoe@example.com  
    - 📱 **Phone:** +123 456 7890  
    - 🔗 [LinkedIn](https://www.linkedin.com/in/johndoe)  
    - 💻 [GitHub](https://github.com/johndoe)  
    """)
st.write("---")

# ================= EDUCATION =================
st.header("🎓 Education")
st.write("""
**Bachelor of Computer Science** – University of Technology (2019 – 2023)  
- First Class Honors  
- Final Year Project: *Smart Irrigation System using IoT*
""")
st.write("---")

# ================= WORK EXPERIENCE =================
st.header("💼 Work Experience")
st.write("""
**Software Engineer – ABC Tech** (2023 – Present)  
- Built full-stack web applications using **Python, Django, React**.  
- Optimized database queries, improving performance by 30%.  
- Integrated APIs for payment systems and real-time dashboards.  

**Intern – XYZ Solutions** (2022 – 2023)  
- Developed **data pipelines** using Pandas & SQL.  
- Assisted in **customer dashboards** with Streamlit and Power BI.  
""")
st.write("---")

# ================= SKILLS =================
st.header("🛠 Skills")
cols = st.columns(3)
skills = ["Python", "Django", "Streamlit", "React", "SQL", 
          "Machine Learning", "Data Analysis", "IoT Systems", "Git/GitHub"]
for i, skill in enumerate(skills):
    cols[i % 3].write(f"- {skill}")
st.write("---")

# ================= PROJECTS =================
st.header("🚀 Projects & Achievements")

st.subheader("1. Smart Irrigation System (IoT)")
st.write("""
- Built an **IoT-based irrigation system** with soil sensors & ESP32.  
- Integrated with mobile app for real-time monitoring.  
- Helped reduce water usage by 25%.  
""")

st.subheader("2. Online Cooperative Store (COOP UMK App)")
st.write("""
- Developed a **Flutter app** for students to check item availability in real-time.  
- Integrated **barcode scanner** for product price details.  
- Implemented **online payment & pick-up system** (no queues).  
""")

st.subheader("3. Smart Firefighting Robot (FYP)")
st.write("""
- Built a **robot with flame sensors, GPS, and camera module**.  
- Implemented real-time fire detection with ESP32 + Streamlit dashboard.  
- Can auto-detect fire hotspots and send alerts.  
""")

st.subheader("4. Solar Tracking with Smart Street Lights")
st.write("""
- Designed a **solar panel tracker** using LDR sensors + servo motor.  
- Integrated **automatic street light control** based on sunlight.  
- Increased efficiency of solar harvesting by ~18%.  
""")

st.write("---")

# ================= FOOTER =================
st.markdown("<p style='text-align: center;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
