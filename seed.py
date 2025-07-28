import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app import create_app, db
from models.user import User
from models.service import Service
from models.employee_services import EmployeeService
from models.employee import Employee
from models.tables import Table
from models.booking import Booking

app = create_app()
print("📦 Using DB:", app.config["SQLALCHEMY_DATABASE_URI"])

with app.app_context():
    db.drop_all()
    db.create_all()

    
    u1 = User(name='Sam Mbogo', email='sam@gmail.com', password_hash='hash', phone='12345678', address='Nairobi', country='KE')
    
   
    s1 = Service(name='Pedicure', duration_minutes=60, price=2500)
    e1 = Employee(name='Maya', role='Beautician', email='maya@beauty.com', phone='0712345678')
    t1 = Table(name='Table 1', capacity=1)

    db.session.add_all([u1, s1, e1, t1])
    db.session.commit()

    print("✅ Seeded Successfully.")
