import streamlit as st
from web_functions import get_common_genes

def show_common(df):
    # Apply custom styles
    st.markdown(
        """
        <style>
        /* Background color */
        [data-testid="stAppViewContainer"] {
            background-color: #e6f2ff;
        }

        /* Centering and styling the multiselect box */
        div[data-baseweb="select"] {
            width: 60% !important;
            margin: auto;
            display: flex;
            justify-content: center;
        }

        div[data-baseweb="select"] * {
            color: #1F4E79 !important;
            font-weight: bold !important;
            font-size: 18px !important;
        }

        /* Force input text inside select box to be visible */
        div[data-baseweb="select"] input {
            color: #1F4E79 !important;
            font-weight: bold !important;
            font-size: 18px !important;
        }

        /* Styling dropdown options */
        ul[role="listbox"] {
            background-color: white !important;
            border: 2px solid #1F4E79 !important;
        }

        ul[role="listbox"] li {
            color: #1F4E79 !important;
            font-size: 18px !important;
            font-weight: bold !important;
        }

        /* Button styling */
        button[kind="primary"] {
            background-color: #1F4E79 !important;
            color: white !important;
            font-size: 18px !important;
            border-radius: 10px !important;
            padding: 10px 20px !important;
            font-weight: bold !important;
        }

        /* Styling text */
        .stText {
            font-size: 18px;
            font-weight: bold;
            color: #1F4E79;
        }

        /* Columns styling */
        .stColumn {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .text{
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Center-aligned label for multiselect
    st.markdown(
        "<h3 style='text-align: center; color: #1F4E79; font-weight: bold;'>Select Multiple Gene Variants</h3>",
        unsafe_allow_html=True
    )

    gene_variants = ['COVID000006', 'COVID000030', 'COVID000034', 'COVID000036', 'COVID000037', 
                     'COVID000043', 'COVID000047', 'COVID000049', 'COVID000050', 'COVID000057', 
                     'COVID000061', 'COVID000062', 'COVID000063', 'COVID000080', 'COVID000088', 
                     'COVID000090', 'COVID000094', 'COVID000095']
    
    selected_variants = st.multiselect("", gene_variants)  # Empty label so header appears separately

    if len(selected_variants) < 2:
        st.write('<p class="text">Please select at least two gene variants to find common genes.</p>', unsafe_allow_html=True)
        return  

    if selected_variants:
        common_upregulated = get_common_genes(df, selected_variants, 'Up-regulated Genes')
        common_downregulated = get_common_genes(df, selected_variants, 'Down-regulated Genes')

        col1, col2 = st.columns(2)

        with col1:
            #st.subheader('Common Up-regulated Genes')
            st.markdown("<h3 style='color: black;'>Common Up-regulated Genes</h3>", unsafe_allow_html=True)
            if isinstance(common_upregulated, set) and common_upregulated:
                num_genes = len(common_upregulated)
                st.markdown(f"<p style='font-size: 18px; color: #1F4E79; font-weight: bold;'>"
                            f"Number of Common Upregulated Genes found: {num_genes}<br>"
                            f"Common Upregulated Genes: {', '.join(list(common_upregulated))}</p>", 
                            unsafe_allow_html=True)
            else:
                #st.write("No common upregulated genes found.") 
                st.write('<p class="text">No common upregulated genes found.</p>', unsafe_allow_html=True)

        with col2:
            #st.subheader('Common Down-regulated Genes')
            st.markdown("<h3 style='color: black;'>Common Down-regulated Genes</h3>", unsafe_allow_html=True)
            if isinstance(common_downregulated, set) and common_downregulated:
                num_genes = len(common_downregulated)
                st.markdown(f"<p style='font-size: 18px; color: #1F4E79; font-weight: bold;'>"
                            f"Number of Common Downregulated Genes found: {num_genes}<br>"
                            f"Common Downregulated Genes: {', '.join(list(common_downregulated))}</p>", 
                            unsafe_allow_html=True)
            else:
                #st.write("No common downregulated genes found.") 
                st.write('<p class="text">No common downregulated genes found.</p>', unsafe_allow_html=True)
