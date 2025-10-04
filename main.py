import streamlit as st

# ================= CUSTOM BACKGROUND (with image) =================
page_bg = """
<style>
/* Background image full screen */
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1531297484001-80022131f5a1?auto=format&fit=crop&w=1920&q=80");
    background-size: cover;
    background-position: center;
}

/* Add glassmorphism effect for main content */
.main {
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    margin-top: 30px;
}

/* Hide default Streamlit elements */
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<h1 style='text-align: center; color:#1a237e;'>📄 My Resume</h1>", unsafe_allow_html=True)
st.write("")

# Wrap all main content in container div
st.markdown('<div class="main">', unsafe_allow_html=True)

# ================= PERSONAL INFO =================
col1, col2 = st.columns([1, 2])

with col1:
    st.image("images/profile.jpg", caption="Abdul Raziq", width=200)

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
skills = ["Python", "SQL", "Data Analysis", "IoT Systems", "Git/GitHub"]
for i, skill in enumerate(skills):
    cols[i % 3].markdown(f"<div style='padding:5px; background:#e3f2fd; border-radius:10px; text-align:center;'>{skill}</div>", unsafe_allow_html=True)
st.write("---")

# ================= PROJECTS =================
st.header("🚀 Projects & Achievements")

# ---- Project 1 ----
col1, col2 = st.columns([1.2, 2])
with col1:
    st.image("images/medical_box.jpg", caption="Smart Medical Box")
with col2:
    st.subheader("1. Smart Medical Box (IoT)")
    st.write("""
    - Developed a **smart medical box with 3 slots** to store medicines.  
    - Integrated with **ESP32** to control notifications and buzzer alerts.  
    - At the scheduled time, a **buzzer** and **notification** remind users to take their medication.  
    - Helps improve **medication adherence** among elderly users.  
    """)

# ---- Project 2 ----
col1, col2 = st.columns([1.2, 2])
with col1:
    st.image("images/coop_app.jpg", caption="COOP UMK App")
with col2:
    st.subheader("2. Online Cooperative Store (COOP UMK App)")
    st.write("""
    - Built an **Android app** for UMK students to check cooperative stock in real-time.  
    - Added **barcode scanner** for price lookup.  
    - Enabled **cashless payment & pickup system** to reduce queuing time.  
    """)

# ---- Project 3 ----
col1, col2 = st.columns([1.2, 2])
with col1:
    st.image("images/firefighting_robot.jpg", caption="Smart Firefighting Robot")
with col2:
    st.subheader("3. Smart Firefighting Robot (FYP)")
    st.write("""
    - Built a **robot** using flame sensors, GPS, ESP32-CAM, and MPU6050.  
    - Features **real-time fire detection** and alert via Android dashboard.  
    - Can detect fire hotspots and navigate automatically.  
    """)

# ---- Project 4 ----
col1, col2 = st.columns([1.2, 2])
with col1:
    st.image("images/solar_tracker.jpg", caption="Solar Tracking & Smart Lights")
with col2:
    st.subheader("4. Solar Tracking with Smart Street Lights")
    st.write("""
    - Created a **solar panel tracker** with LDR sensors and servo motor.  
    - Added **auto street light system** based on sunlight detection.  
    - Improves **energy efficiency** and renewable energy utilization.  
    """)

st.write("---")

# ================= FOOTER =================
st.markdown("<p style='text-align: center; color:#1a237e;'>Made with ❤️ by Abdul Raziq using Streamlit</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
