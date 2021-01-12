
##### BEGIN #####
import requests
import json
current_access_token = "YTUxYTkyZTEtYjA4Ni00OGVkLWJlNjQtZGYzYzU3ZDVmNzc1NDU3MDAxNzctNjIx_PF84_consumer"
uri_scheme = 'https://'
uri_authority_server = 'api.ciscospark.com'
uri_api_path = '/v1/people/me'
url = uri_scheme + uri_authority_server + uri_api_path 
headers = {
    'Authorization': 'Bearer {}'.format(current_access_token),  
    'Content-Type': 'application/json'}

res = requests.get(url, headers=headers)
##### END #####

#YTlmZjgyNjItYzBkZC00ZWI2LWE0YjgtMmIxN2MwNjQyZjUzOTU5NjBiZmQtMGMy_PF84_consumer

#https://api.ciscospark.com/v1/people/me

#curl -X GET https://api.ciscospark.com/v1/people/me -H 'Authorization: Bearer YTUxYTkyZTEtYjA4Ni00OGVkLWJlNjQtZGYzYzU3ZDVmNzc1NDU3MDAxNzctNjIx_PF84_consumer' 

