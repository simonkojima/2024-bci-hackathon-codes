import pythonosc.dispatcher
import pythonosc.osc_server

def function_for_handling_filter(addr, args):
    print("filter", addr, args)

def function_for_handling_default(addr, args):
    print("Default", addr, args)

ip = "127.0.0.1"
port = 7400

dispatcher = pythonosc.dispatcher.Dispatcher()
dispatcher.map("/filter", function_for_handling_filter)
dispatcher.set_default_handler(function_for_handling_default)

server = pythonosc.osc_server.ThreadingOSCUDPServer((ip, port), dispatcher)
server.serve_forever()