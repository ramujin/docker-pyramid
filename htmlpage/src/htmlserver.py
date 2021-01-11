from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse

def hello_world(req):
  return FileResponse("hello.html")

if __name__ == '__main__':
  with Configurator() as config:
    config.add_route('hello', '/')
    config.add_view(hello_world, route_name='hello')
    config.add_static_view(name='/', path='./public', cache_max_age=3600)
    app = config.make_wsgi_app()

  server = make_server('0.0.0.0', 6543, app)
  print('Web server started on: http://0.0.0.0:6543')
  server.serve_forever()
