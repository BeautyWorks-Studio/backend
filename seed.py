from datetime import datetime
from mongoengine import connect
from app.models.product import Product
from app.models.service import Service
from app.models.employee import Employee
from app.models.user import User


connect(db="e-commerce", host="mongodb://localhost:27017/e-commerce")


def seed_products():
    Product.drop_collection()

    products = [
        Product(
            name="Lavender Body Lotion",
            description="A soothing body lotion with lavender scent",
            price=12.99,
            image_urls=[
                "https://example.com/lavender1.jpg",
                "https://example.com/lavender2.jpg"
            ],
            category="Skincare",
            sub_category="Body",
            sizes=["S", "M", "L"],
            bestseller=True,
            date=datetime.now()

        ),
        Product(
            name="Hair Growth Serum",
            description="Stimulates hair growth naturally",
            price=18.50,
            image_urls=["https://example.com/serum.jpg"],
            category="Haircare",
            sub_category="Treatment",
            sizes=["100ml"],
            bestseller=False,
            date=datetime.now()

        )
    ]

    for product in products:
        product.save()

    print("✅ Products seeded.")


def seed_services():
    Service.drop_collection()

    services = [
        Service(
            name="Full Body Massage",
            description="60-minute relaxing massage",
            price=45.00,
            duration=60
        ),
        Service(
            name="Manicure & Pedicure",
            description="Nail grooming and polishing",
            price=30.00,
            duration=45
        )
    ]

    for service in services:
        service.save()

    print("✅ Services seeded.")


def seed_employees():
    Employee.drop_collection()

    employees = [
        Employee(
            name="Tjay",
            role="Therapist",
            email="tjay@example.com",
            phone="0712345678"
        ),
        Employee(
            name="Sam",
            role="Nail Technician",
            email="sam@example.com",
            phone="0798765432"
        )
    ]

    for employee in employees:
        employee.save()

    print("✅ Employees seeded.")


def seed_users():
    User.drop_collection()

    user = User(
        name="Jesse",
        email="jesse@example.com",
        password="hashedpassword",  
        cart_data={}
    )
    user.save()

    print("✅ User seeded.")


if __name__ == "__main__":
    seed_products()
    seed_services()
    seed_employees()
    seed_users()
    print("🌱 All data seeded.")
