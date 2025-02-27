# RPA_CLEAR_PDF

## Descrição

O **RPA_CLEAR_PDF** é um projeto desenvolvido para automatizar o processamento de arquivos PDF. Ele lê documentos na pasta `input_pdfs`, realiza operações específicas (como extração de texto ou dados) e move os arquivos processados para a pasta `processed_pdfs`. Além disso, o sistema evita o reprocessamento de arquivos já tratados, garantindo eficiência e precisão no fluxo de trabalho.

## Funcionalidades

- **Processamento Automático de PDFs**: Leitura e manipulação de arquivos PDF de forma automatizada.
- **Movimentação de Arquivos**: Após o processamento, os PDFs são movidos para a pasta `processed_pdfs`.
- **Controle de Arquivos Processados**: O sistema mantém um registro dos arquivos já processados para evitar reprocessamentos.

## Requisitos

Antes de executar o projeto, certifique-se de que seu ambiente atende aos seguintes requisitos:

- **Python 3.x**: Linguagem de programação utilizada no desenvolvimento do projeto.
- **Bibliotecas Python**: As dependências necessárias estão listadas no arquivo `requirements.txt`.

## Instalação

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local:

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/IuryyCosta/RPA_CLEAR_PDF.git
   ```

2. **Navegue até o diretório do projeto**:

   ```bash
   cd RPA_CLEAR_PDF
   ```

3. **Crie um ambiente virtual (opcional, mas recomendado)**:

   ```bash
   python -m venv venv
   ```

   Ative o ambiente virtual:

   - No Windows:

     ```bash
     venv\Scripts\activate
     ```

   - No macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para iniciar o processamento dos arquivos PDF:

1. Coloque os arquivos PDF que deseja processar na pasta `input_pdfs`.
2. Execute o script principal:

   ```bash
   python main.py
   ```

   O script processará os arquivos e moverá aqueles já tratados para a pasta `processed_pdfs`.
