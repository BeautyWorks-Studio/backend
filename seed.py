<<<<<<< HEAD
from app import create_app, db, bcrypt
from app.models.user import User
from app.models.product import Product

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    user1 = User(
        name='Admin User',
        email='admin@example.com',
        password=bcrypt.generate_password_hash('adminpass').decode('utf-8'),
        role='admin'
    )
    user2 = User(
        name='Staff Member',
        email='staff@example.com',
        password=bcrypt.generate_password_hash('staffpass').decode('utf-8'),
        role='staff'
    )
    user3 = User(
        name='Regular User',
        email='user@example.com',
        password=bcrypt.generate_password_hash('userpass').decode('utf-8'),
        role='user'
    )

    product1 = Product(
        name='Luxury Car',
        description='A luxury vehicle with leather seats and high-end features.',
        price=75000.00,
        image_url='https://example.com/images/luxury-car.jpg'
    )
    product2 = Product(
        name='Sports Bike',
        description='A high-speed bike perfect for racing enthusiasts.',
        price=15000.00,
        image_url='https://example.com/images/sports-bike.jpg'
    )

    db.session.add_all([user1, user2, user3, product1, product2])
    db.session.commit()

    print("Database seeded successfully!")
    print(f"Users: {[user1.name, user2.name, user3.name]}")
    print(f"Products: {[product1.name, product2.name]}")
=======
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import create_app, db
from models.user import User
from models.service import Service
from models.employee import Employee
from models.tables import Table
from models.booking import Booking

app = create_app()
print("📦 Using DB:", app.config["SQLALCHEMY_DATABASE_URI"])

with app.app_context():
    db.drop_all()
    db.create_all()

    # Tjay's input or combined idea
    u1 = User(name='Sam Mbogo', email='sam@gmail.com', password_hash='hash', phone='12345678', address='Nairobi', country='KE')
    
    # Jesse's example entries
    s1 = Service(name='Pedicure', duration_minutes=60, price=2500)
    e1 = Employee(name='Maya', role='Beautician', email='maya@beauty.com', phone='0712345678')
    t1 = Table(name='Table 1', capacity=1)

    db.session.add_all([u1, s1, e1, t1])
    db.session.commit()

    print("✅ Seeded Successfully.")
>>>>>>> 62cc36b9109d9911316eda7ebfbc6407b76b1cd6
