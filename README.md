# Pet Adoption Site

This application is a mock pet adoption site.  Users are able to see all pets and availability. Users can add, view, and edit pet profiles.

This focus of this application is to implement Flask,  Flask-SQLAlchemy, and WTForms.

## Set Up:

__Linux:__

```python3 -m venv venv```

```source venv/bin/activate```

```(venv) pip install -r requirements.txt```

```(venv) flask run```

__Windows:__

```python3 -m venv venv```

or

```python3 -m pip install virtualenv venv```

```venv\Scripts\activate.bat```

```(venv) python3 -m pip install -r requirements.txt```

```(venv) flask run ```

__Database:__

```(psql) CREATE DATABASE pet_adoption ```

```(venv) python seed.py ```