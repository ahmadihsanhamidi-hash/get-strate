import streamlit as st

def show_dashboard():

    st.title("GET STRATE")

    st.subheader(
        "AI-Powered STEM Learning Platform"
    )

    st.write(
        "Platform pembelajaran STEM personal berbasis AI."
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("XP", "1250")
    col2.metric("Topics", "24")
    col3.metric("Quiz Average", "82%")

    st.markdown("## Continue Learning")

    st.info("Newton Laws - 68% completed")