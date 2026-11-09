"""Public Streamlit asset-delivery diagnostic. No secrets, sports data, or API use."""
import streamlit as st

st.set_page_config(page_title="Streamlit Cloud Diagnostic", page_icon="🧪")
st.title("🧪 Streamlit Cloud Diagnostic")
st.success("The minimal app loaded.")
st.write("This public test has no NBA/NHL models, database, API keys, or secrets.")
st.code(f"Streamlit version: {st.__version__}")
st.caption("The private Sports Analytics app is not connected to this test.")

if st.button("Test browser interaction"):
    st.success("BUTTON TEST: PASS")

value = st.slider("Test slider", min_value=0, max_value=10, value=5)
st.write(f"Slider value: {value}")
