from conf import HOST, PORT, r, c


# Create chat db:
try:
    r.db_create('chat').run(c)
except r.errors.ReqlOpFailedError:
    pass
else:
    print('Created chat db')

# Create log table:
try:
    r.db('chat').table_create('log').run(c)
except r.errors.ReqlOpFailedError:
    pass
else:
    print('Created log table')
