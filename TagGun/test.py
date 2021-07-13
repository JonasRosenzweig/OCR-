import requests
from configparser import ConfigParser

url = 'https://api.taggun.io/api/receipt/v1/verbose/file'

config = ConfigParser()
configFile = 'API_key.conf'

with open(configFile) as f:
    config.read_file(f)
APIkey = config.get('API', 'API_key')


if __name__ == '__main__':
    headers = {'apikey': APIkey}

    files = {
        'file': (
            'just_eat.png',  # set a filename for the file
            open(r'C:\Users\surface\Desktop\YouWe\OCR\Receipts\just_eat.png', 'rb'),  # the actual file
            'image/png'),  # content-type for the file

        # other optional parameters for Taggun API (eg: incognito, refresh, ipAddress, language)
        'incognito': (
            None,  # set filename to none for optional parameters
            'false')  # value for the parameters
    }

    response = requests.post(url, files=files, headers=headers)

    print(response.content)
