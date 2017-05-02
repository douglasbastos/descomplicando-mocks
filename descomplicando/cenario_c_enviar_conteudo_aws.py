from unittest.mock import Mock
boto3 = Mock()


def enviar_conteudo_aws(filename, body):
    boto3.send(filename, body)
