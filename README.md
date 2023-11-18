# IntercityRailwayReservationSystem
IntercityRailwayReservationSystem is (Boom will handle this)..


## Installation
### Automated Installation
**For macOS**:
1) Download the install.sh script from the repository.
2) Open Terminal and navigate to the folder containing install.sh.
3) Run the script with ./install.sh.

**For Windows**:

1) Download the install.bat script from the repository.
2) Open Command Prompt and navigate to the folder containing install.bat.
3) Run the script by typing install.bat and pressing Enter.


### Manual Installation
**For macOS**:

1) Clone the repository:
```
git clone https://github.com/Jwizzed/IntercityRailwayReservationSystem.git
cd IntercityRailwayReservationSystem
```
2) Check if Python is installed:
```
python3 --version || python --version
```
If Python is not installed, download and install it from python.org.

3) Create a virtual environment:
```
python3 -m venv venv
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
python3 --version || python --version
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