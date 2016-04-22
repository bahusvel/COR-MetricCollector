from cor.api import Launcher
from collectd.collectd import Collectd
from cor.comm import TCPSocketNetworkAdapter
from subprocess import Popen
import sys

if __name__ == "__main__":
	if len(sys.argv) < 2:
		raise Exception("Usage: python3 sensor.py (location)")
	p = Popen(["collectd", "-C", "./collectd/collectd.conf", "-f"])
	sensor = Launcher()
	sensor.launch_module(Collectd, network_adapter=TCPSocketNetworkAdapter(hostport="127.0.0.1:6091"), location=sys.argv[1])
	sensor.link_external("SensorReading", "192.168.2.132:6090")

