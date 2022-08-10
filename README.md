### How to create a pure wsgi app with python in-built wsgiref module

There are 2 ways of running the app instance or app function 

* using `make_server` directly

        try:
            from wsgiref.simple_server import make_server
            httpd = make_server("",3333,app)
            print("serving on port 3333...")
            httpd.serve_forever()
        except KeyboardInterrupt:
            
            print("Goodbye!")

* using `make_server` with context

        with make_server("",3333,app) as httpd:
            httpd.serve_forever()
            print("server running at port 3333...")

