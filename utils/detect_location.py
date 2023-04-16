import requests, os


def getUserIP():
    # getting user-ip
    try:
        url = 'https://api.ipify.org?format=json'
        response = requests.get(url)
        if response:
            user_ip = response.json()['ip']
    except:
        # set up a default ip
        user_ip = '167.99.203.64'
        
    return user_ip
        
def getLocation():
    USER_IP = getUserIP()
    API_KEY = os.environ.get('apiip_APIKEY')
    try:
        url = f'http://apiip.net/api/check?ip={USER_IP}&accessKey={API_KEY}'
        response = requests.get(url).json()
        return response['latitude'], response['longitude']
    except:
        print('wow')
