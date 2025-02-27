import os
import shutil

def get_pdf_files(folder_path):
    # Retorna uma lista de caminhos completos dos arquivos PDF na pasta especificada
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]

def move_file(file_path, destination_folder):
    # Verifica se a pasta de destino existe, e se não existir, cria a pasta
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    # Move o arquivo para a pasta de destino
    shutil.move(file_path, destination_folder)

def save_markdown_file(md_content, output_folder, pdf_file):
    # Verifica se a pasta de saída existe, e se não existir, cria a pasta
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Gera o nome do arquivo Markdown com base no nome do arquivo PDF
    md_filename = os.path.basename(pdf_file).replace('.pdf', '.md')
    md_filepath = os.path.join(output_folder, md_filename)
    # Salva o conteúdo Markdown no arquivo
    with open(md_filepath, 'w', encoding='utf-8') as md_file:
        md_file.write(md_content)

def create_directories(folders):
    # Verifica e cria pastas necessárias se não existirem
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
