from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
#from app import db, bcrypt

def create_user(username, password):
    hashed_pw = generate_password_hash(plain_password)
    user = User(username=username, password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return user
    return None
