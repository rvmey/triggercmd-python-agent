from .sails_websocket import SailsWebsocket
import time

def on_error(ws, error):
    print('Error: ' + str(error))
    print("Still trying to connect.")

def connect(computer_id, token, function):
    def on_connect(ws):
        print('Connected')
        ws.send('get', '/api/computer/subscribeToFunRoom?roomName=' + computer_id, {"Authorization": "Bearer " + token},{"message":"nothing"})

    def on_message(ws, message):
        function(message)

    triggercmd_address = "https://www.triggercmd.com"
    ws = SailsWebsocket(triggercmd_address + '/socket.io')
    ws.on_connect = on_connect
    ws.on_error = on_error
    ws.on_message = on_message
    while True:
        try:
            ws.run_forever()
        except Exception as e:
            print(str(e))
        time.sleep(5)
