from cor.api import CORModule
from .sensor_pb2 import SensorReading
import http.client
import math


class InfluxCollector(CORModule):

	def sensor_reading(self, message):
		connection = http.client.HTTPConnection(self.server, self.port)
		connection.connect()
		metrics = dict(message.values)
		line = "{metric_name},location={location} value={metric_value}\n"
		body = ""
		for metric in metrics:
			val = metrics[metric]
			if math.isnan(val):
				val = 0
			body += line.format(metric_name=metric, location=message.location, metric_value=val)
		connection.request("POST", "/write?db=metrics", body)
		response = connection.getresponse()
		if response.status != 204:
			data = response.read()
			print(response.status, response.reason)
			print(data)
		connection.close()

	def __init__(self, server="127.0.0.1", port=8086, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.server = server
		self.port = port
		self.add_topic("SensorReading", self.sensor_reading)
		self.register_type("SensorReading", SensorReading)
