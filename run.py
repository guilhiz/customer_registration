import uvicorn
from src.main import app  # Importe diretamente do módulo main

host = "0.0.0.0"
port = 8002

if __name__ == '__main__':
    uvicorn.run(app, host=host, port=port)