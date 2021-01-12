#Importing the Unittest libary
import unittest

#Omporting the 'main' module that we awnt to test  
import ipv4_subnetmasks_prefixes as addresses

class Test_IPv4Addres(unittest.TestCase):

    #Testing if the subnet mask and the prefix are correct
    def test_get_prefix(self):
        submask = '255.255.255.240'
        prefix = '/28'
        self.assertEqual(addresses.get_net_prefix(submask), prefix)

    #Testing if the prefix (CIDR) and the subnet mask are correct 
    def test_netmask(self):
        submask = '255.255.255.240'
        prefix = '/28'
        self.assertEqual(addresses.get_netmask(prefix), submask)
     
    #Testing if the binary notation of the subnet mask is correct
    def test_get_network_bits(self):
        submask = '255.255.255.240'
        bits = '1111 1111 1111 1111 1111 1111 1111 0000'
        self.assertEqual(addresses.get_network_bits(submask), bits)

    #Testing if the available addresses are correct
    def test_get_number_ip_addresses(self):
        prefix = '/28'
        available = 16
        self.assertEqual(addresses.get_number_ip_addresses(prefix), available)
    
    #Testing if the useable addresses are correct
    def test_get_ip_hosts(self):
        prefix = '/28'
        usable = 14
        self.assertEqual(addresses.get_number_ip_hosts(prefix), usable)

#To run the unittest
if __name__ == '__main__':
    unittest.main()
