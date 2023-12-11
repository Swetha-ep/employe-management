#Employee Management System

Welcome to the Employee Management System, a dynamic platform designed to effortlessly handle every aspect of workforce administration. This system was developed using HTML, CSS, JavaScript, Bootstrap for the frontend, and Django with MySQL for the backend.

Getting Started
To run the project locally, follow these steps:

Prerequisites
Python 
Django
MySQL
Setup


Clone the repository:
git clone https://github.com/Swetha-ep/Project-Employee.git

Navigate to the project directory:
cd Project-Employee


Create and activate a virtual environment:
python -m venv env
source env/bin/activate  

Install dependencies:
pip install -r requirements.txt

Configure the Database:
Create a MySQL database.

Copy the .env.example file to .env:
cp .env.example .env
Update the .env file with your database settings.

Apply migrations:
python manage.py migrate

Run the development server:
python manage.py runserver
Access the application in your browser at http://127.0.0.1:8000/.

Usage:
Navigate to http://127.0.0.1:8000/ to access the Employee Management System.

  


