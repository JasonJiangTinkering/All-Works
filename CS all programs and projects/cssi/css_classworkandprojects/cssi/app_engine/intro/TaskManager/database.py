from app_models import Student, Group, Task, Organizer 

def seed_data():
	students = []

	students.append(Student(fname="Adam",lname="Thomas").put())
	students.append(Student(fname="Alyssa",lname="Roach").put())
	students.append(Student(fname="Andrew",lname="Charles").put())
	students.append(Student(fname="Bencarthur",lname="Noel").put())
	students.append(Student(fname="Chrishaun",lname="Inniss").put())
	students.append(Student(fname="Cody",lname="Ramsey").put())
	students.append(Student(fname="Daniel",lname="St. Vincent").put())
	students.append(Student(fname="Darren",lname="Zou").put())
	students.append(Student(fname="Janelle",lname="Piedrahita").put())
	students.append(Student(fname="Jason",lname="Jiang").put())
	students.append(Student(fname="Joshua",lname="Yates").put())
	students.append(Student(fname="Kevin",lname="Benfield").put())
	students.append(Student(fname="Mariama",lname="Drame").put())
	students.append(Student(fname="Marron",lname="St. Marthe").put())
	students.append(Student(fname="Michael",lname="Casey").put())
	students.append(Student(fname="Michael",lname="McIntosh").put())
	students.append(Student(fname="Oghenetare",lname="Ikie").put())
	students.append(Student(fname="Rashique",lname="Minott").put())
	students.append(Student(fname="Samuel",lname="James").put())
	students.append(Student(fname="Sean",lname="Wilson-Bynoe").put())
	students.append(Student(fname="Shamar",lname="Samuels").put())
	students.append(Student(fname="Sophia",lname="Lorraine Bailey").put())
	students.append(Student(fname="Stephanie",lname="Fuentes").put())
	
	alpha_team = Group(name="Alpha",project="Keep Kalm")
	beta_team = Group(name="Beta",project="Rate My Foster")
	gamma_team = Group(name="Gamma",project="1K Pic Mosaic")
	delta_team = Group(name="Delta",project="Lottery Generator")
	zeta_team = Group(name="Zeta",project="Keeping Green")
	theta_team = Group(name="Theta",project="I Declare War")
	omega_team = Group(name="Omega",project="Major Clarifier")

	task_key = Task(info="Finish Fortune Teller Lab").put()

	for i in range(len(students)):
		Organizer(student=students[i],task=task_key,priority=1,completed=False).put()
	
	alpha_team.students.append(students[11])
	alpha_team.students.append(students[21])
	alpha_team.students.append(students[13])

	beta_team.students.append(students[20])
	beta_team.students.append(students[16])
	beta_team.students.append(students[8])

	gamma_team.students.append(students[6])
	gamma_team.students.append(students[7])
	gamma_team.students.append(students[12])

	delta_team.students.append(students[3])
	delta_team.students.append(students[14])
	delta_team.students.append(students[22])
	delta_team.students.append(students[2])

	zeta_team.students.append(students[19])
	zeta_team.students.append(students[15])
	zeta_team.students.append(students[17])
	
	theta_team.students.append(students[0])
	theta_team.students.append(students[9])
	theta_team.students.append(students[10])

	omega_team.students.append(students[1])
	omega_team.students.append(students[5])
	omega_team.students.append(students[18])
	omega_team.students.append(students[4])

	alpha_team.put()
	beta_team.put()
	gamma_team.put()
	delta_team.put()
	zeta_team.put()
	theta_team.put()
	omega_team.put()
	
	
	
	
	
	


	





