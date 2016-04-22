from cor.api import Launcher
from influxcollector.influxcollector import InfluxCollector
from cor.comm import TCPSocketNetworkAdapter

collector = Launcher()
collector.launch_module(InfluxCollector, network_adapter=TCPSocketNetworkAdapter(hostport="0.0.0.0:6090"))
