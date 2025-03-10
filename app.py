import streamlit as st
from Tabs import gene_variant, common_genes, home, about
from web_functions import get_common_genes, load_and_process_data
import pandas as pd

file_path = 'data/Database.xlsx'
df = load_and_process_data(file_path)

st.set_page_config(page_title="COVID Gene Database", page_icon="🧬", layout="wide")

st.markdown(
    """
    <style>
    /* Change the top bar background */
    header[data-testid="stHeader"] {
        background-color: #e6f2ff !important;
    }

    

    /* Remove the white gap below the top bar */
    header[data-testid="stHeader"] div {
        background-color: #e6f2ff !important;
    }

    /* Sidebar (Navigation Bar) Styling */
    [data-testid="stSidebar"] {
        background-color: #1179ae;
        padding: 20px;
    }

    /* Sidebar text (Ensuring all text is white) */
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Sidebar navigation links (unselected) */
    [data-testid="stSidebarNav"] a {
        color: white !important;
        font-size: 18px;
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
        transition: background-color 0.3s ease;
        text-decoration: none;
    }

    /* Hover effect */
    [data-testid="stSidebarNav"] a:hover {
        background-color: #357ABD;
    }

    /* Selected item in the sidebar */
    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background-color: #357ABD;
        color: white !important;
        font-weight: bold;
    }

    /* Background for the entire page */
    .main {
        background-color: #F0F2F6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Navigation Tabs
Tabs = {
    "Home": home.show_home, 
    "About":about.about_page, 
    "Gene Variant Selection": lambda: gene_variant.show_genes(df), 
    "Common Genes Selection": lambda: common_genes.show_common(df),
}

st.sidebar.title("Navigate")  
selected_tab = st.sidebar.radio("Select a Tab", list(Tabs.keys()))
Tabs[selected_tab]()
