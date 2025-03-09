import pandas as pd

def load_and_process_data(file_path):
    df = pd.read_excel(file_path, header=None)

    column_names = []
    for i in range(0, df.shape[1], 2):  
        variant_name = df.iloc[0, i]  
        column_names.append(f"{variant_name}_Up-regulated")
        column_names.append(f"{variant_name}_Down-regulated")

    df.columns = column_names

    df = df.drop(index=1)
    df = df.drop(index=0)
    df = df.reset_index(drop=True)

    return df

def get_common_genes(df, selected_variants, regulation_type):
    common_genes = None

    for variant in selected_variants:
        if regulation_type == "Up-regulated Genes":
            column_name = f"{variant}_Up-regulated"
        elif regulation_type == "Down-regulated Genes":
            column_name = f"{variant}_Down-regulated"
        else:
            raise ValueError(f"Invalid regulation_type: {regulation_type}")

        if column_name not in df.columns:
            raise ValueError(f"Column {column_name} not found in DataFrame.")

        genes = set(df[column_name].dropna())  

        if common_genes is None:
            common_genes = genes
        else:
            common_genes = common_genes.intersection(genes)

    if not common_genes:
        return "No common genes found"
    
    return common_genes
