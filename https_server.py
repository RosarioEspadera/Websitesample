import http.server
import ssl

# Define the server address and port
server_address = ('0.0.0.0', 4443)

# Custom handler to serve index.html and disable directory listing
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"  # Serve index.html as the default page
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def list_directory(self, path):
        self.send_error(403, "Directory listing is forbidden")
        return None

# Create an HTTP server
httpd = http.server.HTTPServer(server_address, CustomHandler)

# Create an SSL context
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="selfsigned.crt", keyfile="selfsigned.key")

# Wrap the server with SSL
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

print("Serving on https://127.0.0.1:4443")
httpd.serve_forever()