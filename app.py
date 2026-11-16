import streamlit as st
import os
from google.colab import userdata
from copilot_engine import generate_telco_qa_artifacts

if "GEMINI_API_KEY" not in os.environ:
    try:
        os.environ["GEMINI_API_KEY"] = userdata.get('GEMINI_API_KEY')
    except Exception:
        pass

st.set_page_config(page_title="TelcoQA Copilot", layout="wide")

st.title("📡 TelcoQA Copilot")
st.markdown("### Autonomous AI Assistant for Telco Test Generation & Gap Analysis")

feature_input = st.text_area(
    "Enter Feature Description:",
    value="When an enterprise client triggers an outbound bulk SMS campaign, the gateway routes messages via primary SMPP connections. If a delivery receipt (DLR) status DELIVRD is not received within 15 seconds, the system triggers an automatic fallback retry through a secondary route. If both routes fail or return EXPIRED/UNDELIV, the transaction logs an error event, updates the dashboard status to Failed, and raises a billing credit exception.",
    height=130
)

if st.button("Generate QA Artifacts", type="primary"):
    if not os.environ.get("GEMINI_API_KEY"):
        st.error("GEMINI_API_KEY not found! Please add it in Colab Secrets (Key icon on the left) and enable Notebook access.")
    else:
        with st.spinner("AI Agent is synthesizing Gherkin, Playwright script, and coverage gap report..."):
            try:
                artifacts = generate_telco_qa_artifacts(feature_input)
                st.success("Artifacts Generated Successfully!")
                
                tab1, tab2, tab3 = st.tabs(["🥒 Gherkin BDD", "🎭 Playwright Script", "📊 Coverage-Gap Report"])
                
                with tab1:
                    st.code(artifacts["gherkin"], language="gherkin")
                    st.download_button("Download .feature", artifacts["gherkin"], file_name="sms_delivery.feature")
                    
                with tab2:
                    st.code(artifacts["playwright_script"], language="python")
                    st.download_button("Download Test Script", artifacts["playwright_script"], file_name="test_sms_delivery.py")
                    
                with tab3:
                    st.markdown(artifacts["coverage_report"])
                    st.download_button("Download Report", artifacts["coverage_report"], file_name="coverage_gap.md")
                    
            except Exception as e:
                st.error(f"Generation failed: {e}")
