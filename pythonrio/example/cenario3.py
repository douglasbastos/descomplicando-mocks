from unittest.mock import Mock

# Mockado para não ter necessidade de criar o modelo,
UserHasPermission = Mock(return_value=1)


class NotPermission(Exception):
    pass


def tem_permissao(user, permissao):
    user = UserHasPermission.objects.filter(user=user, permissao=permissao)
    if user:
        return True
    else:
        raise NotPermission


def info_evento(key):
    events = {'pythonrio': 'Rio de Janeiro',
              'pythonbrasil2016': 'Florianópolois',
              'pythonbrasil2017': 'Belo Horizonte',
              'pythonsudeste2017': 'Rio de Janeiro'}
    try:
        permissao = tem_permissao(user='douglasbastos', permissao='ver_eventos')
        if permissao:
            return events.get(key, 'Nenhum evento encontrado')
    except Exception:
        return 'Você não tem permissão para essa operação'
