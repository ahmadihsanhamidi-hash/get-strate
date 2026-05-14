import streamlit as st

def show_dashboard():

    st.title("📚 LENTERA BANGSA")

    st.subheader(
        "Platform Pembelajaran Nusantara Knowledge Digital Hub"
    )

    st.write(
        "LENTERA BANGSA adalah platform pembelajaran digital berbasis teknologi dan AI yang mendukung akses pengetahuan Nusantara secara modern, interaktif, dan inklusif."
    )

    st.markdown("---")

    st.markdown(
        """
        ### 🌏 Visi Platform

        Menjadi pusat pembelajaran digital Nusantara yang mengintegrasikan teknologi, AI, literasi sains, budaya, dan pendidikan modern dalam satu ekosistem terpadu.
        """
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("XP", "1250")
    col2.metric("Topics", "24")
    col3.metric("Quiz Average", "82%")

    st.markdown("## Continue Learning")

    st.info("Literasi Digital Nusantara - 68% completed")