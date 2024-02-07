import tabula
import pandas as pd

def extract_tables_from_pdf(pdf_path):
    all_dataframes = []
    for page_number in range(1, len(tabula.read_pdf(pdf_path, pages="all")) + 1):
        tables = tabula.read_pdf(pdf_path, pages=page_number, multiple_tables=True)
        for table in tables:
            dataframe = pd.DataFrame(table)
            all_dataframes.append(dataframe)
    return all_dataframes
pdf_path = "caminho_para_seu_arquivo.pdf"
all_dataframes = extract_tables_from_pdf(pdf_path)
with open("tabelas_extraidas.csv", "w", encoding="utf-8") as f:
    for dataframe in all_dataframes:
        dataframe.to_csv(f, index=False)
