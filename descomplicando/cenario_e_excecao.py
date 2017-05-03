

class SemPermissao(Exception):
    pass


def tem_permissao(user, permissao):
    pass


def data_proximo_pybr(user):
    if tem_permissao(user=user, permissao='ver evento'):
        return 'De 06 a 11 de Outubro'
    raise SemPermissao


def mostrar_data_da_proxima_pybr():
    try:
        return data_proximo_pybr(user='douglasbastos')
    except SemPermissao:
        return 'Seu usuário não tem permissão'