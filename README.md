# IntercityRailwayReservationSystem
IntercityRailwayReservationSystem is a part of the "Database Systems for Software and Knowledge Engineers"(01219231) course.
It's a web application that mainly focuses on the database workflow of the railway ticket system. The aim of this project
is to create a mock  of the real business and integrate the database system to answer the business question.

## Goals
The user can...
- Book the train ticket using the web app
- View all tickets
- inspect the ticket detail
- Search routes

## Installation
**For macOS**:

1) Clone the repository:
```
git clone https://github.com/Jwizzed/IntercityRailwayReservationSystem.git
cd IntercityRailwayReservationSystem
```
2) Check if Python is installed:
```
python --version || python --version
```
If Python is not installed, download and install it from python.org.

3) Create a virtual environment:
```
python -m venv venv
source venv/bin/activate
```
4) Install dependencies:
```
pip install -r requirements.txt
```
5) Migrate the database:
```
python manage.py migrate
```
6) Load sample data:
```
python manage.py loaddata sample_db.json
```
7) Run the server:
```
python manage.py runserver
```

For Windows:

1) Clone the repository:
```
git clone https://github.com/Jwizzed/IntercityRailwayReservationSystem.git
cd IntercityRailwayReservationSystem
```
2) Check if Python is installed
```
python --version || python --version
```
3) Create a virtual environment:
```
python -m venv venv
.\venv\Scripts\activate
```
4) Install dependencies:
```
pip install -r requirements.txt
```
5) Migrate the database:
```
python manage.py migrate
```
6) Load sample data:
```
python manage.py loaddata sample_db.json

```
7) Run the server:
```
python manage.py runserver
```
