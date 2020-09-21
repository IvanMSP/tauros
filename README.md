# Test Backend Tauros


# Technology Stack

   [Django framework 3.0.7](https://www.djangoproject.com/)

   [Django rest framework 3.11](https://www.django-rest-framework.org/)

   [Postgres](https://www.postgresql.org/)

   [sqlite3](https://www.sqlite.org/)

   [Git Flow](https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow)

# Install Project

    1. Create virtual enviroment
        `virtualenv -p python3 env`

    2. Activate enviroment
        `source env/bin/activate`

    3. Clone the project and run the next commands.

    4. Install all the requirements
        `pip install -r requirements/development.txt`

    5. Migrate the migrations
        `python manage.py migrate`

    6. Create super user
        `python manage.py createsuperuser`

    7. run server
        `python manage.py runserver`

    ## Note:
        Download the file .env

# Documentation Endpoints

[API Documentation Tauros]()