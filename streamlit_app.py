import os
import time
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000/agent"

st.set_page_config(
    page_title="AI Business Proposal Generator",
    page_icon="🤖",
    layout="wide",
)

# ---------------- Header ---------------- #

st.title("🤖 AI Business Proposal Generator")
st.caption(
    "FastAPI • LangGraph • OpenAI • Streamlit"
)

# ---------------- Sidebar ---------------- #

with st.sidebar:
    st.header("Project Information")

    st.markdown("""
**Tech Stack**

- FastAPI
- LangGraph
- OpenAI
- Streamlit
- Python-docx

---

**Workflow**

User Request

⬇

Planner

⬇

Executor

⬇

DOCX Generator

⬇

API Response

---

**Engineering Improvement**

✅ Multi-Step Planning
""")

# ---------------- Main ---------------- #

examples = [
    "Create a proposal for an AI Resume Screening System.",
    "Create a proposal for an AI Hospital Management System.",
    "Create a proposal for an AI Customer Support Chatbot.",
    "Create a proposal for an AI Inventory Management System.",
]

selected = st.selectbox(
    "Example Prompts",
    ["Custom"] + examples,
)

if selected != "Custom":
    default_text = selected
else:
    default_text = ""

request = st.text_area(
    "Business Request",
    value=default_text,
    height=180,
)

generate = st.button(
    "🚀 Generate Proposal",
    use_container_width=True,
)

# ---------------- Generate ---------------- #

if generate:

    if not request.strip():
        st.warning("Please enter a request.")
        st.stop()

    start = time.time()

    with st.status("Generating Proposal...", expanded=True) as status:

        st.write("📌 Sending request to FastAPI...")
        time.sleep(0.5)

        try:

            response = requests.post(
                API_URL,
                json={"request": request},
                timeout=300,
            )

            response.raise_for_status()

        except Exception as e:

            status.update(
                label="Failed",
                state="error",
            )

            st.error(str(e))
            st.stop()

        data = response.json()

        st.write("📝 Planning completed")
        st.write("🤖 Proposal generated")
        st.write("📄 Word document created")

        status.update(
            label="Completed",
            state="complete",
        )

    elapsed = round(time.time() - start, 2)

    # ---------------- Metrics ---------------- #

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Tasks", len(data["tasks"]))

    c2.metric(
        "Words",
        len(data["proposal"].split())
    )

    c3.metric(
        "Time",
        f"{elapsed}s"
    )

    c4.metric(
        "Model",
        "GPT-4.1 Mini"
    )

    # ---------------- Tasks ---------------- #

    with st.expander("📋 Generated Task List", expanded=True):

        for i, task in enumerate(data["tasks"], 1):
            st.write(f"{i}. {task}")

    # ---------------- Proposal ---------------- #

    with st.expander("📄 Proposal Preview", expanded=True):

        st.markdown(data["proposal"])

    # ---------------- Download ---------------- #

    st.subheader("📁 Generated Document")

    document_path = data["document"]

    if os.path.exists(document_path):

        with open(document_path, "rb") as f:

            st.download_button(
                "⬇ Download Proposal (.docx)",
                f,
                file_name=os.path.basename(document_path),
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True,
            )

    else:

        st.warning(
            f"Document not found:\n{document_path}"
        )

    # ---------------- Raw Response ---------------- #

    with st.expander("🔍 API Response"):

        st.json(data)

st.divider()

st.caption(
    "Built using FastAPI, LangGraph, OpenAI and Streamlit"
)