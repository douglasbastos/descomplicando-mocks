import requests
import json


def pega_informacoes_usuario_github(username):
    url_api = 'https://api.github.com/users/{}'.format(username)
    response = requests.get(url_api)
    if response.status_code == 200:
        content = json.loads(response.content.decode('utf-8'))
        return content
    else:
        return 'Usuário não existe'
