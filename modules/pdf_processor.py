import pdfplumber
import re

def convert_pdf_to_md(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        md_content = ""
        for page in pdf.pages:
            text = page.extract_text()
            cleaned_text = clean_text(text)
            md_content += cleaned_text.replace('\n', '  \n') + '\n\n'
    return md_content

def clean_text(text):
    # Remove o sumário
    text = remove_toc(text)
    
    # Remove palavras específicas e caracteres especiais
    words_to_remove = ["palavra_especifica1", "palavra_especifica2"]  # Adicione as palavras a serem removidas
    chars_to_remove = [r"[^\w\s]", r"''", r'"', r"/", r"\|"]  # Remove caracteres especiais

    for word in words_to_remove:
        text = text.replace(word, "")

    for char in chars_to_remove:
        text = re.sub(char, "", text)

    return text

def remove_toc(text):
    # Remove o título "Sumário"
    text = re.sub(r'^Sumário\s*$', '', text, flags=re.M)

    # Regex para capturar as linhas do sumário
    # Essas linhas começam com números de seções e podem ter pontos ou sub-seções, seguidas do texto e o número de página no final
    text = re.sub(r'^\d+(\.\d+)*\s+[^0-9]+(\s+\d+)$', '', text, flags=re.M)
    # Remove numeração de páginas e o termo "Página X" no final das linhas
    text = re.sub(r'(?i)p[áa]gina \d+', '', text)  # Remove "Página X"
    return text