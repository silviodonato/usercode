import requests

FED = 164
subsystem = "TECminus"
urlBase = "https://stripcabling.web.cern.ch/%s/FED_%d/ourAliasforCabling.txt"

cookies=None

cookies = [
{
    "domain": ".cern.ch",
    "expirationDate": 1739807865.431355,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_ga",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "GA1.2.777218723.1690451477",
    "id": 1
},
{
    "domain": ".cern.ch",
    "expirationDate": 1736325318.889691,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_ga_872FB4C5HF",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "GS1.1.1701765318.1.0.1701765318.60.0.0",
    "id": 2
},
{
    "domain": ".cern.ch",
    "expirationDate": 1726476694.531383,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_ga_QKCN98CYKH",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "GS1.2.1691916694.1.0.1691916694.0.0.0",
    "id": 3
},
{
    "domain": ".cern.ch",
    "expirationDate": 1736325318.974262,
    "hostOnly": False,
    "httpOnly": False,
    "name": "_ga_ZXXEKF4B3S",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "GS1.1.1701765318.1.0.1701765318.60.0.0",
    "id": 4
},
{
    "domain": ".cern.ch",
    "expirationDate": 1721979319,
    "hostOnly": False,
    "httpOnly": False,
    "name": "rl_anonymous_id",
    "path": "/",
    "sameSite": "lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "%22dc67d1c2-6e72-41c2-a7c2-ce2c5d5c2e1f%22",
    "id": 5
},
{
    "domain": ".cern.ch",
    "expirationDate": 1735926571,
    "hostOnly": False,
    "httpOnly": False,
    "name": "rl_user_id",
    "path": "/",
    "sameSite": "lax",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "%22%22",
    "id": 6
},
{
    "domain": "stripcabling.web.cern.ch",
    "hostOnly": True,
    "httpOnly": True,
    "name": "9c7d484949d4ac9c26f0215451a62c9d",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": True,
    "session": True,
    "storeId": "0",
    "value": "b160583b25e555a466f3e598e0b894ed",
    "id": 7
},
{
    "domain": "stripcabling.web.cern.ch",
    "hostOnly": True,
    "httpOnly": True,
    "name": "mod_auth_openidc_session",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": True,
    "storeId": "0",
    "value": "f0ed9bc7-4243-4dc3-8f79-398268323f90",
    "id": 8
}
]
for FED in [164]:
    for subsystem in ["TECminus"]:
        response = requests.get(urlBase%(subsystem, FED), cookies=cookies)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        with open(filename, 'w', encoding='utf-8') as file:
            print(response.text)
#            file.write(response.text)


