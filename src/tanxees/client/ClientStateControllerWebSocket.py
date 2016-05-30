import websocket
import six
import threading
import time
import select
import traceback
import json

from tanxees.api.TheStateModel import TheStateModel

class PatchedWebSocketApp(websocket.WebSocketApp):
    def run_forever(self, sockopt=None, sslopt=None,
                    ping_interval=0, ping_timeout=None,
                    http_proxy_host=None, http_proxy_port=None,
                    http_no_proxy=None, http_proxy_auth=None,
                    skip_utf8_validation=False,
                    host=None, origin=None):
        """
        Patched version which handles more exceptions compared to original
        """

        if not ping_timeout or ping_timeout <= 0:
            ping_timeout = None
        if sockopt is None:
            sockopt = []
        if sslopt is None:
            sslopt = {}
        if self.sock:
            raise websocket.WebSocketException("socket is already opened")
        thread = None
        close_frame = None

        try:
            self.sock = websocket.WebSocket(self.get_mask_key,
                sockopt=sockopt, sslopt=sslopt,
                fire_cont_frame=self.on_cont_message and True or False,
                skip_utf8_validation=skip_utf8_validation)
            self.sock.settimeout(websocket.getdefaulttimeout())
            self.sock.connect(self.url, header=self.header, cookie=self.cookie,
                http_proxy_host=http_proxy_host,
                http_proxy_port=http_proxy_port,
                http_no_proxy=http_no_proxy, http_proxy_auth=http_proxy_auth,
                subprotocols=self.subprotocols,
                host=host, origin=origin)
            self._callback(self.on_open)

            if ping_interval:
                event = threading.Event()
                thread = threading.Thread(target=self._send_ping, args=(ping_interval, event))
                thread.setDaemon(True)
                thread.start()

            while self.sock.connected:
                r, w, e = select.select((self.sock.sock, ), (), (), ping_timeout)
                if not self.keep_running:
                    break
                if ping_timeout and self.last_ping_tm and time.time() - self.last_ping_tm > ping_timeout:
                    self.last_ping_tm = 0
                    raise websocket.WebSocketTimeoutException("ping timed out")

                if r:
                    op_code, frame = self.sock.recv_data_frame(True)
                    if op_code == websocket.ABNF.OPCODE_CLOSE:
                        close_frame = frame
                        break
                    elif op_code == websocket.ABNF.OPCODE_PING:
                        self._callback(self.on_ping, frame.data)
                    elif op_code == websocket.ABNF.OPCODE_PONG:
                        self._callback(self.on_pong, frame.data)
                    elif op_code == websocket.ABNF.OPCODE_CONT and self.on_cont_message:
                        self._callback(self.on_data, data, frame.opcode, frame.fin)
                        self._callback(self.on_cont_message, frame.data, frame.fin)
                    else:
                        data = frame.data
                        if six.PY3 and frame.opcode == websocket.ABNF.OPCODE_TEXT:
                            data = data.decode("utf-8")
                        self._callback(self.on_data, data, frame.opcode, True)
                        self._callback(self.on_message, data)
        except (Exception, KeyboardInterrupt, SystemExit) as e:
            self._callback(self.on_error, e)
            if isinstance(e, SystemExit):
                # propagate SystemExit further
                raise
        finally:
            if thread:
                event.set()
                thread.join()
                self.keep_running = False
            self.sock.close()
            self._callback(self.on_close,
                *self._get_close_args(close_frame.data if close_frame else None))
            self.sock = None

class ClientStateControllerWebSocket(object):
    def __init__(self, address, controller):
        self.ws = PatchedWebSocketApp(address, on_message=self.onMessage, on_error=self.onError,
                                 on_close=self.onClose)
        self.controller = controller

    def onMessage(self, ws, message):
        data = json.loads(message)
        theState = TheStateModel.handleJson(data)
        if self.controller.updateClientState(theState):
            self.ws.send(json.dumps(self.controller.clientState.toJson()))

    def onError(self, ws, error):
        if not isinstance(error, (SystemExit, KeyboardInterrupt)):
            traceback.print_exc()

    def onClose(self, ws):
        pass

    def run(self):
        self.ws.run_forever()
