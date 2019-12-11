# Products RestAPI
Simple Flask RestAPI to retrieve product information

---

## Install Dependincies

cd to **products** folder and:

```python
pip install -r requirements.txt
```

---

## Data Ingest
Raw data is ingested from CSV files and stored in SQLLite DB.
ingest_data.py is a simple script which accepts csv file as argument,
then parses the csv file and ingest data into the DB.
Note: It is assumed that the csv file will be of format specific for this exercise.

To execute the script and ingest datt, cd to the directory and:

```python
python ingest_data.py path_to_csv_file
```

---

## Running the APP
The app can be run either from a IDE capable of running flask applications like PyCharm
or can be run from command line:

cd to **products/app** folder and:
```python
export FLASK_APP=app.py
flask run
```
This should sart the server on localhost or displayed IP as above commands output

### Available EndPoints

/prod/<int: product_id>
retruns product details for specified product id, if present else returns error message

example:
```json
{
    "id": "1085936",
    "name": "wheeling",
    "brand": "Tabanus",
    "retailer": "anticourtier",
    "price": 293.0,
    "in_stock": true
}
```

/cheapest/<int:n>
returns list of cheapest products of **n** length.

eample:
```json
{
    "cheapest": [
        {
            "id": "8182756",
            "name": "mesencephalon",
            "brand": "abbey",
            "retailer": "zymology",
            "price": 0.1,
            "in_stock": false
        },
        {
            "id": "7009195",
            "name": "unworthiness",
            "brand": "felstone",
            "retailer": "Archimago",
            "price": 0.1,
            "in_stock": true
        },
        {
            "id": "3733492",
            "name": "asperuloside",
            "brand": "geoduck",
            "retailer": "defensive",
            "price": 0.1,
            "in_stock": true
        }
    ]
}
```


