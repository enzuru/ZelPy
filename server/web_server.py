import miniupnpc
import http.server
import socketserver

Handler = http.server.SimpleHTTPRequestHandler
port = 8003
proto = 'TCP'
url = "0.0.0.0"

httpd = socketserver.TCPServer((url, port), Handler)
print("serving at port", port)

upnp = miniupnpc.UPnP()
upnp.discoverdelay = 10
upnp.discover()
upnp.selectigd()
upnp.addportmapping(
    port,
    proto,
    upnp.lanaddr,
    port,
    'HTTP',
    ''
)
print(upnp)
print(upnp.externalipaddress())
print(upnp.statusinfo(), upnp.connectiontype())

i = 0
while True:
        p = upnp.getgenericportmapping(i)
        if p==None:
                break
        print(i, p)
        (port, proto, (ihost,iport), desc, c, d, e) = p
        #print port, desc
        i = i + 1

print(upnp.getspecificportmapping(port, proto))
httpd.serve_forever()
