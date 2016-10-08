from  unittest import TestCase
import mock

from example.delete_key import delete_key

class DeleteKeyTest(TestCase):

    @mock.patch('example.delete_key.redis')
    def test_remove_chave(self, redis):
        delete_key('1234')
        self.assertTrue(redis.StrictRedis.return_value.delete.called)
