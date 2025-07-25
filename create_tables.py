from app import create_app, db
import models  

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ All tables created successfully.")