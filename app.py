import streamlit as st

from pages.dashboard import show_dashboard
from pages.learning_path import show_learning_path
from pages.ai_tutor import show_ai_tutor
from pages.profile import show_profile

st.set_page_config(
    page_title="LENTERA BANGSA",
    page_icon="📚",
    layout="wide"
)

st.sidebar.title("📚 LENTERA BANGSA")

menu = st.sidebar.radio(
    "Navigation",
    ["Dashboard", "Learning Path", "AI Tutor", "Profile"]
)

if menu == "Dashboard":

    show_dashboard()

elif menu == "Learning Path":

    show_learning_path()

elif menu == "AI Tutor":

    show_ai_tutor()

elif menu == "Profile":

    show_profile()