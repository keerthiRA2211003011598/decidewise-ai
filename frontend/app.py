import streamlit as st
import requests

# Page config
st.set_page_config(
    page_title="DecideWise AI",
    layout="centered"
)

st.title("🧠 DecideWise")
st.caption("An Explainable AI Decision Assistant for Students & Professionals")

st.markdown(
    """
Enter your situation below.  
The AI agent will **analyze your decision logically** and give a **clear recommendation**.
"""
)

# -------------------------
# User Inputs
# -------------------------
background = st.text_area(
    "🎓 Your Background",
    placeholder="Final year CSE student with Python and ML basics"
)

goal = st.text_area(
    "🎯 Your Goal",
    placeholder="Get a stable job within 6 months"
)

option_a = st.text_area(
    "🅰️ Option A",
    placeholder="Prepare for campus placements"
)

option_b = st.text_area(
    "🅱️ Option B",
    placeholder="Prepare for GATE"
)

risk_tolerance = st.selectbox(
    "⚠️ Risk Tolerance",
    ["Low", "Medium", "High"]
)

st.divider()

# -------------------------
# Button Action
# -------------------------
if st.button("🔍 Analyze My Decision"):
    if not background or not goal or not option_a or not option_b:
        st.error("Please fill in all the fields.")
    else:
        with st.spinner("AI is analyzing your decision..."):
            try:
                response = requests.post(
                    "https://github.com/keerthiRA2211003011598/decidewise-ai",
                    json={
                        "background": background,
                        "goal": goal,
                        "option_a": option_a,
                        "option_b": option_b,
                        "risk_tolerance": risk_tolerance
                    },
                    timeout=60
                )

                if response.status_code == 200:
                    data = response.json()

                    st.success("✅ Decision Analysis Complete")

                    st.subheader("🔑 Key Factors")
                    for item in data["key_factors"]:
                        st.write("•", item)

                    st.subheader("🅰️ Option A Analysis")
                    for item in data["option_a_analysis"]:
                        st.write("•", item)

                    st.subheader("🅱️ Option B Analysis")
                    for item in data["option_b_analysis"]:
                        st.write("•", item)

                    st.subheader("⚠️ Risks")
                    for item in data["risks"]:
                        st.write("•", item)

                    st.subheader("✅ Final Recommendation")
                    st.write(data["final_recommendation"])

                    st.subheader("📊 Confidence Score")
                    st.progress(data["confidence_score"] / 100)

                else:
                    st.error("Backend error. Please try again.")

            except Exception as e:
                st.error("Could not connect to backend. Is it running?")
