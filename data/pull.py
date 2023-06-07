import requests
import json
from nom import get_geolocation
def locations():
    fin = []
    # Define the URL of the API endpoint
    url = 'https://data.birminghamal.gov/api/3/action/datastore_search_sql'

    # Define the SQL query you want to execute
    sql = 'SELECT * from "0f113c53-1559-45c1-8802-9bc0dfd52b52" LIMIT 100'  

    # Define the data payload to send with the request
    data = {
        'sql': sql
    }

    # Send the request
    response = requests.get(url, params=data)

    # Make sure the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()

        # Print the data
        #print(json.dumps(data, indent=4))
    else:
        # If the request was not successful, print the status code
        print(f'Request failed with status code {response.status_code}')

    data = response.json()

    # Access the import requests
    records = data['result']['records']

    # Loop through the import requests and print their attributes
    for record in records:
        x =  (get_geolocation(record['Block'],record['Street'],record['Case Address Zip'])) 
        if x != None:
            fin.append(x)

    return fin
print(locations())

