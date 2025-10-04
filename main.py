import streamlit as st

# ================= HEADER =================
st.markdown("<h1 style='text-align: center;'>📄 My Resume</h1>", unsafe_allow_html=True)
st.write("")

# ================= PERSONAL INFO =================l
col1, col2 = st.columns([1, 2])

with col1:
    st.image("images/profile.jpg", caption="Abdul Raziq", width=200)  # Profile photo

with col2:
    st.subheader("Abdul Raziq Bin Mohd Yasak")
    st.write("""
    - 📧 **Email:** raziqyasak10@gmail.com  
    - 📱 **Phone:** 011-11112707  
    - 🔗 [LinkedIn](https://www.linkedin.com/in/raziqyasak10)  
    - 💻 [GitHub](https://github.com/raziqyasak7)  
    """)
st.write("---")

# ================= EDUCATION =================
st.header("🎓 Education")
st.write("""
**Bachelor Of Information Technology With Honours** – University Malaysia Kelantan (2022 – 2026)  
- Final Year Project: *Smart FireFighting Robot With Real-Time Fire Detection*
""")
st.write("---")

# ================= SKILLS =================
st.header("🛠 Skills")
cols = st.columns(3)
skills = ["Python", "SQL", "Machine Learning", "Data Analysis", "IoT Systems", "Git/GitHub"]
for i, skill in enumerate(skills):
    cols[i % 3].write(f"- {skill}")
st.write("---")

# ================= PROJECTS =================
st.header("🚀 Projects & Achievements")

# ---- Project 1 ----
col1, col2 = st.columns([1.5, 2])
with col1:
    st.image("images/medical_box.jpg", caption="Smart Medical Box")  
with col2:
    st.subheader("1. Smart Medical Box (IoT)")
    st.write("""
    - Developed a **smart medical box with 3 slots** to store medicines.  
    - Integrated with **ESP32** to control notifications and buzzer alerts.  
    - At the scheduled time, the system triggers a **buzzer sound** and **notification** to remind users to take their medication.  
    - Designed to improve **medication adherence** for patients with chronic illnesses and elderly users.  
    """)

# ---- Project 2 ----
col1, col2 = st.columns([1.5, 2])
with col1:
    st.image("images/coop_app.jpg", caption="COOP UMK App")  
with col2:
    st.subheader("2. Online Cooperative Store (COOP UMK App)")
    st.write("""
    - Developed a **Flutter app** for students to check item availability in real-time.  
    - Integrated **barcode scanner** for product price details.  
    - Implemented **online payment & pick-up system** (no queues).  
    """)

# ---- Project 3 ----
col1, col2 = st.columns([1.5, 2])
with col1:
    st.image("images/firefighting_robot.jpg", caption="Smart Firefighting Robot")  
with col2:
    st.subheader("3. Smart Firefighting Robot (FYP)")
    st.write("""
    - Built a **robot with flame sensors, GPS, and camera module**.  
    - Implemented real-time fire detection with ESP32 + Streamlit dashboard.  
    - Can auto-detect fire hotspots and send alerts.  
    """)

# ---- Project 4 ----
col1, col2 = st.columns([1.5, 2])
with col1:
    st.image("images/solar_tracker.jpg", caption="Solar Tracking & Smart Lights")  
with col2:
    st.subheader("4. Solar Tracking with Smart Street Lights")
    st.write("""
    - Designed a **solar panel tracker** using LDR sensors + servo motor.  
    - Integrated **automatic street light control** based on sunlight.  
    - Increased efficiency of solar harvesting by ~18%.  
    """)

st.write("---")


