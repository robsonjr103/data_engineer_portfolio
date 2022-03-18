import sys
sys.path.insert(0, '../../') # Add the 'project' folder to PATH
#import Pytest


class Testcreatebucket(object):

    def test_createbucket(self):

        test_argument = "a"
        actual = 'create_bucket'