import streamlit as st
import os

# Title
st.set_page_config(page_title="CR Study App - Heart", layout="wide")
st.title("🫀 Cardiorespiratory Study App")
st.subheader("Focus: Heart")

# Sidebar navigation
st.sidebar.title("📚 Topics")
topics = ["Heart"]  # Add more later
selected_topic = st.sidebar.radio("Select a topic:", topics)

# Display Markdown notes
notes_dir = "notes"
note_file = os.path.join(notes_dir, f"{selected_topic.lower()}.md")

if os.path.exists(note_file):
    with open(note_file, "r", encoding="utf-8") as f:
        content = f.read()
        st.markdown(content, unsafe_allow_html=True)
else:
    st.warning(f"No notes found for {selected_topic}.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by CxunChuah for CR revision.")
