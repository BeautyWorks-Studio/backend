from app import app, db
from app.models.user import User

with app.app_context():
    print("Seeding database...")

    User.query.delete()

    user1 = User(username='admin', email='admin@example.com', password='password123')
    user2 = User(username='tjay', email='tjay@example.com', password='secret456')

    db.session.add_all([user1, user2])
    db.session.commit()

    print("Database seeded successfully.")

