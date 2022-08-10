

def app(environ,response:callable):
    status = "200 OK"
    headers = [
        ("Content-Type","text/html")
    ]
    response(
        status,
        headers
    )

    response_byte = "Hello, World !".encode()

    return [response_byte]


if __name__ == "__main__":
    """
    you can run the server by using this to method
    """
    try:
        from wsgiref.simple_server import make_server
        httpd = make_server("",3333,app)
        print("serving on port 3333...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        
        print("Goodbye!")
    
