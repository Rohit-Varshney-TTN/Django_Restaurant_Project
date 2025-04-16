Restaurant Management System (Django)
=====================================

A Restaurant App built using Django to manage food items, 
orders, and cart functionality efficiently.

Features:
---------
- Search food by name & category
- Add to cart & remove from cart
- User authentication (Login, Register, Logout)
- Food menu with categories (Veg/Non-Veg)
- Upload & display food images
- Admin panel to manage food items

Project Structure:
------------------
```
myproject/
  ├── account/          (User authentication)
  ├── cart/             (Cart functionality)
  ├── food/             (Food item management)
  ├── templates/        (HTML templates)
  ├── static/           (CSS & JS files)
  ├── manage.py         
  ├── db.sqlite3        
```

Setup & Installation:
---------------------
1. Clone the repository:
   git clone https://github.com/Rohit-Varshney-TTN/Django_Restaurant_Project
   cd restaurant-management

2. Create and activate virtual environment:
   python -m venv myenv
   source myenv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Apply migrations and run the server:
   python manage.py migrate
   python manage.py runserver

5. Open the application:
   http://127.0.0.1:8000/

Admin Panel:
------------
To access the admin panel, create a superuser:
   python manage.py createsuperuser

Login at: http://127.0.0.1:8000/admin/
