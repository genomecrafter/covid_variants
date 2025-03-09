import streamlit as st

def show_genes(df):
    # Apply custom styles
    st.markdown(
        """
        <style>
        /* Background color */
        
        [data-testid="stAppViewContainer"] {
            background-color: #e6f2ff;
        }

        /* Centering and styling the select box */
div[data-baseweb="select"] {
    width: 60% !important;  /* Adjust width */
    margin: auto; /* Center the select box */
    display: flex;
    justify-content: center;
}

div[data-baseweb="select"] * {
    color: #1F4E79 !important; /* Blue text */
    font-weight: bold !important;
    font-size: 18px !important;
}

/* Force input text inside select box to be visible */
div[data-baseweb="select"] input {
    color: #1F4E79 !important; /* Dark blue text */
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
        </style>
        """,
        unsafe_allow_html=True
    )

    variant_names = df.columns.str.extract(r'(.*)_Up-regulated')[0].dropna().unique()
    
    # Center-aligned label for select box
    st.markdown(
    "<h3 style='text-align: center; color: #1F4E79; font-weight: bold;'>Select a Gene Variant</h3>",
    unsafe_allow_html=True
)

# Centering the select box
    selected_variant = st.selectbox("", variant_names)  # Empty label so only styled header appears

    
    upregulated_genes = df[selected_variant + "_Up-regulated"].dropna().tolist()
    downregulated_genes = df[selected_variant + "_Down-regulated"].dropna().tolist()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f"Up-regulated genes for {selected_variant}:")
        st.write(upregulated_genes)
    
    with col2:
        st.subheader(f"Down-regulated genes for {selected_variant}:")
        st.write(downregulated_genes)
