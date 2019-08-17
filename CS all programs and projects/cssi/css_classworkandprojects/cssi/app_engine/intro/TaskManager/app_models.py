from google.appengine.ext import ndb

class Student(ndb.Model):
	fname = ndb.StringProperty(required=True)
	lname = ndb.StringProperty(required=True)

class Group(ndb.Model):
	name = ndb.StringProperty(required=False, default="CSSI-X Team")
	project = ndb.StringProperty(required=False)
	students = ndb.KeyProperty(Student,repeated=True)

class Task(ndb.Model):
	info = ndb.StringProperty(required=True)
	

class Organizer(ndb.Model):
	student = ndb.KeyProperty(Student,required=True)
	task = ndb.KeyProperty(Task,required=True)
	priority = ndb.IntegerProperty(default=0)
	completed = ndb.BooleanProperty(default=False)
	
