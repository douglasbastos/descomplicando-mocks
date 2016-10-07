# Descomplicandos os mocks

Testar unitariamente é fácil, mas quando temos uma dependência externa no nosso código, a implementação do teste acaba demorando quando não sabemos usar direito os paranauês do mock.

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

**Mas por quê devemos isolar?**

Vamos dizer que sua função pega informações que estão armazenadas em um banco NoSQL, no nosso exemplo será o redis.


# Exemplo de uma função acessando
https://api.github.com/users/douglasbastos

# Teste para essa função.

Ao executar esse teste sempre estaremos indo até a API do github pegando a informações e validando as informações.
Mas existem vários problemas nessa implementação.

-Estaremos fazendo um request de verdade, tornando nosso teste mais demorado.
-Dependendo da frequência a própria API bloquear o acesso.
-Quando a API mudar qualquer informação ou mesmo ficar fora do ar, seu teste vai quebrar

Quando temos esse tipo de situação utilizamos uma biblioteca chamada Mock

# pip install mock

Abaixo o exemplo da solução utilizando mock

# Exemplo do teste utilizando mock

# Explicar como funciona o mock no teste criado acima

# Explicar como funciona a biblioteca mock

# Mostrar outras formas de mockar um objeto(decorator, with, setUp)

# Quando quero testar se uma função chamou outra função(call_count, call_arg_list, etc)

# Quando quero testar uma lógica com dia de semana e dependo do datetime.now()

# Quando quero testar uma requisição para uma API, e mockar os dados retornados por ela.

# Mostrar os problemas que temos ao utilizar mocks
