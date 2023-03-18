#!/usr/bin/env python3

#don't forget to set your environment variables

#web browsers cannot execute Python code. 
#Flask translates http requests into python objects and python objects into http responses. 

#Application and Request Contexts
    # When flask gets a request from the browser, it passes specific objects to the route's view function. One object that gets passed is the request object. The view function doesn't automatically have access to this object but can do so through CONTEXTS. 

    #request context
        #request is a global variable that comes with the Flask framework that provides an unchanging set of information

        #to do this, Flask generates a CONTEXT for requests after receiving a request and before the application runs. Thus, when request is called, we're provided with all of the request data without having to do any configuration

        #TLDR: Flask generates a context for requests that gives us access to a request's data

        #To generate a request context manually, run these two commands
            #from app import app
            #from flask import request

            #request_context = app.test_request_context()
            #request_context.push()

        #if you are in a debugging shell, use request_context.pop() to clear the request_context object before moving onto a new request

    #application context
        #Similar to request context, Flask also has application context
        #basically when a request is received, Flask generates the application context, providing us with application data we can access.

        #to access the data, you'll use flask.current_app

    #other contexts
        #g is an object that can be used to store anything that you want to store globally for the lifetime of a request. It is reset with each new request.
        #session is a dictionary object that can be used to hold onto values between multiple requests.

#The URL Map
    # The URL Map is just a dictionary that maps URLs to the views that are served to the client
    # Everytime you use @app.route, you add a new key/value to the URL map

    # To view the URL map, use app.url_map


from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    host = request.headers.get('Host')
    return f'<h1>The host for this page is {host}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
