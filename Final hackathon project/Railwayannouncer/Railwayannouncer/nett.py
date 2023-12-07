import socket

def is_internet_available():
        try:
            # Try to connect to a well-known website (in this case, Google's DNS server)
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False