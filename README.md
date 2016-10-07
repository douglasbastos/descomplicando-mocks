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


if __name__ == '__main__':
    unittest.main()
```

```
$ python -m unittest test_simple
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

##### Exemplo de uso
