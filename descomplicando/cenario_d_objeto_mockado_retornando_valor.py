from unittest.mock import Mock

class redis():
    def get(self):
        # Criado dessa forma para não precisar da instalação do redis
        pass


def is_positive(key):
    if redis.get(key) >= 1:
        return True
    return False
