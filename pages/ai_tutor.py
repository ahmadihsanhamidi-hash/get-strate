import streamlit as st

def show_ai_tutor():

    st.title("AI Tutor")

    question = st.text_input(
        "Ask anything about STEM"
    )

    if question:

        st.write("### AI Response")

        st.write(
            "Newton's Second Law states that force equals mass times acceleration."
        )