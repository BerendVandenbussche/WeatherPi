## How to install
```
pip install -r requirements.txt
apt install pijuice-base
apt install sqlite3
```

## Add .env file
Example `.env`:

```
DBFILENAME="weatherdb.sql"
ONEWIRESENSORADDRESS="28-00000aee38a9"
DHT11SENSORPIN=27
PLUVIOPIN=21
PLUVIOSIZE=0.2794
ANEMOPIN=13
```

## Database
`sqlite` database with the following structure:

![Alt text](./WeatherDatabaseDiagram.jpg "database structure diagram")

### Database dump

*[Dump file](https://github.com/BerendVandenbussche/WeatherPi/blob/master/weatherdb.sql)*

## How to run

Run the backend

```
gunicorn -w 4 -b 0.0.0.0:5500 wsgi:app
```
