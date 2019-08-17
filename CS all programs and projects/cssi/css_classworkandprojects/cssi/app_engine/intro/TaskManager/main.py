import webapp2
import os
import jinja2
from app_models import Student, Task, Group, Organizer
from database import seed_data

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def GetInfo(entity):
    info = {}
    info["key"] = entity.key

    if entity.completed:
        info["state"] = "completed"
    else:
        info["state"] = "notcompleted"
    
    if entity.priority == 0:
        info["difficulty"] = "easy"
    elif entity.priority == 1:
        info["difficulty"] = "middle"
    else:
        info["difficulty"] = "hard"
    
    student = Student.query(Student.key == entity.student).fetch(1)[0]

    info["name"] = student.fname + " " + student.lname

    task = Task.query(Task.key == entity.task).fetch(1)[0]

    info["task"] = task.info;

    group = Group.query(Group.students.IN([entity.student])).fetch(1)[0].name

    info["group"] = group

    return info

def GetTask():
    tasks = Organizer.query().fetch()
    values = {"entities":[]}

    for i in tasks:
        values["entities"].append(GetInfo(i))

    return values

def GetNames():
    students = Student.query().order(Student.fname).fetch()
    names = []

    for i in students:
        names.append(i.fname + " " + i.lname)
    
    return names

class MainPage(webapp2.RequestHandler):
    def get(self):
        t = the_jinja_env.get_template('/templates/index.html')
        data = GetTask()
        data["names"] = GetNames()

        self.response.write(t.render(data))

class LoadPage(webapp2.RequestHandler):
    def get(self):
        seed_data()
        t = the_jinja_env.get_template('/templates/loader.html')
        self.response.write(t.render())

routes = [('/',MainPage),('/load',LoadPage)]
app = webapp2.WSGIApplication(routes, debug=True)
