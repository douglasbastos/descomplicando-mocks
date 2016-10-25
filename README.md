### Utilize python3 para realizar os testes.


```
mkvirtualenv -p python3 descomplicando-mocks
```

A biblioteca mock é nativa a partir do python3, caso queira utilizar python2 instale-a via pip

```
pip install mock
```

E altere os imports

```
from unittest import mock
```

para

```
import mock
```

### Rode os testes

```
py.test -skx
```
