

class SemPermissao(Exception):
    pass


def tem_permissao(user, permissao):
    pass


def ver_evento(user, evento='pythonbrasil'):
    if tem_permissao(user=user, evento=evento):
        return 'De 06 a 11 de Outubro'
    raise SemPermissao


def mostrar_data_da_proxima_pybr():
    try:
        return ver_evento(user='douglasbastos',
                          evento='pythonbrasil')
    except SemPermissao:
        return 'Seu usuário não tem permissão'