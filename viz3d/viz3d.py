from cor.api import CORModule, Message


class Viz3D(CORModule):

	def sensor_reading(self, message):
		print(message)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.add_topics({"SENSOR_READING": self.sensor_reading})