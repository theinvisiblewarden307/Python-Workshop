#Excercise: User info

def info(username, id):
    is_admin = id<100
    return is_admin, {'first':username, 'id':id}

info('Ramanuj', 5)