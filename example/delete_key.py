import redis

def delete_key(key):
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    return r.delete(key)
