from example.cenario1 import send_content
from unittest import TestCase, mock


class SendContentTeste(TestCase):

    # Mock está sendo criado no declaração with
    def test_send_content(self):
        with mock.patch('example.cenario1.upload_aws') as upload_aws:
            send_content('Hello Word', 'helloword.txt')
            upload_aws.assert_called_with('Hello Word', 'helloword.txt')

    # Aqui estou realizando o mesmo teste de cima, mas utilizando decorator
    @mock.patch('example.cenario1.upload_aws')
    def test_send_content_sintax2(self, upload_aws):
        send_content('Hello Word', 'helloword.txt')
        upload_aws.assert_called_with('Hello Word', 'helloword.txt')


# Aqui estou utilizando o mesmo teste, mas adicionando no setUp que será
# reaproveitado para todos os testes da classe
class SendContentUsingPatchTeste(TestCase):

    def setUp(self):
        self.upload_aws_patcher = mock.patch('example.cenario1.upload_aws')
        self.upload_aws = self.upload_aws_patcher.start()

    def tearDown(self):
        self.upload_aws_patcher.stop()

    def test_send_content(self):
        send_content('Hello Word', 'helloword.txt')
        self.upload_aws.assert_called_with('Hello Word', 'helloword.txt')
