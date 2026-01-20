import streamlit as st
import requests

# Page config
st.set_page_config(page_title="DecideWise AI", page_icon="🧠")

st.title("🧠 DecideWise AI")
st.write("AI-powered decision analysis using a Generative AI agent")

# 🔴 CHANGE THIS ONLY
BACKEND_URL = "https://pacific-cooperation-production.up.railway.app"
# 🔴 If your Railway domain is different, replace ONLY the domain part

# Input form
with st.form("decision_form"):
    background = st.text_area("Your Background", placeholder="e.g. Final year CSE student")
    goal = st.text_input("Your Goal", placeholder="e.g. Get placed in a good company")
    option_a = st.text_area("Option A", placeholder="e.g. Join a startup")
    option_b = st.text_area("Option B", placeholder="e.g. Prepare for MNC")
    risk_tolerance = st.selectbox("Risk Tolerance", ["low", "medium", "high"])

    submit = st.form_submit_button("Analyze My Decision")

# On submit
if submit:
    if not all([background, goal, option_a, option_b]):
        st.error("❌ Please fill all the fields")
    else:
        with st.spinner("🧠 Analyzing your decision..."):
            try:
                payload = {
                    "background": background,
                    "goal": goal,
                    "option_a": option_a,
                    "option_b": option_b,
                    "risk_tolerance": risk_tolerance
                }

                response = requests.post(
                    BACKEND_URL,
                    json=payload,
                    timeout=60
                )

                if response.status_code == 200:
                    st.success("✅ Analysis Complete")
                    st.json(response.json())
                else:
                    st.error(f"❌ Error {response.status_code}")
                    st.text(response.text)

            except Exception as e:
                st.error("❌ Backend not reachable")
                st.text(str(e))

