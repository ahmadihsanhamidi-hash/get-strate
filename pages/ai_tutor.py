import streamlit as st


def show_ai_tutor():

    st.title("🤖 AI Tutor Nusantara")

    st.subheader(
        "Verifikasi Informasi, Literasi Digital, dan Pembelajaran Kearifan Lokal"
    )

    st.write(
        "AI Tutor membantu pengguna melakukan verifikasi informasi, menemukan sumber belajar terpercaya, serta mengeksplorasi pengetahuan Nusantara secara digital."
    )

    st.markdown("---")

    fitur = st.selectbox(
        "Pilih fitur AI Tutor",
        [
            "Verifikasi Hoaks",
            "Sumber Primer",
            "Artikel & Ebook",
            "Kajian Pembelajaran",
            "Video Pembelajaran",
            "Kearifan Lokal"
        ]
    )

    pertanyaan = st.text_input(
        "Masukkan pertanyaan atau topik"
    )

    st.markdown("---")

    # VERIFIKASI HOAKS
    if fitur == "Verifikasi Hoaks":

        st.info(
            "Fitur ini membantu pengguna mengecek validitas informasi dan membandingkan dengan sumber terpercaya."
        )

        if pertanyaan:

            st.success("Hasil Verifikasi")

            st.write(
                "Informasi perlu dibandingkan dengan sumber resmi seperti kementerian, jurnal ilmiah, media kredibel, dan lembaga pemeriksa fakta."
            )

            st.markdown("### Langkah Verifikasi")

            st.write("- Periksa tanggal publikasi")
            st.write("- Cek sumber asli berita")
            st.write("- Bandingkan dengan media terpercaya")
            st.write("- Hindari judul provokatif")
            st.write("- Pastikan ada data dan referensi")

    # SUMBER PRIMER
    elif fitur == "Sumber Primer":

        st.info(
            "Membantu menemukan sumber primer akademik dan referensi terpercaya."
        )

        if pertanyaan:

            st.success("Rekomendasi Sumber")

            st.write("Berikut jenis sumber primer yang disarankan:")

            st.write("- Artikel jurnal ilmiah")
            st.write("- Buku akademik")
            st.write("- Prosiding konferensi")
            st.write("- Data resmi pemerintah")
            st.write("- Arsip budaya dan sejarah")

    # ARTIKEL & EBOOK
    elif fitur == "Artikel & Ebook":

        st.info(
            "Rekomendasi bahan bacaan digital untuk pembelajaran mandiri."
        )

        if pertanyaan:

            st.success("Rekomendasi Bacaan")

            st.write(
                "Topik yang dicari dapat dipelajari melalui ebook pendidikan, jurnal open access, dan artikel ilmiah populer."
            )

            st.write("Contoh sumber:")
            st.write("- Google Scholar")
            st.write("- DOAJ")
            st.write("- Perpusnas Digital")
            st.write("- Garuda Kemdikbud")

    # KAJIAN PEMBELAJARAN
    elif fitur == "Kajian Pembelajaran":

        st.info(
            "Menyediakan penjelasan konsep dan kajian edukatif."
        )

        if pertanyaan:

            st.success("Kajian Singkat")

            st.write(
                "Topik pembelajaran dapat dianalisis dari aspek konsep, penerapan, dan relevansi dalam kehidupan sehari-hari."
            )

    # VIDEO PEMBELAJARAN
    elif fitur == "Video Pembelajaran":

        st.info(
            "Rekomendasi video edukatif dan media pembelajaran interaktif."
        )

        if pertanyaan:

            st.success("Saran Video")

            st.write(
                "Cari video pembelajaran dari kanal edukasi terpercaya dan universitas resmi."
            )

            st.write("Contoh platform:")
            st.write("- YouTube Edu")
            st.write("- Rumah Belajar")
            st.write("- Coursera")
            st.write("- Khan Academy")

    # KEARIFAN LOKAL
    elif fitur == "Kearifan Lokal":

        st.info(
            "Eksplorasi budaya dan pengetahuan lokal Nusantara secara digital."
        )

        if pertanyaan:

            st.success("Kajian Kearifan Lokal")

            st.write(
                "Kearifan lokal dapat dikaji dari aspek budaya, lingkungan, pendidikan, sains tradisional, dan nilai sosial masyarakat."
            )

            st.markdown("### Contoh Topik")

            st.write("- Arsitektur rumah adat")
            st.write("- Sistem pertanian tradisional")
            st.write("- Pengobatan tradisional")
            st.write("- Permainan tradisional")
            st.write("- Astronomi lokal Nusantara")