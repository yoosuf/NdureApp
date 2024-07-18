# Ndure App

## Overview
Ndure is a Django-based application designed to manage users, their workout logs, and training packages. The application supports user authentication, user management, workout types, and workout logs with the ability to associate trainers and training packages. The app also supports multiple time zones for users.

## Features
- User registration, login, and profile management
- Support for multiple time zones
- Workout types management
- Workout logs with multiple workout types
- User training packages
- Admin interface to manage users, workout logs, and packages
- Group-based user filtering for customers and trainers

## Requirements
- Python 3.12
- Django 4.0
- PostgreSQL (recommended for production)
- `pytz` for timezone support

## Installation

### Clone the Repository
```sh
git clone https://github.com/yourusername/ndure_app.git
cd ndure_app
```

## Create and Activate Virtual Environment

```sh
python -m venv ndure_env
source ndure_env/bin/activate  # On Windows use `ndure_env\Scripts\activate`
```

## Install Dependencies

```sh
pip install -r requirements.txt
```

## Set Up Environment Variables
Create a .env file in the project root and add your environment-specific variables:

```sh
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/ndure_db
```

## Apply Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

## Create a Superuser
```sh
python manage.py createsuperuser
```

## Run the Development Server
```sh
python manage.py runserver
```
## Usage

- Access the application at http://127.0.0.1:8000/
- Access the admin interface at http://127.0.0.1:8000/admin/


## Project Structure

```
ndure_app/
├── ndure_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── workouts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   └── ...
├── static/
│   ├── css/
│   ├── js/
│   └── ...
├── manage.py
└── requirements.txt
```

# MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


# Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

