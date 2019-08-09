import webapp2
import jinja2
import os
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        #self.response.header['Content-Type'] = 'text/plain'
        self.response.write('<h1>Hello, World</h1>')

class secret(webapp2.RequestHandler):
    def get(self):
        self.response.write('Yo u found a secret page')

class colors(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/fav-colors.html')
        self.response.write(template.render())
app = webapp2.WSGIApplication([
    ('/', MainPage),('/secret', secret), ('/fav', colors)]
    , debug=True)

