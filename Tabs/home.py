import streamlit as st

def show_home():
    # Custom styling with background color
    st.markdown(
        """
        <style>
        [data-testid="stAppViewContainer"] {
            background-color: #e6f2ff;
        }
        .title {
            font-size: 80px !important;
            font-weight: bold;
            text-align: center;
            color: #2E3B55;
            margin-bottom: 10px;
            line-height: 90px; /* Adjust spacing */
            text-shadow: 2px 2px 5px rgba(0,0,0,0.2); /* Adds shadow */
        }
        .tagline {
            font-size: 30px !important;
            font-weight: bold;
            text-align: center;
            color: #1F4E79;
            margin-bottom: 40px;
        }
        .subtitle {
            font-size: 30px !important;
            font-weight: bold;
            color: #1F4E79;
        }
        .text {
            font-size: 18px;
            color: #333333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Big Title (Centered)
    st.markdown('<p class="title">COVID Gene Database</p>', unsafe_allow_html=True)
    # Tagline Below Title
    st.markdown('<p class="tagline">Tracking COVID-19 gene variants</p>', unsafe_allow_html=True)

    # Row 1: Image on Left | Text on Right
    col1, col2 = st.columns([1.5, 2])

    with col1:
        st.image("images//th.jpg", caption="Cut away model of COVID-19", use_container_width=True)

    with col2:
        st.markdown('<p class="subtitle">📌 What is This?</p>', unsafe_allow_html=True)
        st.markdown('<p class="text">The COVID Gene Database is an interactive platform that helps researchers, scientists, and healthcare professionals explore gene expression changes in different COVID-19 variants. The database provides information on up-regulated and down-regulated genes for selected variants, helping identify common genetic patterns.</p>', unsafe_allow_html=True)

    # Row 2: Text on Left | Image on Right
    col3, col4 = st.columns([2, 1.5])

    with col3:
        st.markdown('<p class="subtitle">🔍 How Does It Work?</p>', unsafe_allow_html=True)
    
        st.markdown("""
    <style>
        .black-text ul {
            color: black;
        }
        .black-text li {
            color: black;
            font-size: 16px; /* Adjust size if needed */
        }
    </style>
    <div class="black-text">
        <ul>
            <li><b>Select a COVID-19 variant</b> to view its associated <b>up-regulated</b> (activated) and <b>down-regulated</b> (suppressed) genes.</li>
            <li><b>Compare multiple variants</b> to find <b>common genes</b>, which may help in understanding shared biological mechanisms and potential therapeutic targets.</li>
            <li>The data is sourced from <b>genetic studies and analyses</b> to provide insights into how COVID-19 affects gene expression in different variants.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


    with col4:
        st.image("images//th1.png", caption="DNA strand", use_container_width=True)

    # Row 3: Image on Left | Text on Right
    col5, col6 = st.columns([1.5, 2])

    with col5:
        st.image("images//th2.jpg", caption="Gene expression", use_container_width=True)

    with col6:
        st.markdown('<p class="subtitle">🌟 Why is This Important?</p>', unsafe_allow_html=True)
        st.markdown("""
    <style>
    .text {
        color: black !important;
        font-size: 16px;
    }
    </style>
    <div class="text">
    <ul>
        <li>Helps in identifying <b>biomarkers</b> for disease severity and progression.</li>
        <li>Aids in <b>drug discovery</b> by targeting common gene expressions across variants.</li>
        <li>Supports scientific research on the genetic response to COVID-19.</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)





