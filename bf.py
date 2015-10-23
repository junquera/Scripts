charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
complete_list = []
for current in xrange(50):
    a = [i for i in charset]
    for y in xrange(current):
        a = [x + i for i in charset for x in a]
    complete_list = complete_list+a
