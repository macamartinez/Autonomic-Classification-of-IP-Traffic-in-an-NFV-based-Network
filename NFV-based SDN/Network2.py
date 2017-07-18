#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():

    NODE1_IP='192.168.0.114'
    CONTROLLER_IP='192.168.0.112'

    net = Mininet( topo=None,
                   build=False)

    net.addController( 'c0',
                      controller=RemoteController,
                      ip=CONTROLLER_IP,
                      port=6633)

     
    h114 = net.addHost('h114', ip='10.0.1.114' )
    h110 = net.addHost('h110', ip='10.0.1.110' )
    h99 = net.addHost('h99', ip='10.0.1.99' )
    h78 = net.addHost('h78', ip='10.0.1.78' )
    h79 = net.addHost('h79', ip='10.0.1.79' )
    h87 = net.addHost('h87', ip='10.0.1.87' )
    h69 = net.addHost('h69', ip='10.0.1.69' )
    h105 = net.addHost('h105', ip='10.0.1.105' )
    h95 = net.addHost('h95', ip='10.0.1.95' )
    h88 = net.addHost('h88', ip='10.0.1.88' )
    h126 = net.addHost('h126', ip='10.0.1.126' )
    h100 = net.addHost('h100', ip='10.0.1.100' )
    h117 = net.addHost('h117', ip='10.0.1.117' )
    h109 = net.addHost('h109', ip='10.0.1.109' )
    h112 = net.addHost('h112', ip='10.0.1.112' )
    h80 = net.addHost('h80', ip='10.0.1.80' )
    h124 = net.addHost('h124', ip='10.0.1.124' )
    h70 = net.addHost('h70', ip='10.0.1.70' )
    h92 = net.addHost('h92', ip='10.0.1.92' )
    h123 = net.addHost('h123', ip='10.0.1.123' )
    h122 = net.addHost('h122', ip='10.0.1.122' )
    h102 = net.addHost('h102', ip='10.0.1.102' )
    h81 = net.addHost('h81', ip='10.0.1.81' )
    h71 = net.addHost('h71', ip='10.0.1.71' )
    h97 = net.addHost('h97', ip='10.0.1.97' )
    h65 = net.addHost('h65', ip='10.0.1.65' )
    h93 = net.addHost('h93', ip='10.0.1.93' )
    h121 = net.addHost('h121', ip='10.0.1.121' )
    h104 = net.addHost('h104', ip='10.0.1.104' )
    h72 = net.addHost('h72', ip='10.0.1.72' )
    h120 = net.addHost('h120', ip='10.0.1.120' )
    h91 = net.addHost('h91', ip='10.0.1.91' )
    h82 = net.addHost('h82', ip='10.0.1.82' )
    h90 = net.addHost('h90', ip='10.0.1.90' )
    h94 = net.addHost('h94', ip='10.0.1.94' )
    h73 = net.addHost('h73', ip='10.0.1.73' )
    h106 = net.addHost('h106', ip='10.0.1.106' )
    h74 = net.addHost('h74', ip='10.0.1.74' )
    h116 = net.addHost('h116', ip='10.0.1.116' )
    h83 = net.addHost('h83', ip='10.0.1.83' )
    h115 = net.addHost('h115', ip='10.0.1.115' )
    h89 = net.addHost('h89', ip='10.0.1.89' )
    h125 = net.addHost('h125', ip='10.0.1.125' )
    h84 = net.addHost('h84', ip='10.0.1.84' )
    h101 = net.addHost('h101', ip='10.0.1.101' )
    h107 = net.addHost('h107', ip='10.0.1.107' )
    h119 = net.addHost('h119', ip='10.0.1.119' )
    h96 = net.addHost('h96', ip='10.0.1.96' )
    h75 = net.addHost('h75', ip='10.0.1.75' )
    h66 = net.addHost('h66', ip='10.0.1.66' )
    h85 = net.addHost('h85', ip='10.0.1.85' )
    h108 = net.addHost('h108', ip='10.0.1.108' )
    h127 = net.addHost('h127', ip='10.0.1.127' )
    h98 = net.addHost('h98', ip='10.0.1.98' )
    h118 = net.addHost('h118', ip='10.0.1.118' )
    h76 = net.addHost('h76', ip='10.0.1.76' )
    h128 = net.addHost('h128', ip='10.0.1.128' )
    h111 = net.addHost('h111', ip='10.0.1.111' )
    h86 = net.addHost('h86', ip='10.0.1.86' )
    h67 = net.addHost('h67', ip='10.0.1.67' )
    h77 = net.addHost('h77', ip='10.0.1.77' )
    h103 = net.addHost('h103', ip='10.0.1.103' )
    h68 = net.addHost('h68', ip='10.0.1.68' )
    h113 = net.addHost('h113', ip='10.0.1.113' )

    s31 = net.addSwitch('s31')
    s25 = net.addSwitch('s25')
    s28 = net.addSwitch('s28')
    s42 = net.addSwitch('s42')
    s22 = net.addSwitch('s22')
    s29 = net.addSwitch('s29')
    s23 = net.addSwitch('s23')
    s32 = net.addSwitch('s32')
    s33 = net.addSwitch('s33')
    s35 = net.addSwitch('s35')
    s26 = net.addSwitch('s26')
    s27 = net.addSwitch('s27')
    s37 = net.addSwitch('s37')
    s34 = net.addSwitch('s34')
    s40 = net.addSwitch('s40')
    s41 = net.addSwitch('s41')
    s30 = net.addSwitch('s30')
    s38 = net.addSwitch('s38')
    s39 = net.addSwitch('s39')
    s24 = net.addSwitch('s24')
    s36 = net.addSwitch('s36')

    net.addLink(s31, h83)
    net.addLink(s31, h84)
    net.addLink(s32, h85)
    net.addLink(s32, h86)
    net.addLink(s32, h87)
    net.addLink(s32, h88)
    net.addLink(s33, h89)
    net.addLink(s33, h90)
    net.addLink(s33, h91)
    net.addLink(s33, h92)
    net.addLink(s34, h93)
    net.addLink(s34, h94)
    net.addLink(s34, h95)
    net.addLink(s34, h96)
    net.addLink(s35, h97)
    net.addLink(s35, h98)
    net.addLink(s35, h99)
    net.addLink(s35, h100)
    net.addLink(s36, h101)
    net.addLink(s36, h102)
    net.addLink(s36, h103)
    net.addLink(s36, h104)
    net.addLink(s37, h105)
    net.addLink(s37, h106)
    net.addLink(s37, h107)
    net.addLink(s37, h108)
    net.addLink(s38, h109)
    net.addLink(s38, h110)
    net.addLink(s38, h111)
    net.addLink(s38, h112)
    net.addLink(s39, h113)
    net.addLink(s39, h114)
    net.addLink(s39, h115)
    net.addLink(s39, h116)
    net.addLink(s40, h117)
    net.addLink(s40, h118)
    net.addLink(s40, h119)
    net.addLink(s40, h120)
    net.addLink(s41, h121)
    net.addLink(s41, h122)
    net.addLink(s41, h123)
    net.addLink(s41, h124)
    net.addLink(s42, h125)
    net.addLink(s42, h126)
    net.addLink(s42, h127)
    net.addLink(s42, h128)
    net.addLink(s23, s22)
    net.addLink(s22, s24)
    net.addLink(s22, s25)
    net.addLink(s22, s26)
    net.addLink(s23, s27)
    net.addLink(s23, s28)
    net.addLink(s23, s29)
    net.addLink(s23, s30)
    net.addLink(s24, s31)
    net.addLink(s24, s32)
    net.addLink(s24, s33)
    net.addLink(s24, s34)
    net.addLink(s25, s35)
    net.addLink(s25, s36)
    net.addLink(s25, s37)
    net.addLink(s25, s38)
    net.addLink(s26, s39)
    net.addLink(s26, s40)
    net.addLink(s26, s41)
    net.addLink(s26, s42)
    net.addLink(s27, h65)
    net.addLink(s27, h66)
    net.addLink(s27, h67)
    net.addLink(s27, h68)
    net.addLink(s28, h69)
    net.addLink(s28, h70)
    net.addLink(s28, h71)
    net.addLink(s28, h72)
    net.addLink(s29, h74)
    net.addLink(s29, h73)
    net.addLink(s29, h75)
    net.addLink(s29, h76)
    net.addLink(s30, h77)
    net.addLink(s30, h78)
    net.addLink(s30, h79)
    net.addLink(s30, h80)
    net.addLink(s31, h81)
    net.addLink(s31, h82)    
    net.start()

    # Configure the GRE tunnel
    s22.cmd('ovs-vsctl add-port s22 s22-gre1 -- set interface s22-gre1 type=gre options:remote_ip='+NODE1_IP)
    s23.cmd('ovs-vsctl add-port s23 s23-gre1 -- set interface s23-gre1 type=gre options:remote_ip='+NODE1_IP)
    s24.cmd('ovs-vsctl add-port s24 s24-gre1 -- set interface s24-gre1 type=gre options:remote_ip='+NODE1_IP)
    s25.cmd('ovs-vsctl add-port s25 s25-gre1 -- set interface s25-gre1 type=gre options:remote_ip='+NODE1_IP)
    s26.cmd('ovs-vsctl add-port s26 s26-gre1 -- set interface s26-gre1 type=gre options:remote_ip='+NODE1_IP)
    s27.cmd('ovs-vsctl add-port s27 s27-gre1 -- set interface s27-gre1 type=gre options:remote_ip='+NODE1_IP)
    s28.cmd('ovs-vsctl add-port s28 s28-gre1 -- set interface s28-gre1 type=gre options:remote_ip='+NODE1_IP)
    s29.cmd('ovs-vsctl add-port s29 s29-gre1 -- set interface s29-gre1 type=gre options:remote_ip='+NODE1_IP)
    s30.cmd('ovs-vsctl add-port s30 s30-gre1 -- set interface s30-gre1 type=gre options:remote_ip='+NODE1_IP)
    s31.cmd('ovs-vsctl add-port s31 s31-gre1 -- set interface s31-gre1 type=gre options:remote_ip='+NODE1_IP)
    s32.cmd('ovs-vsctl add-port s32 s32-gre1 -- set interface s32-gre1 type=gre options:remote_ip='+NODE1_IP)
    s33.cmd('ovs-vsctl add-port s33 s33-gre1 -- set interface s33-gre1 type=gre options:remote_ip='+NODE1_IP)
    s34.cmd('ovs-vsctl add-port s34 s34-gre1 -- set interface s34-gre1 type=gre options:remote_ip='+NODE1_IP)
    s35.cmd('ovs-vsctl add-port s35 s35-gre1 -- set interface s35-gre1 type=gre options:remote_ip='+NODE1_IP)
    s36.cmd('ovs-vsctl add-port s36 s36-gre1 -- set interface s36-gre1 type=gre options:remote_ip='+NODE1_IP)
    s37.cmd('ovs-vsctl add-port s37 s37-gre1 -- set interface s37-gre1 type=gre options:remote_ip='+NODE1_IP)
    s38.cmd('ovs-vsctl add-port s38 s38-gre1 -- set interface s38-gre1 type=gre options:remote_ip='+NODE1_IP)
    s39.cmd('ovs-vsctl add-port s39 s39-gre1 -- set interface s39-gre1 type=gre options:remote_ip='+NODE1_IP)
    s40.cmd('ovs-vsctl add-port s40 s40-gre1 -- set interface s40-gre1 type=gre options:remote_ip='+NODE1_IP)
    s41.cmd('ovs-vsctl add-port s41 s41-gre1 -- set interface s41-gre1 type=gre options:remote_ip='+NODE1_IP)
    s42.cmd('ovs-vsctl add-port s42 s42-gre1 -- set interface s42-gre1 type=gre options:remote_ip='+NODE1_IP)
    s42.cmdPrint('ovs-vsctl show')
    
     CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()
