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
        template = the_jinja_env.get_template('templates/memegen.html')
        replace = {'test' : " ",'pic' : " "}
        self.response.write(template.render(replace))

    def post(self):
        getttext = self.request.get('memename')
        getmeme = self.request.get('pics')
        final = 0
       # drake = "False"
        finaltext = getttext
        if getmeme == 'meme1':
            final = "https://i.imgflip.com/2/1ur9b0.jpg"
        if getmeme == 'meme2':
            final = "https://i.imgflip.com/2/30b1gx.jpg"
       #     drake = True
        #    finaltext = getttext.split('^')

        template = the_jinja_env.get_template('templates/memegen.html')
        #, 'drake' : drake
        replace = {'test': finaltext, 'pic' : final}
        self.response.write(template.render(replace))

class data(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template("template/memegen.html")
        self.response.write(template.render(testing))

class secret(webapp2.RequestHandler):
    def get(self):
        self.response.write('Yo u found a secret page')

class colors(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('templates/fav-colors.html')
        testing = {"title" :"title", "item1":"blue","item2":"red","item3":"green","item4":"purple"}
        self.response.write(template.render(testing))

app = webapp2.WSGIApplication([
    ('/', MainPage),('/secret', secret),('/data',data), ('/fav', colors)]
    , debug=True)

