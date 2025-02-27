
from modules.pdf_converter import process_pdfs
from modules.file_manager import create_directories

def main():
    input_folder = 'input_pdfs'# Pasta onde os PDFs de entrada estão localizados
    processed_folder = 'processed_pdfs' # Pasta onde os PDFs processados serão movidos
    output_folder = 'generated_md'# Pasta onde os arquivos Markdown gerados serão salvos

    # Verifica e cria as pastas necessárias
    create_directories([input_folder, processed_folder, output_folder])

    # Processa os PDFs
    process_pdfs(input_folder, processed_folder, output_folder)

if __name__ == "__main__":
    main()
