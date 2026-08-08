import os
import tempfile
import streamlit as st

from ingest import ingest_pdf
from rag import retrieve_documents
from llm import generate_answer

# ----------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------

st.set_page_config(
    page_title="AI PDF Assistant",
    page_icon="📘",
    layout="wide",
)

# ----------------------------------------------------
# CSS
# ----------------------------------------------------

st.markdown("""
<style>

.main{
    background:#f5f7fb;
}

.block-container{
    max-width:1100px;
    padding-top:2rem;
    padding-bottom:3rem;
}

h1{
    color:#1f2937;
}

.stButton>button{
    width:100%;
    height:52px;
    font-size:18px;
    font-weight:600;
    border-radius:10px;
}

.stFileUploader{
    font-size:18px;
}

.stTextInput input{
    height:55px;
    font-size:18px;
}

.answer-card{
    background:white;
    padding:25px;
    border-radius:12px;
    border-left:8px solid #2563eb;
    box-shadow:0px 4px 12px rgba(0,0,0,.08);
    font-size:18px;
    line-height:1.8;
    margin-bottom:20px;
}

.citation-card{
    background:white;
    padding:20px;
    border-radius:12px;
    box-shadow:0px 4px 12px rgba(0,0,0,.08);
    margin-bottom:18px;
}

.footer{
    text-align:center;
    color:gray;
    padding-top:40px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------
# HEADER
# ----------------------------------------------------

st.title("📘 AI PDF Question Answering System")

st.write(
    "Upload one or more PDF documents, index them into Qdrant, and ask questions using your AI-powered RAG assistant."
)

st.divider()

# ----------------------------------------------------
# PDF UPLOAD
# ----------------------------------------------------

st.subheader("📂 Upload PDF Documents")

uploaded_files = st.file_uploader(
    "",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    col1, col2 = st.columns([4,1])

    with col2:

        if st.button("📥 Index PDFs", use_container_width=True):

            progress = st.progress(0)

            status = st.empty()

            total = len(uploaded_files)

            for i, uploaded_file in enumerate(uploaded_files):

                status.info(f"Indexing **{uploaded_file.name}**")

                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as tmp:

                    tmp.write(uploaded_file.getvalue())

                    temp_path = tmp.name

                ingest_pdf(
                    temp_path,
                    uploaded_file.name
                )

    

                os.remove(temp_path)

                progress.progress((i+1)/total)

            status.success("✅ PDFs Indexed Successfully!")

st.divider()

# ----------------------------------------------------
# QUESTION
# ----------------------------------------------------

st.subheader("💬 Ask a Question")

with st.form("question_form", clear_on_submit=False):

    question = st.text_input(
        "",
        placeholder="Example: What is personal liberty under Article 21?"
    )

    submitted = st.form_submit_button(
        "🔍 Get Answer",
        use_container_width=True
    )

# ----------------------------------------------------
# ANSWER
# ----------------------------------------------------

if submitted:

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching relevant documents..."):

            docs = retrieve_documents(question)

            answer, citations = generate_answer(
                question,
                docs
            )

        # ---------------- Answer ----------------

        st.markdown("## ✅ Answer")

        st.markdown(
            f"""
<div class="answer-card">
{answer}
</div>
""",
            unsafe_allow_html=True,
        )

           # ---------------- Citations ----------------

    st.markdown("## 📚 Citations")

    if len(citations) == 0:

        st.info("No citations found.")

    else:

        for i, c in enumerate(citations, start=1):

            with st.expander(f"📄 Citation {i}", expanded=(i == 1)):

                st.markdown(
                    f"""
<div style="font-size:15px; line-height:1.5">

<b>Source:</b> {c['source']}<br>

<b>Page:</b> {c['page']}<br><br>

<b>Retrieved Text:</b>

<div style="
background:#f5f5f5;
padding:12px;
border-radius:8px;
margin-top:8px;
border-left:4px solid #2563eb;
font-size:14px;
white-space:pre-wrap;
">

{c['text']}

</div>

</div>
                    """,
                    unsafe_allow_html=True,
                )

# ----------------------------------------------------
# FOOTER
# ----------------------------------------------------

st.markdown(
    """
<div class="footer">
Built with ❤️ using Streamlit • Qdrant • HuggingFace • OpenRouter
</div>
""",
    unsafe_allow_html=True,
)