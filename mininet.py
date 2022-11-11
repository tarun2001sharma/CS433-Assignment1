from mininet.cli import CLI
from mininet.link import TCLink
from mininet.topo import Topo
from mininet.node import OVSController, OVSBridge
from mininet.log import setLogLevel
from mininet.net import Mininet


def Initiate_network():

    topo = Create_topology()
    net = Mininet( topo=topo, controller=OVSController,switch=OVSBridge, link=TCLink)
    net.start()
    CLI(net)
    net.stop()

class Create_topology(Topo):

    def build( self, **_kwargs ):

        # Add hosts
        hostA = self.addHost('A', ip='33.0.0.0/8')
        hostB = self.addHost('B', ip='33.0.0.1/8')
        hostC = self.addHost('C', ip='33.0.0.2/8')
        hostD = self.addHost('D', ip='33.0.0.3/8')

        # switches
        sw1 = self.addSwitch('r1')
        sw2 = self.addSwitch('r2')

        bandwidth = 1000  #define bandwidth
        # delay_time = '1ms'   #define delay

        # links
        self.addLink(hostA, sw1, bw=bandwidth, delay='1ms', loss = 0)
        self.addLink(hostD, sw1, bw=bandwidth, delay='1ms', loss = 0)
        self.addLink(sw2, hostB, bw=bandwidth, delay='1ms', loss = 0)
        self.addLink(sw2, hostC, bw=bandwidth, delay='5ms', loss = 0)
        self.addLink(sw1, sw2, bw=500, delay='10ms', loss = 0)


if __name__ == '__main__':
    setLogLevel( 'info' )
    Initiate_network()
