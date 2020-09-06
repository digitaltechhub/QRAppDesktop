# class below implements a course at a school

class Course:
	def __init__(self, name, code, start, stop, time):
		"""

		:param name: name of the course
		:param code: course code
		:param start: time lesson begins
		:param stop: time lesson stops
		:param time: duration of the lesson
		"""
		self.Name = name
		self.Code = code
		self.start_time = start
		self.duration = time
		self.stop_time = stop
		self.Qr_code = None
