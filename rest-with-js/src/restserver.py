from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import FileResponse

records = [
  {"id":1, "userId":1, "title":"hello", "body":"hellooooooo"},
  {"id":2, "userId":2, "title":"bye", "body":"sayonnara!"},
  {"id":3, "userId":3, "title":"why", "body":"why not?"},
  {"id":4, "userId":4, "title":"fly", "body":"yayyyyy!!!"},
]

def index_page(req):
  return FileResponse("index.html")

def get_post(req):
  idx = int(req.matchdict['post_id'])-1
  return records[idx]

if __name__ == '__main__':
  with Configurator() as config:
    config.add_route('home', '/')
    config.add_view(index_page, route_name='home')

    config.add_route('posts', '/posts/{post_id}')
    config.add_view(get_post, route_name='posts', renderer='json')

    config.add_static_view(name='/', path='./public', cache_max_age=3600)
    app = config.make_wsgi_app()

  server = make_server('0.0.0.0', 6543, app)
  print('Web server started on: http://0.0.0.0:6543')
  server.serve_forever()
