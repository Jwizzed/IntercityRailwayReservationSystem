# IntercityRailwayReservationSystem
IntercityRailwayReservationSystem is (Boom will handle this)..


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