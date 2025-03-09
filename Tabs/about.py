import streamlit as st

def about_page():
    # Apply custom styles
    st.markdown(
        """
        <style>
        /* Background color */
        [data-testid="stAppViewContainer"] {
            background-color: #e6f2ff;
        }

        /* Header styling */
        h1, h2 {
            text-align: center;
            color: #1F4E79;
            font-weight: bold;
        }

        /* Styled text container */
        .stText {
            font-size: 18px;
            font-weight: bold;
            color: #1F4E79;
            text-align: center;
        }

        /* Box styling */
        .info-box {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin: auto;
            width: 70%;
            text-align: center;
            font-size: 18px;
        }

        /* Columns styling */
        .stColumn {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Page Title
    st.markdown("<h1>About This Project</h1>", unsafe_allow_html=True)

    # Side-by-side layout for sections
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<h2>Data Collection</h2>", unsafe_allow_html=True)
        st.markdown(
    "<div class='info-box'>"
    "<p>The dataset used in this project was collected by:<br>"
    "<b>Computational Genomics Center of Excellence,</b><br>"
    "<b>Department of Biotechnology,</b><br>"
    "<b>RV College of Engineering.</b><br><br>"
    "The data was gathered from reliable sources and curated for accuracy.</p>"
    "</div>",
    unsafe_allow_html=True
)



    with col2:
        st.markdown("<h2>Webpage Development</h2>", unsafe_allow_html=True)
        st.markdown(
    "<div class='info-box'>"
    "<p>This webpage was designed and developed by:<br>"
    "<b>Nikita S Raj Kapini,</b><br>"
    "<b>4th Sem, Department of Computer Science,</b><br>"
    "<b>RV College of Engineering.</b><br><br>"
    "It provides an interactive interface for analyzing gene variant relationships.</p>"
    "</div>",
    unsafe_allow_html=True
)


    # Footer
    st.markdown(
        "<p style='text-align: center; font-size: 16px; color: #1F4E79;'>"
        "For any queries, please contact: <b>nikitasrajk.cs23@rvce.edu.in</b></p>",
        unsafe_allow_html=True
    )
