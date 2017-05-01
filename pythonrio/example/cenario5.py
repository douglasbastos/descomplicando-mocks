import datetime


def saudacao():
    current_time = datetime.datetime.now()

    if current_time.hour < 12:
        msg = 'Bom dia'
    elif 12 <= current_time.hour < 18:
        msg = 'Boa tarde'
    else:
        msg = 'Boa noite'

    return msg
