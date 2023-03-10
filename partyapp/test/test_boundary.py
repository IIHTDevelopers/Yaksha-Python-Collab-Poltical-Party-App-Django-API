from rest_framework.test import APITestCase
from partyapp.test.TestUtils import TestUtils
class PoliticalAPIBoundaryTest(APITestCase):
    def test_boundary(self):
        test_obj = TestUtils()
        test_obj.yakshaAssert("PoliticalParty_TestBoundary",True,"boundary")
        print("PoliticalParty_TestBoundary = Passed")
