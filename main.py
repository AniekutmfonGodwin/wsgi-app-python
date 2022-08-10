from wsgiref.simple_server import make_server


PORT = 3333



class Application(object):
    """creating wsgi app using class

    Args:
        object (_type_): _description_
    """
    def __call__(self,environ,response:callable):
        
        PATH_INFO = environ["PATH_INFO"]


        if PATH_INFO == "/hello":
            return self.hello

        


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

    def hello(self,environ,response):
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


    def goodbye(self,environ,response):
        status = "200 OK"
        headers = [
            ("Content-Type","text/html")
        ]
        response(
            status,
            headers
        )

        response_byte = "Good bye!".encode()

        return [response_byte]

    def notfound(self,environ,response):
        status = '404 Not Found'
        headers = [
            ("Content-Type","text/html")
        ]
        response(
            status,
            headers
        )

        response_byte = "Not found".encode()

        return [response_byte]

    

def app(environ,response:callable):
    # print("environ ",environ)
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

start_message = "server running on port {port}\nvisit link to view pages\n\n http://localhost:{port}\n\n".format(port=PORT)

if __name__ == "__main__":
    """
    you can run the server by using this to method
    """
    # try:
    #     httpd = make_server("",PORT,app)
    #     print(start_message)
    #     httpd.serve_forever()
    # except KeyboardInterrupt:
    #     print("Goodbye!")
        
    
    with make_server("",PORT,Application()) as httpd:
        print(start_message)
        httpd.serve_forever()
    
    
