import socket

# Define the host and port to listen on
HOST, PORT = '127.0.0.1', 8080


def handle_root(request_method,path,request_path):        
    # Construct a simple HTTP response
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        "\r\n"
        f"<html><body><p>method: {request_method}  </p>"
        f"<p> requested path: {request_path} </p> </body></html>"
        f"{path}"
        ) 
    return http_response

def handle_about(request_method,path,request_path):        
    # Construct a simple HTTP response
    http_response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        "\r\n"
        "<html><body> <h1> ABOUT </h1>"
        f"<p>method: {request_method}  </p>"
        f"<p> requested path: {request_path} </p> </body></html>"
        f"{path}"
        ) 
    return http_response

def handle_error():        
    # Construct a simple HTTP response
    http_response = (
        "HTTP/1.1 404 NOT FOUND\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        "\r\n"
        "<html><body> ERROR 404 NOT FOUND </html>"
        ) 
    return http_response

# Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    # Allow immediate reuse of address after program exit
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Serving HTTP on {HOST} port {PORT} ...")

    while True:
        # Accept a new client connection
        client_connection, client_address = server_socket.accept()
        with client_connection:
            # Receive the request data (limit to 1024 bytes for simplicity)
            request_data = client_connection.recv(1024).decode('utf-8')
            print("Received request:")
            print(request_data)

            request_method = request_data.split('\n', 1)[0]
            request_path = request_data.split('\n', 2)[1]
            path = request_method.split()[1]
            if path == "/":
                http_response = handle_root(request_method,path,request_path)
            if path == "/about":
                http_response = handle_about(request_method,path,request_path)
            if path != "/":
                http_response = handle_error()
                 
            # Send the HTTP response back to the client
            client_connection.sendall(http_response.encode('utf-8'))   