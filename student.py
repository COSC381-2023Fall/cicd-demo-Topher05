from course import courses, Course


class Student:
	def __init__(self,IED,name):
		self._IED = IED
		self._name = name
		self.stdCourses = []

	def addCourse(self, course):
		if course in courses:
			self.stdCourses.append(course)

	
stdCourses= []
stds = {}