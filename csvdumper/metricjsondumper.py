from cor.api import CORModule
from .sensor_pb2 import SensorReading
import json


class MetricJsonDumper(CORModule):

	def sensor_reading(self, message):
		data = json.dumps(dict(message.values))
		path = "{}/{}:{}.json"
		with open(path.format(self.path, message.location, message.timestamp), 'w') as json_file:
			json_file.write(data)

	def __init__(self, path="~/dump", *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.path = path
		self.add_topic("SensorReading", self.sensor_reading)
		self.register_type("SensorReading", SensorReading)
