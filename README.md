# A simple "Search Engine"
for my internship.

## Installation
- You need Python 3.11 installed and a mysql server running on your machine.
- Install the required libraries by running the command `pip install -r requirements.txt`.
- make a copy of `.env.example` and name it `.env` and customize the edit the file the way you want.
- You can either import the test database by importing the `users.sql` file or using the command `alembic head upgrade`.
And here you go!
All you need to do is to run `main.py` and go to the address you choose in .env file (by default: `127.0.0.1:8000/docs`)
