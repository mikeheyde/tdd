import re

class ConfigurationParser:

    def parseCustomerNames(self):
        deviceConig = open('config.txt','r').read()
        customernamePattern = r'ip vrf ([a-zA-Z_]+)\n'
        customerNames = re.findall(customernamePattern, deviceConig)
        return customerNames

