import time
import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class PDFHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        if event.src_path.endswith('.pdf'):
            print(f'Novo arquivo detectado: {event.src_path}')
            executar_main()

def executar_main():
    print("Executando main.py para processar PDFs...")
    subprocess.run(["python", "main.py"])  # Chama o script principal do projeto

def start_watching():
    input_folder = "input_pdfs"
    os.makedirs(input_folder, exist_ok=True)

    event_handler = PDFHandler()
    observer = Observer()
    observer.schedule(event_handler, input_folder, recursive=False)
    observer.start()

    print("Monitorando a pasta input_pdfs... Pressione Ctrl+C para sair.")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watching()
