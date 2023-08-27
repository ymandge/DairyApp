Directory structure we followed -

    Todo - Directory structure is bit changed, please correct this readme file as new directory structure
    milk_delivery_app/
    ├── app/
    │   ├── controllers/
    │   ├── models/
    │   ├── services/
    │   ├── utils/
    │   └── __init__.py
    ├── migrations/
    ├── tests/
    ├── config.py
    ├── requirements.txt
    ├── run.py
    └── README.md

Let's go through each directory and its purpose:

    • app/: This directory contains the core application code.

    • controllers/: It holds the controller modules responsible for handling the API routes and request/response handling.

    • models/: This directory contains the database models or data schemas for your application entities.

    • services/: It holds the business logic and service modules that encapsulate the application's functionality.

    • utils/: This directory contains utility functions or helper modules that can be reused across the application.

    • __init__.py: This file initializes the Flask application and registers the necessary components.

    • migrations/: If you're using a database migration tool like Alembic or Flask-Migrate, this directory can store the database migration scripts.

    • tests/: This directory is used for writing test cases and holds the unit tests for your application.

    • config.py: The configuration file where you can define environment-specific configurations, database connection details, and other settings.

    • requirements.txt: This file lists all the dependencies and libraries required for running the application. It helps to manage the project's dependencies.

    • run.py: The entry point for running the application.

    • README.md: A readme file that provides an overview of the project, installation instructions, and any other relevant information.

Desing page: https://docs.google.com/document/d/14HrpnqMSMzDOoQ7a9hV5wZ2IPvqsoTno5sIWBWVlICk/edit?usp=sharing



How to run app :
    1. gunicorn -b 0.0.0.0:8000 "DairyApp.__main__:make_app('test')"
    2. On Localhost - http://localhost:8000/dairyapp/ 
    3. On Windows machine - http://192.168.11.128:8000/dairyapp/