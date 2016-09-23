import rethinkdb as r
from twisted.internet.task import LoopingCall
from twisted.internet import reactor

from conf import UPDATE_INTERVAL

c = r.connect(host='localhost', port=28015)

def get_all_chat():
    rows = r.db('chat').table('log').run(c)
    for row in rows:
        print format_message(row)

def get_messages_since_interval():
    return r.db('chat').table('log').filter(
        lambda row: row['time'].during(
            r.now() - UPDATE_INTERVAL, r.now())).run(c)

def format_message(row):
    return '%s %s: %s' % (
        row.get('time').strftime('%H:%M:%S'),
        row.get('user'),
        row.get('message')
    )

def update_messages(interval):
    for message in get_messages_since_interval():
        print format_message(message)

def send_message(user, message):
    return r.db('chat').table('log').insert(
        [{'user': user, 'message': message, 'time': r.now()}]
    ).run(c)

get_all_chat()

lc = LoopingCall(update_messages, UPDATE_INTERVAL)
lc.start(UPDATE_INTERVAL)

reactor.run()
