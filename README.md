# Descomplicandos os mocks

Testar unitariamente é fácil, mas quando temos uma dependência externa no nosso código, a implementação do teste acaba demorando quando não sabemos usar direito os paranauês do mock.

TODO
*Explicar um pouco o que vai ser feito no artigo*

Teste de unidade
---
O teste de unidade mais conhecido como teste unitário é aquele que testa uma única unidade do sistema. Ele a testa de maneira isolada que consiste em verificar dados válidos e inválidos via entrada e saída.

```
# simple.py

def soma(num1, num2):
    return num1 + num2
```

```
# test_simple.py

import unittest
from example.simple import soma


class SomaTest(unittest.TestCase):

    def test_soma_certa(self):
        result = soma(2, 2)
        self.assertEqual(result, 4)
```

Rodando o teste
```
$ python -m unittest test_simple
```

Você poderá visualizar todo o código do artigo no [github](https://github.com/douglasbastos/descomplicando-mocks), para executar os testes a partir de lá só será necessário modificar o caminho do arquivo, ficando por exemplo:

```
$ python -m unittest example.tests.test_simple
```

Dependências externas
---
Mas quando temos dependência externa, por exemplo banco de dados ou API. Devemos isolar o nosso código.

##### Mas por quê devemos isolar?

Vamos dizer que sua função precisa de informações que estão armazenadas em um banco NoSQL, no nosso exemplo será o redis.

Função abaixo pede ao redis que exclua uma determinada chave.
```
# delete_key.py

import redis

def delete_key(key):
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    return r.delete(key)
```
No exemplo acima, vemos que foi aberta uma conexão com um banco de dados.

##### O que temos de problema nessa abordagem?

* É necessário ter um banco de dados redis instalado e rodando.
* É necessário armazenar valores no redis antes de iniciar os testes.

##### E como conseguimos testar?

```
$ pip install mock
```

```
from  unittest import TestCase
import mock

from example.delete_key import delete_key

class DeleteKeyTest(TestCase):

    @mock.patch('example.delete_key.redis')
    def test_remove_chave(self, redis):
        delete_key('1234')
        self.assertTrue(redis.StrictRedis.return_value.delete.called)
```

Observe que chamamos o mock a partir de um decorator, passando o caminho do arquivo até chegar no objeto que queremos mockar, nesse exemplo é o redis.

Existe mais duas formas de criar esse mock.
class DeleteKeyTest(TestCase):

```
class DeleteKeyTest(TestCase):

    def test_remove_chave(self):
        with mock.patch('example.delete_key.redis') as redis:
            delete_key('1234')
            self.assertTrue(redis.StrictRedis.return_value.delete.called)
```
Utilizando with, onde não temos diferença na execução

```
class DeleteKeyTest(TestCase):

    @classmethod
    def setUp(cls)
        self.redis_patcher = mock.patch('example.delete_key.redis')
        self.redis = self.patcher.start()

    def test_remove_chave(self):
            delete_key('1234')
            self.assertTrue(self.redis.StrictRedis.return_value.delete.called)
```
