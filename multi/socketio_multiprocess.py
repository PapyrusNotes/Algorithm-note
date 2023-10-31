import socketio
from flask import Flask

from multiprocessing import Process, Queue, current_process
import threading

import random
import os
import time


def sio_client(id1, id2):
    process_id = os.getpid()
    process_name = current_process().name
    connected = False

    print(f'args : {id1}, {id2}')

    sio = socketio.SimpleClient()
    print('sio client established on sio_client ')

    # connect to a Socket.IO server for detection streaming
    while not connected:
        try:
            sio.connect('http://127.0.0.1:5000/', transports=['websocket'])
            print('connected to server')
            connected = True
        except Exception as ex:
            print("Client process failed to establish initial connection to server : ", type(ex).__name__)
            time.sleep(2)

    while True:
        try:
            event = sio.receive()
            print(print(f'received event: "{event[0]}" with arguments {event[1:]}'))
        except KeyboardInterrupt:
            return 0


def get_detection(arg1, sio, mq):

    while True:
        msg = mq.get()
        sio.emit('detection', {'_code': 'foo',
                               'class': msg,
                               'timestamp': 'time_foo',
                               'name': 'file foo'})
        print(f'sio emitted {msg}')
        time.sleep(1)


def sio_server(id1, id2, sio_mq):
    process_id = os.getpid()
    process_name = current_process().name
    print(f'args : {id1}, {id2}')

    sio = socketio.Server(async_mode='threading')
    app = Flask(__name__)

    @sio.event
    def connect(sid, environ, auth):
        print('[INFO] Connected to client', sid)

    @sio.event
    def disconnect(sid):
        print('disconnected ', sid)

    print('Flask app is initialized on sio_server ')

    detection_worker = threading.Thread(target=get_detection, args=(1, sio, sio_mq))
    detection_worker.daemon = True
    detection_worker.start()

    # create a Socket.IO server for detection streaming
    app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
    app.run(host="0.0.0.0", port=5000)
    # middleware_app = socketio.Middleware(sio, app)
    # eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), middleware_app)


def background_job(_min, _max):
    while True:
        try:
            print(f'Value from main process background thread {random.randrange(_min, _max)}')
            time.sleep(1)
        except KeyboardInterrupt:
            break


def main():
    """
    main() has 2 task after creating 2 sio servers.
        - Produce resource for server
        - Calculate something

    when KeyboardInterrupted, main() closes 2 sio servers.
    """

    main_process_id = os.getpid()
    print(f'Main process Id{main_process_id}')

    sio_mq = Queue()
    # socket-io server (index:2) sends resource
    server = Process(name='sio_server', target=sio_server, args=(2, 200, sio_mq))
    # socket-io client (index:1) receives resource
    client = Process(name='sio_client', target=sio_client, args=(1, 100))
    server.start()
    time.sleep(2)
    client.start()

    detection_worker = threading.Thread(target=background_job, args=(1, 100))
    detection_worker.daemon = True
    detection_worker.start()

    while True:
        try:
            msg = random.randrange(1, 100)
            sio_mq.put(msg)
        except KeyboardInterrupt:
            server.close()
            print('sio_server closed')
            client.close()
            print('sio_client closed')
            server.terminate()
            client.terminate()
            break


if __name__ == '__main__':
    main()
