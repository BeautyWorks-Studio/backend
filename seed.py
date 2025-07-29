from app import create_app, db, bcrypt
from app.models.user import User
from app.models.product import Product
from app.models.service import Service
from app.models.employee import Employee
from app.models.tables import Table
from app.models.booking import Booking

app = create_app()
print("�� Using DB:", app.config["SQLALCHEMY_DATABASE_URI"])

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
    user4 = User(
        name='Sam Mbogo',
        email='sam@gmail.com',
        password=bcrypt.generate_password_hash('sam123').decode('utf-8'),
        role='user',
        phone='12345678',
        address='Nairobi',
        country='KE'
    )

    product1 = Product(
        name='Makeup',
        description='Glowing skin.',
        price=75000.00,
        
    )
    product2 = Product(
        name='Garnier',
        description='Removes acne.',
        price=15000.00,
       
    )

    service1 = Service(name='Pedicure', duration_minutes=60, price=2500)

    employee1 = Employee(name='Maya', role='Beautician', email='maya@beauty.com', phone='0712345678')

    table1 = Table(name='Table 1', capacity=1)

    db.session.add_all([user1, user2, user3, user4, product1, product2, service1, employee1, table1])
    db.session.commit()

    print("Database seeded successfully!")
    print(f"Users: {[user1.name, user2.name, user3.name, user4.name]}")
    print(f"Products: {[product1.name, product2.name]}")
    print(f"Services: {[service1.name]}")
    print(f"Employees: {[employee1.name]}")
    print(f"Tables: {[table1.name]}")

