# importing the requests library
import requests

# api-endpoint
URL = "http://webservices.nextbus.com/service/publicJSONFeed"

# input STOPID and ROUTETAG
# EXAMPLE STOPID=12029 and ROUTETAG=42
STOPID = input("Enter STOP ID: ")
ROUTETAG = input("Enter ROUTE TAG: ")

# defining a params dict for the parameters to be sent to the API
PARAMS = {
    # tell api to send predictions back
    'command': "predictions",
    # tell api the agency we want is ttc
    "a": "ttc",
    "stopId": STOPID,
    "routeTag": ROUTETAG
}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

# go through the nested data to find what we want which is the prediction
predictions = data['predictions']["direction"]["prediction"]

# loop over each bus predicted arrived
for prediction in predictions:
    minutes = prediction["minutes"]
    print("Bus in {} minutes".format(minutes))
