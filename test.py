import unittest
from ConfigurationParser import ConfigurationParser

class TestParse(unittest.TestCase):
    
    def test_parse_cust_name(self):
        cp = ConfigurationParser()
        expected_names = ['CUSTOMER_A', 'CUSTOMER_B']
        parsed_names = cp.parseCustomerNames()
        return self.assertEqual(expected_names, parsed_names)
    def test_parse_cust_types(self):
        cp = ConfigurationParser()
        parsed_names = cp.parseCustomerNames()
        return self.assertEqual(list, type(parsed_names))


obj = TestParse()
test1 = obj.test_parse_cust_name()
test2 = obj.test_parse_cust_types()
print(test1)
print(test2)