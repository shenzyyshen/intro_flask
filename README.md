# Intro Flask Project
# Intro Flask Project

This is a simple Flask application to demonstrate basic routing, templates, and forms.

## Features

- Home page with a welcome message and current time
- Dynamic user data display
- Form to update a user's country
- View all users
- Greet users dynamically via URL
- Custom 404 error page

## Project Structure

intro_flask/
│
├── main.py # Flask application
├── templates/ # Jinja2 HTML templates
│ ├── base.html
│ ├── home.html
│ ├── form.html
│ ├── update_country.html
│ ├── all_users.html
│ └── 404.html
├── static/ # Static files (CSS, images)
│ ├── style.css
│ └── images/
└── README.md # Project documentation


## Usage

/ : Home page

/all-users : List all users

/update-country : Update a user's country

/greet/<name> : Greet a user dynamically

/form : Simple form example

## Requirements

- Python 3.10+  
- Flask  

Install Flask with:

```bash
pip install flask

python3 main.py
