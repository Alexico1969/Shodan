# Shodan

I'm getting a weird error : 

Internal Server Error

Then when I check the logs it says : 

2020-03-26 21:47:58,482: Exception on / [POST]
Traceback (most recent call last):
  File "/home/AxelFF/mysite/flask_app.py", line 37, in hello_world
    print('')
BlockingIOError: [Errno 11] write could not complete without blocking
**NO MATCH**
During handling of the above exception, another exception occurred:
**NO MATCH**
Traceback (most recent call last):
  File "/usr/lib/python3.8/site-packages/flask/app.py", line 2446, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3.8/site-packages/flask/app.py", line 1951, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3.8/site-packages/flask/app.py", line 1820, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "/usr/lib/python3.8/site-packages/flask/_compat.py", line 39, in reraise
    raise value
  File "/usr/lib/python3.8/site-packages/flask/app.py", line 1949, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3.8/site-packages/flask/app.py", line 1935, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "/home/AxelFF/mysite/flask_app.py", line 39, in hello_world
    print("Error")
BlockingIOError: [Errno 11] write could not complete without blocking

What do ? 
