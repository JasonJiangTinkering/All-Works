import webapp2
import jinja2
import os

foods = {"recipe1":{"name":"Lemonade","ingredients":["125 mL Brown Sugar","250 mL Lemon Juice","1500 mL Water"]},
"recipe2":{"name":"Naan","ingredients":["2.5 mL Brown Sugar","80 mL Water","1.875 mL Active Dry Yeast","290 mL Flour","80 mL Plain Yogurt","10 mL Oil"]},
"recipe3":{"name":"Alfredo Sauce","ingredients":["40 mL Butter","5 mL Salt","2.5 mL Pepper","30 mL Flour","250 mL Milk","250 mL Parmesan Cheese"]}}

the_jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
extensions=['jinja2.ext.autoescape'],autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):  
        t = the_jinja_env.get_template('templates/index.html')
        self.response.write(t.render())
    
    def post(self):
        t = the_jinja_env.get_template('templates/results.html')
        choice = self.request.get('food')
      
        if foods.has_key(choice):
            self.response.write(t.render(foods[choice]))
        else:
            self.response.write(t.render(foods["recipe1"]))

routes = [('/',MainPage)]
app = webapp2.WSGIApplication(routes, debug=True)