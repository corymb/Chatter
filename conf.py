import os
import sys

import rethinkdb as r

PORT=os.environ.get('RETHINK_HOST', '28015')
HOST=os.environ.get('RETHINK_PORT', 'localhost')

try:
    c = r.connect(host=HOST, port=PORT)
except r.errors.ReqlDriverError:
    print('Check RethinkDB is running on port %s' % PORT)
    sys.exit()

UPDATE_INTERVAL = 1.0
