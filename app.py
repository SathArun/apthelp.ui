import os
import streamlit as st
import requests

from dotenv import load_dotenv
load_dotenv()

# Read backend URL from env so containerized app can reach external backend service
BACKEND_URL = os.environ.get("BACKEND_URL", "http://127.0.0.1:8000/query")
BACKEND_URL = "https://apthelp-service-458515387636.asia-south2.run.app/query"

st.set_page_config(page_title="Tamil Nadu Bye-laws Q&A", layout="wide")
st.title("🏢 Tamil Nadu Apartment Bye-laws Q&A")

st.info(f"Using backend: {BACKEND_URL}")

query = st.text_area("Enter your question:", placeholder="e.g., What is the minimum parking requirement under TN Apartment Rules?")

if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Fetching answer..."):
            try:
                res = requests.post(BACKEND_URL, json={"question": query}, timeout=10)
                res.raise_for_status()
                data = res.json()
                st.subheader("Answer:")
                st.write(data.get("answer", "No answer found."))
            except requests.exceptions.RequestException as e:
                st.error(f"Request error when contacting backend ({BACKEND_URL}): {e}")
            except Exception as e:
                st.error(f"Unexpected error: {e}")
