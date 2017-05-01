import responses
from unittest import TestCase
from example.cenario6 import pega_informacoes_usuario_github


class PegaInformacoesUsuarioGitHubTest(TestCase):

    @responses.activate
    def test_deve_retornar_informacoes_do_usuario_caso_ele_exista(self):
        info = {'username': 'douglasbastos', 'location': 'Rio de Janeiro'}
        username = 'douglasbastos'
        url_api = 'https://api.github.com/users/{}'.format(username)
        responses.add(responses.GET, url_api,
                      json=info, status=200)

        result = pega_informacoes_usuario_github(username)
        self.assertDictEqual(result, info)

    @responses.activate
    def test_deve_retornar_mensagem_de_nao_encontrado_caso_usuario_nao_exista(self):
        username = 'douglasbastos'
        url_api = 'https://api.github.com/users/{}'.format(username)
        responses.add(responses.GET, url_api,
                      body='{"error": "not found"}', status=404)

        result = pega_informacoes_usuario_github(username)
        self.assertEqual(result, 'Usuário não existe')
