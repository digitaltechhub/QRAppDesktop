# attributes of a lec can be used to populate course name and code drop downs

class Lecturer:
	def __init__(self, name, email, phone, courses):

		"""

		:param name: users name
		:param email: users email
		:param phone: users phone number
		:param courses: a dict mapping course names to course code for a unit taught by a lec
		"""

		self.Name = name
		self.Email = email
		self.Phone_number = phone
		self.courses_taught = courses
