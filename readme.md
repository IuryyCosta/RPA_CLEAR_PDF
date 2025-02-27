# RPA_CLEAR_PDF

## ✨ Descrição
O **RPA_CLEAR_PDF** é um projeto automatizado para processar arquivos PDF. Ele monitora a pasta `input_pdfs`, processa os arquivos e os move para `processed_pdfs`, garantindo que documentos já tratados não sejam reprocessados.

Com a implementação do `watcher.py`, o sistema monitora continuamente a pasta `input_pdfs` e executa `main.py` automaticamente ao detectar novos PDFs.

---

## 🔧 Funcionalidades
- ✅ **Processamento automático de PDFs**: Identifica e manipula arquivos PDF.
- ✅ **Monitoramento em tempo real**: O `watcher.py` observa a pasta `input_pdfs` e inicia o processamento automaticamente.
- ✅ **Evita reprocessamento**: Mantém um histórico para impedir que arquivos já tratados sejam processados novamente.
- ✅ **Execução contínua no servidor**: Pode ser configurado como serviço no **Windows** e **Linux**.

---

## 📝 Requisitos
- **Python 3.x**
- **Bibliotecas Python** (listadas em `requirements.txt`)

Instale o Python [aqui](https://www.python.org/downloads/) se ainda não tiver.

---

## 🔄 Instalação

### 1. **Clone o repositório**
```bash
git clone https://github.com/IuryyCosta/RPA_CLEAR_PDF.git
cd RPA_CLEAR_PDF
```

### 2. **Crie um ambiente virtual (opcional, mas recomendado)**
```bash
python -m venv venv
```
Ative o ambiente virtual:
- **Windows:** `venv\Scripts\activate`
- **Linux/macOS:** `source venv/bin/activate`

### 3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

---

## 🚀 Uso Manual (Sem Monitoramento)
Se quiser rodar manualmente, coloque os PDFs em `input_pdfs` e execute:
```bash
python main.py
```
Os arquivos processados serão movidos para `processed_pdfs`.

---

## ⌛ Monitoramento Automático com `watcher.py`
O `watcher.py` verifica a pasta `input_pdfs` e executa `main.py` automaticamente quando novos PDFs são adicionados.

### 🖥️ **Executando no Windows**

1. Inicie o monitoramento:
   ```bash
   python watcher.py
   ```
2. Para rodar automaticamente no Windows, use o **NSSM**:
   - Baixe o `nssm.exe` [aqui](https://nssm.cc/download).
   - Instale o serviço:
     ```bash
     nssm install RPA_CLEAR_PDF
     ```
   - Configure `Path` para `python.exe` e `Arguments` para `watcher.py`.
   - Clique em **Install service** e inicie com:
     ```bash
     nssm start RPA_CLEAR_PDF
     ```

### 🧑‍💻 **Executando no Linux**
1. Inicie o monitoramento manualmente:
   ```bash
   python watcher.py
   ```
2. Para rodar automaticamente, crie um serviço `systemd`:
   ```bash
   sudo nano /etc/systemd/system/rpa_clear_pdf.service
   ```
   Adicione:
   ```ini
   [Unit]
   Description=Monitoramento de PDFs
   After=network.target

   [Service]
   ExecStart=/usr/bin/python3 /caminho/do/projeto/watcher.py
   WorkingDirectory=/caminho/do/projeto
   Restart=always
   User=seu_usuario

   [Install]
   WantedBy=multi-user.target
   ```
3. Habilite e inicie:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl start rpa_clear_pdf
   sudo systemctl enable rpa_clear_pdf
   ```
4. Verifique o status:
   ```bash
   sudo systemctl status rpa_clear_pdf
   ```

---



---

Agora seu repositório está pronto para ser executado manualmente ou automaticamente como um serviço! 🚀