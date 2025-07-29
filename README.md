  
  Beauty Services & Products Booking System API
This is the backend API for the Beauty Services and Products Booking System — a full-stack platform that allows customers to browse and book beauty services, purchase beauty products, and manage appointments. It also provides administrative functionality for managing users, services, products, employees, and orders.

 Project Structure
bash
Copy
Edit
.
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── user_routes.py
│   │   ├── product_routes.py
│   │   ├── service_routes.py
│   │   ├── booking_routes.py
│   │   ├── order_routes.py
│   │   └── employee_routes.py
│   ├── utils/
│   │   └── auth.py
│   └── config.py
├── migrations/
├── seed.py
├── requirements.txt
├── .env
└── run.py
⚙️ Tech Stack
Backend: Flask (RESTful architecture)

Database: PostgreSQL

ORM: SQLAlchemy

Authentication: JWT (JSON Web Tokens)

Migrations: Flask-Migrate

Password Security: Werkzeug Hashing

🧩 Features
🔐 Authentication
Register / Login using JWT

Role-based access control (admin / customer)

Passwords are hashed and never stored in plain text

👤 User Management
Admin and customer roles

User data includes: name, email, phone, country, timezone, etc.

🧴 Product Management
Admins can CREATE, READ, UPDATE, and DELETE beauty products

Products include: name, description, price, category, stock, etc.

💇 Service Booking
View all available beauty services

Book services and manage personal appointments

Admins can manage all bookings

💼 Employees
Admins can manage employee profiles

Assign services and availability

🧾 Orders & Payments
Customers can place product orders

Track order status

(Future Feature) Payment gateway integration

🗃️ Models Overview
User: Handles registration, login, and role permissions

Product: Represents items for sale

Service: Represents available beauty services

Booking: Customer appointments for services

Order: Purchase orders by customers

OrderItem: Items within an order (for multi-product orders)

Employee: Staff members performing services

🔄 API Endpoints
Auth
Method	Endpoint	Description
POST	/api/register	Register a user
POST	/api/login	Login and receive token

Users
Method	Endpoint	Description
GET	/api/users	List all users (admin)
GET	/api/users/<id>	Get single user

Products
Method	Endpoint	Description
GET	/api/products	List all products
POST	/api/products	Create new product (admin)
PATCH	/api/products/<id>	Update product (admin)
DELETE	/api/products/<id>	Delete product (admin)

Services
Method	Endpoint	Description
GET	/api/services	List all services
POST	/api/services	Create new service (admin)

Bookings
Method	Endpoint	Description
GET	/api/bookings	Get user bookings
POST	/api/bookings	Create new booking

Orders
Method	Endpoint	Description
POST	/api/orders	Create order (customer)
GET	/api/orders	List orders

🚀 Getting Started
Clone the Repo
bash
Copy
Edit
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd backend
Set Up Environment
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Configure Environment Variables
Create a .env file with:

env
Copy
Edit
DATABASE_URL=postgresql://username:password@localhost/db_name
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
Run Migrations
bash
Copy
Edit
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
Seed Database (Optional)
bash
Copy
Edit
python seed.py
Start the Server
bash
Copy
Edit
flask run
🧪 Testing
Use Postman or cURL to interact with endpoints. Ensure to set Authorization: Bearer <token> for protected routes.

✨ Future Improvements
Integrate a payment gateway (Stripe or Mpesa)

Add email notifications for bookings/orders

Improve employee scheduling

Build a dashboard for admins

Add pagination and filtering

👥 Contributors
Sam Mbogo

Team Moringa FT13 Phase 5


