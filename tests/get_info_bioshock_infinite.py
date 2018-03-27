import json
from steamapi.core import APIConnection

connection = APIConnection(api_key="A9AD261A3278990F62FD6A6193BEC570",
                           validate_key=True)
response = connection.call(interface='ISteamUserStats', command='GetSchemaForGame', version='v2', appid='8870')

with open('response_bioshock.json', 'w') as outfile:
    json.dump(response, outfile)
