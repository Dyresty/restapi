# REST API Projects

This repository contains two mini projects:

1. **Custom REST API** using Flask and SQLAlchemy (`application.py`)
2. **StackOverflow API Consumer** using the StackExchange API and `requests` (`api.py`)

## 1. Custom REST API with Flask (`application.py`)

This is a simple REST API that allows you to create, read, update, and delete (CRUD) drinks using SQLite as the database.

### Features

- Create a new drink (`POST /drinks`)
- Get all drinks (`GET /drinks`)
- Get a specific drink by ID (`GET /drinks/<id>`)
- Update a drink by ID (`PUT /drinks/<id>`)
- Delete a drink by ID (`DELETE /drinks/<id>`)

### Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/rest-api-projects.git
   cd rest-api-projects
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

   - On Mac/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install flask flask_sqlalchemy
   ```

5. **Run the Application**

   Run directly:
   ```bash
   python application.py
   ```

   Or using Flask CLI:
   ```bash
   set FLASK_APP=application.py     # On Windows
   export FLASK_APP=application.py  # On Mac/Linux
   flask run
   ```

### Using the API

Use **Postman** or **Insomnia** to test the endpoints:

- `GET http://localhost:5000/drinks`
- `POST http://localhost:5000/drinks`
  ```json
  {
    "name": "Lemonade",
    "description": "Fresh and cool"
  }
  ```
- `PUT http://localhost:5000/drinks/1`
  ```json
  {
    "name": "Iced Tea",
    "description": "Sweet and cold"
  }
  ```
- `DELETE http://localhost:5000/drinks/1`

---

## 2. StackOverflow API Consumer (`api.py`)

This script fetches the most active recent questions from StackOverflow using the StackExchange API.

### Features

- Retrieves questions using `requests`
- Filters and displays only questions with a score ≥ 1
- Outputs title, link, and score

### Stack Used

- Python
- Requests module
- StackExchange API

### Setup Instructions

1. Ensure you are in the virtual environment (created above).

2. Run the script:
   ```bash
   python api.py
   ```

### Output Example

```
How do I reverse a list in Python?
https://stackoverflow.com/questions/12345
Score: 4
```

If the score is < 1, it prints:
```
Skipped because the criteria of score>=1 is not satisfied
```

---
