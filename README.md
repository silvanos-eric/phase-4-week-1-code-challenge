# Superheroes API 🚀

## Overview
This is an incredible Flask-based web application that allows you to manage superheroes and their powers! Built using SQLAlchemy and Alembic for database handling and migrations, this app provides an exciting interface to retrieve, update, and create superheroes and their awesome powers.

## Project Structure
Here is the structure of the project:

```bash
.
├── .gitignore                     # Lists files and directories to be ignored by Git
├── LICENSE                        # Project license (MIT)
├── Pipfile                        # Package dependencies
├── Pipfile.lock                   # Locked package versions
├── README.md                      # Project documentation (this file)
└── server
    ├── app.py                     # Main Flask application
    ├── debug.py                   # Debugging utilities using ipdb
    ├── instance/                  # Contains SQLite database (ignored in Git)
    │   └── app.db                 # SQLite database file (excluded)
    ├── migrations/                # Alembic migrations
    │   ├── alembic.ini            # Alembic configuration
    │   ├── env.py                 # Migration environment
    │   ├── README                 # Migration documentation
    │   ├── script.py.mako         # Template for Alembic migrations
    │   └── versions/              # Versioned migration scripts
    │       └── da48c45b06b5_create_table_heroes_powers_heroes_and_.py
    ├── models.py                  # SQLAlchemy models for heroes and powers
    └── seed.py                    # Script for seeding initial data

```

## Features ✨

- **Retrieve Heroes and Powers**: Easily get a list of heroes or powers in a neatly formatted way.
- **Update Powers**: Modify existing superhero powers with PATCH requests.
- **Create Hero-Power Relationships**: Dynamically assign powers to heroes with varying strength levels.
- **Fully Seeded Data**: Start with a beautifully curated set of heroes and powers.

## Setup Instructions 🔧

### Prerequisites
- **Python 3.10+**: Ensure you have Python 3.10 or higher installed on your machine.
- **Pipenv**: This project uses `Pipenv` for clean, straightforward dependency management. Install it with:
  ```bash
  pip install pipenv
  ```

### Installation Steps 🛠️
1. Clone the repository:
   ```bash
   git clone https://github.com/silvanos-eric/phase-4-week-1-code-challenge.git
   ```
2. Navigate into the project directory:
   ```bash
   cd phase-4-week-1-code-challenge
   ```
3. Install the dependencies:
   ```bash
   pipenv install
   ```

### Running the Application 🎮
1. Start the virtual environment:
   ```bash
   pipenv shell
   ```
2. Run the Flask app:
   ```bash
   python server/app.py
   ```
   The application will start on `localhost:5555` and is now ready to serve superhero data!

### Database Migrations 📊
1. **Create a migration**:
   ```bash
   flask db migrate  -m "Add migration message"
   ```
2. **Apply migrations**:
   ```bash
   flask db upgrade
   ```

### Seeding the Database 🌱
Populate your database with amazing data using:
```bash
python server/seed.py
```
This will insert heroes and powers into the database and create thrilling hero-power relationships!

## API Endpoints 🌐

### GET `/`
Returns a welcome message indicating the API is live.

### GET `/heroes`
Returns a list of all heroes, excluding their related powers.

### GET `/heroes/<id>`
Fetches details for a specific hero by their ID.

### GET `/powers`
Returns a list of all available powers.

### GET `/powers/<id>`
Returns details of a specific power by ID.

### PATCH `/powers/<id>`
Allows updates to a power’s details using a JSON payload.

### POST `/hero_powers`
Creates a new hero-power relationship, with custom strength, using a JSON payload.

## Ignored Files 🛑
The following files and directories are excluded from version control, as outlined in the `.gitignore`:
- `instance/` (e.g., `app.db`) — Local instance folder for database storage.
- Compiled Python files (`*.pyc`, `__pycache__/`), build files (`dist/`, `build/`), and various virtual environment directories (`env/`, `venv/`).

## License 📄
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.