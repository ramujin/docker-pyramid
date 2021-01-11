from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response # instead of FileResponse, we now render the template into a response!

def hello_world_template(req):
  data = {'message': 'Greetings!'}
  return render_to_response('hello.html', data, request=req)

if __name__ == '__main__':
  with Configurator() as config:
    # to use Jinja2 to render the template!
    config.include('pyramid_jinja2')
    config.add_jinja2_renderer('.html')

    config.add_route('template_hello', '/')
    config.add_view(hello_world_template, route_name='template_hello')

    config.add_static_view(name='/', path='./public', cache_max_age=3600)
    app = config.make_wsgi_app()

  server = make_server('0.0.0.0', 6543, app)
  print('Web server started on: http://0.0.0.0:6543')
  server.serve_forever()
