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

Ou utilizando versões superiores à python3.3 ele vem por padrão dentro da biblioteca unittest

```
from unittest import mock
```

##### Mas o que essa biblioteca faz?
Ele permite que você substituia partes de seu sistema na execução de testes, adicionando valores fictícios. Assim simulando comunicações externas.

Vamos utilizar a função criada anteriomente e vamos isolar a parte onde ocorre comunicação com o Redis.

```
from unittest import TestCase, mock

from delete_key import delete_key

class DeleteKeyTest(TestCase):

    @mock.patch('delete_key.redis')
    def test_remove_chave(self, redis):
        delete_key('1234')
        self.assertTrue(redis.StrictRedis.return_value.delete.called)
```

Ao utilizar o decorator mock.patch, devemos passar o caminho do objeto que queremos isolar, normalmente o caminho do arquivo desde a raiz do projeto, até o objeto que está dentro do arquivo.

Para o melhor entendimento, abaixo está o retorno quando chamamos diretamente o redis, e quando estamos mockando

```
>>> import redis
>>> redis
<module 'redis' from '/home/douglasbastos/.virtualenvs/jobs/local/lib/python2.7/site-packages/redis/__init__.pyc'>
```
Sem o uso de mock.

```
>>> import redis
>>> from mock import Mock

>>> redis = Mock()
>>> redis
<Mock id='139814111313872'>
```
Utilizando a biblioteca mock


**Existe outras formas de mocks objetos.**

Utilizando with, onde não temos diferença na execução
```
class DeleteKeyTest(TestCase):

    def test_remove_chave(self):
        with mock.patch('example.delete_key.redis') as redis:
            delete_key('1234')
            self.assertTrue(redis.StrictRedis.return_value.delete.called)
```

No setup onde mockamos apenas uma vez e seu valor é válido para todos os testes dentro daquela classe.

```
class DeleteKeyTest(TestCase):

    def setUp(self)
        self.redis_patcher = mock.patch('example.delete_key.redis')
        self.redis = self.patcher.start()

    def test_remove_chave(self):
            delete_key('1234')
            self.assertTrue(self.redis.StrictRedis.return_value.delete.called)
```

Utilizando ```mock.patch('caminho.objeto')``` passamos uma string do caminho relativo do objeto que queremos mockar, mas podemos utilizar ```mock.patch.object(Class, 'method')``` quando queremos mockar ao expecifico de dentro de uma class.

```
 -- Exemplo utilizando mock.patch.object(Class, 'method')
```

Podemos simular um valor de retorno quando necessário, fazemos isso utilizando ```return_value```

```
# helper.py
import redis


def get_value(key):
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    return r.get(key)


def is_positive_number(key):
    if get_value(key) >= 1:
        return True
    return False

```

Acima estamos criando uma função que ao receber uma chave, ele consulta o banco redis e depois de pegar essa informação ele verifica se é positivo ou negativo.

Para testar isso precisamos simular um valor de retorno para o ```get_value```. Faremos isso no teste abaixo


```
from unittest import TestCase, mock

from helper import get_value, is_positive_number


class IsNumberPositiveTest(TestCase):

    @mock.patch('helper.get_value', return_value=4)
    def test_deve_retornar_true_quando_numero_positivo(self, redis):
        result = is_positive_number('key')
        self.assertTrue(result)


    @mock.patch.object('helper.get_value', return_value=-4)
    def test_deve_retornar_false_quando_numero_negativo(self, redis):
        result = is_positive_number('key')
        self.assertFalse(result)
```

Passamos um segundo argumento dentro do decorator, simulamos o valor que será retornado pelo ```get_value```. Dessa forma quando o ```is_positive_number``` chama get_value, o mesmo não é executado, somente retorna o valor de ```return_value```.

Quando o retorno é um Exception, podemos utilizar o ```side_effect``` como o exemplo abaixo.

```
 -- Exemplo de side_effect
```

Você pode ter observado no primeiro teste realizado nesse artigo temos um ```assert(delete.called)```, esse called é um dos diversos métodos que nos ajudam a testar dentro da Python. Por exemplo o ```called``` como o próprio nome diz, confere se a função delete que foi mockada foi chamada em algum momento.

São diversos métodos dentro de mock que podem nos ajudar nesse quesito, demostrarei alguma deles.

######  call_args

######  call_args_list

######  call_count

######  assert_called_with

######  assert_called_once_with

######  assert_any_call

######  Conclusão