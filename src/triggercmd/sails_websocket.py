#!/usr/bin/env python
import websocket
import requests
import _thread
import time
import json

websocket.setdefaulttimeout(10)

class SailsWebsocket:
    sails_version = "0.11.0"

    def __init__(self, socket_io_url):
        self.connection_state = 0
        self.ping_interval = 60000
        self.__can_send_ping = False
        self.website_url = socket_io_url + '/?__sails_io_sdk_version=' + self.sails_version + '&transport=polling'
        ws_socket_io_url = socket_io_url.replace("http", "ws")
        self.base_website_socket = ws_socket_io_url + '/?__sails_io_sdk_version=' + self.sails_version + '&transport=websocket&sid='
        self.website_socket = None
        self.__ws = None

    def __get_sid(self, s):
        first = '"sid":"'
        last = '"'
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]

    def __get_ping_interval(self, s):
        first = '"pingInterval":'
        last = ','
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return int(s[start:end])

    def __send_ping(self):
        while self.__can_send_ping:
            self.__ws.send('22')
            time.sleep(self.ping_interval/1000)

    def __open(self, ws):
        ws.send('52')
        self.connection_state = 1
    
    def __error(self, ws, error):
        self.on_error(self, error)

    def __message(self, ws, message):
        if (self.connection_state == 1) and (message == '40'):
            self.__can_send_ping = True
            _thread.start_new_thread(self.__send_ping, ())
            self.connection_state = 2
            self.on_connect(self)
        elif (self.connection_state == 2) and (message != '3'):
            decripted_message = self.__decriptMessage(message)
            self.on_message(self, decripted_message)
        elif (self.connection_state == 1) and (message != '3'):
            self.stop()
            self.on_error(self, 'Connection failed')

    def __decriptMessage(self, message):
        return message[13:len(message)-1]

    def run_forever(self):
        r = requests.get(self.website_url, headers={"__sails_io_sdk_version":self.sails_version})
        params = r.text
        sid = self.__get_sid(params)
        self.website_socket = self.base_website_socket + sid
        self.ping_interval = self.__get_ping_interval(params)
        self.__ws = websocket.WebSocketApp(self.website_socket)
        self.__ws.on_open = self.__open
        self.__ws.on_error = self.__error
        self.__ws.on_message = self.__message
        self.__ws.run_forever()

    def stop(self):
        self.__can_send_ping = False
        self.__ws.close()

    def send(self, method, domain, headers, message):
        json_header = json.dumps(headers)
        json_message = json.dumps(message)
        self.__ws.send('42["' + method + '", {"url":"' + domain + "&__sails_io_sdk_version=" + self.sails_version + '", "headers":' + json_header + ', "data":' + json_message + '}]')
    
    def on_connect(self, ws):
        print('connected to triggercmd')

    def on_error(self, ws, error):
        print(error)

    def on_message(self, ws, message):
        print(message)

