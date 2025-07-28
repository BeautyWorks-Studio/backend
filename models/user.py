from app import db  # or from app.extensions import db, depending on your structure

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    # ... other fields ...
