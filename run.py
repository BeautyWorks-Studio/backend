from app import create_app
from app.config.mongodb import connect_db

app = create_app()

if __name__ == "__main__":
    app.run(port=5000, debug=True)
