import unittest
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.abspath(__file__),
                                '..', '..', '..', '..', 'keystone')))
    
from keystone import server
import keystone.logic.types.auth as auth
import keystone.logic.types.fault as fault

from StringIO import StringIO
from datetime import date
from lxml import etree

    
class TestAuth(unittest.TestCase):
    '''Unit tests for auth.py.'''
    
    pwd_xml = '<?xml version="1.0" encoding="UTF-8"?> \
                <passwordCredentials \
                xmlns="http://docs.openstack.org/idm/api/v1.0" \
                password="secret" username="disabled" \
                />'
    
    def test_pwd_cred_marshall(self):
        creds = auth.PasswordCredentials.from_xml(self.pwd_xml)
        self.assertTrue(creds.password,"secret")
        self.assertTrue(creds.username,"username")
    
        
if __name__ == '__main__':
    unittest.main()