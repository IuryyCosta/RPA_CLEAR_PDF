from modules.pdf_processor import convert_pdf_to_md
from modules.file_manager import (
    get_pdf_files,
    move_file,
    save_markdown_file
)

def process_pdfs(input_folder, processed_folder, output_folder):
    pdf_files = get_pdf_files(input_folder)  # Pega a lista de arquivos PDF na pasta 
    

    for pdf_file in pdf_files:  # Itera sobre cada arquivo PDF
        md_content = convert_pdf_to_md(pdf_file)  # Converte o PDF para Markdown
        save_markdown_file(md_content, output_folder, pdf_file)  # Salva o arquivo Markdown gerado
        move_file(pdf_file, processed_folder)  # Move o PDF processado para a pasta de PDFs processados
        
