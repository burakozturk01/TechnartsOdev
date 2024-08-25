## Description

This project is a Django REST Framework application that allows users to manage airlines and their associated planes. It provides endpoints for adding, updating, and listing airlines and planes. The project also includes JWT authentication to verify user login status.

## Features

- CRUD operations for airlines and planes
- JWT authentication

## Installation

To install this project, follow these steps:

1. Clone the repository: `git clone https://github.com/burakozturk01/TechnartsOdev.git`
2. Activate the virtual environment: (powershell) `./venv/Scripts/Activate.ps1`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Set up the database: `python manage.py migrate`
5. Start the development server: `python manage.py runserver`

## Usage

To use this project, follow these steps:

1. Open Postman and import the provided Postman Collection.
2. Make sure the Django development server is running.
3. Authenticate with JWT by sending a POST request to the `/api/token/` endpoint with valid credentials.
4. Use the obtained token to include in the `Authorization` header for subsequent requests.
5. Use the available endpoints to manage airlines and planes.
