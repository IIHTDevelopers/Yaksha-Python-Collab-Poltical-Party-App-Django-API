from rest_framework.test import APITestCase
from partyapp.models import PoliticalPartyModel,PoliticalLeaderModel,DevelopmentModel
from partyapp.test.TestUtils import TestUtils
class PoliticalAPIExceptionalTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        PoliticalPartyModel.objects.create(
        party_id= 1,
        party_name= "TDP",
        party_founder= "NTR")

        PoliticalLeaderModel.objects.create(
        leader_id= 1,
        party_id=1,
        candidate_name="Naidu",
        state_name="Telangana"
        )

        DevelopmentModel.objects.create(
        development_id= 1,
        leader_id= 1,
        development_title= "Mission Bhagiratha",
        development_activity= "Free Water Supply Throughout State",
        development_budget=450.00,
        development_state= "TS",
        development_activity_month= 11,
        development_activity_year= 2015)

        with open("../output_revised.txt","w") as f:
            pass

    def test_fetch_all_registered_political_parties_fail(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalpartyx/'
        response=self.client.get(url)
        if response.status_code==404:
            test_obj.yakshaAssert("PoliticalParty_TestFetchAllRegisteredPoliticalPartiesFail", True, "exception")
            print("PoliticalParty_TestFetchAllRegisteredPoliticalPartiesFail = Passed")
        else:
            test_obj.yakshaAssert("PoliticalParty_TestFetchAllRegisteredPoliticalPartiesFail", False, "exception")
            print("PoliticalParty_TestFetchAllRegisteredPoliticalPartiesFail = Failed")

    def test_get_political_party_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/111/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("PoliticalParty_TestGetPoliticalPartyByNonExistId", True, "exception")
            print("PoliticalParty_TestGetPoliticalPartyByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("PoliticalParty_TestGetPoliticalPartyByNonExistId", False, "exception")
            print("PoliticalParty_TestGetPoliticalPartyByNonExistId= Failed")

    def test_register_political_party_with_insufficient_data(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty/'
        data={
        "party_id": 1,
        "party_name": "TDP"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("PoliticalParty_TestRegisterPoliticalPartyWithInsufficientData", True, "exception")
            print("PoliticalParty_TestRegisterPoliticalPartyWithInsufficientData = Passed")
        else:
            test_obj.yakshaAssert("PoliticalParty_TestRegisterPoliticalPartyWithInsufficientData", False, "exception")
            print("PoliticalParty_TestRegisterPoliticalPartyWithInsufficientData= Failed")

    def test_update_political_party_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/1111/'
        data={
        "party_founder": "RamaRao"
        }
        response=self.client.patch(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("PoliticalParty_TestUpdatePoliticalPartyByNonExistId", True, "exception")
            print("PoliticalParty_TestUpdatePoliticalPartyByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("PoliticalParty_TestUpdatePoliticalPartyByNonExistId", False, "exception")
            print("PoliticalParty_TestUpdatePoliticalPartyByNonExistId = Failed")

    def test_delete_political_party_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/1111/'
        response=self.client.delete(url)
        if response.status_code==500:
            test_obj.yakshaAssert("PoliticalParty_TestDeletePoliticalPartyByNonExistId", True, "exception")
            print("PoliticalParty_TestDeletePoliticalPartyByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("PoliticalParty_TestDeletePoliticalPartyByNonExistId", False, "exception")
            print("PoliticalParty_TestDeletePoliticalPartyByNonExistId = Failed")

#PoliticalLeader

    def test_fetch_all_registered_political_leaders_fail(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleaderx/'
        response=self.client.get(url)
        if response.status_code==404:
            test_obj.yakshaAssert("PoliticalLeader_TestFetchAllRegisteredPoliticalLeadersFail", True, "exception")
            print("PoliticalLeader_TestFetchAllRegisteredPoliticalLeadersFail = Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestFetchAllRegisteredPoliticalLeadersFail", False, "exception")
            print("PoliticalLeader_TestFetchAllRegisteredPoliticalLeadersFail = Failed")

    def test_get_political_leader_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/111/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("PoliticalLeader_TestGetPoliticalLeaderByNonExistId", True, "exception")
            print("PoliticalLeader_TestGetPoliticalLeaderByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestGetPoliticalLeaderByNonExistId", False, "exception")
            print("PoliticalLeader_TestGetPoliticalLeaderByNonExistId = Failed")

    def test_register_political_leader_with_insufficient_data(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader/'
        data={
            "leader_id": 1,
            "party_id": 1,
            "candidate_name": "Naidu",
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("PoliticalLeader_TestRegisterPoliticalLeaderWithInsufficientData", True, "exception")
            print("PoliticalLeader_TestRegisterPoliticalLeaderWithInsufficientData = Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestRegisterPoliticalLeaderWithInsufficientData", False, "exception")
            print("PoliticalLeader_TestRegisterPoliticalLeaderWithInsufficientData = Failed")

    def test_update_political_leader_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/111/'
        data={
            "leader_id": 1,
            "party_id": 1,
            "candidate_name": "C Babu Naidu",
            "state_name": "AP"
        }
        response=self.client.patch(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("PoliticalLeader_TestUpdatePoliticalLeaderByNonExistId", True, "exception")
            print("PoliticalLeader_TestUpdatePoliticalLeaderByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestUpdatePoliticalLeaderByNonExistId", False, "exception")
            print("PoliticalLeader_TestUpdatePoliticalLeaderByNonExistId = Failed")

    def test_delete_political_leader_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/1111/'
        response=self.client.delete(url)
        if response.status_code==500:
            test_obj.yakshaAssert("PoliticalLeader_TestDeletePoliticalLeaderByNonExistId", True, "exception")
            print("PoliticalLeader_TestDeletePoliticalLeaderByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestDeletePoliticalLeaderByNonExistId", False, "exception")
            print("PoliticalLeader_TestDeletePoliticalLeaderByNonExistId = Failed")

    def test_get_political_leader__by_non_exist_party_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleaderbyparty/?party_id=111'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("PoliticalLeader_TestGetPoliticalLeaderByNonExistPartyId", True, "exception")
            print("PoliticalLeader_TestGetPoliticalLeaderByNonExistPartyId = Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestGetPoliticalLeaderByNonExistPartyId", False, "exception")
            print("PoliticalLeader_TestGetPoliticalLeaderByNonExistPartyId = Failed")

#Development

    def test_fetch_all_created_developments_fail(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/developmentx/'
        response=self.client.get(url)
        if response.status_code==404:
            test_obj.yakshaAssert("Development_TestFetchAllCreatedDevelopmentsFail", True, "exception")
            print("Development_TestFetchAllCreatedDevelopmentsFail = Passed")
        else:
            test_obj.yakshaAssert("Development_TestFetchAllCreatedDevelopmentsFail", False, "exception")
            print("Development_TestFetchAllCreatedDevelopmentsFail = Failed")

    def test_get_development_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/111/'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Development_TestGetDevelopmentByNonExistId", True, "exception")
            print("Development_TestGetDevelopmentByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("Development_TestGetDevelopmentByNonExistId", False, "exception")
            print("Development_TestGetDevelopmentByNonExistId = Failed")

    def test_create_development_fail_with_insufficient_data(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/developmentx/'
        data={
        "development_id": 1,
        "leader_id": 1,
        "development_title": "Mission Bhagiratha",
        "development_activity": "Free Water Supply Throughout State",
        "development_budget": "450.00",
        "development_state": "TS",
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==404:
            test_obj.yakshaAssert("Development_TestCreateDevelopmentFailWithInsufficientData", True, "exception")
            print("Development_TestCreateDevelopmentFailWithInsufficientData = Passed")
        else:
            test_obj.yakshaAssert("Development_TestCreateDevelopmentFailWithInsufficientData", False, "exception")
            print("Development_TestCreateDevelopmentFailWithInsufficientData = Failed")

    def test_update_development_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/111/'
        data={
        "development_id": 1,
        "leader_id": 1,
        "development_title": "Mission Bhagiratha",
        "development_activity": "Free Water Supply Throughout State",
        "development_budget": "450.00",
        "development_state": "TS",
        "development_activity_month": 11,
        "development_activity_year": 2015
        }
        response=self.client.patch(url,data,format='json')
        if response.status_code==500:
            test_obj.yakshaAssert("Development_TestUpdateDevelopmentByNonExistId", True, "exception")
            print("Development_TestUpdateDevelopmentByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("Development_TestUpdateDevelopmentByNonExistId", False, "exception")
            print("Development_TestUpdateDevelopmentByNonExistId = Failed")

    def test_delete_development_by_non_exist_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/1111/'
        response=self.client.delete(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Development_TestDeleteDevelopmentByNonExistId", True, "exception")
            print("Development_TestDeleteDevelopmentByNonExistId = Passed")
        else:
            test_obj.yakshaAssert("Development_TestDeleteDevelopmentByNonExistId", False, "exception")
            print("Development_TestDeleteDevelopmentByNonExistId = Failed")

    def test_get_all_developments_by_non_exist_leader_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/developmentbyleader/?leader_id=111'
        response=self.client.get(url)
        if response.status_code==500:
            test_obj.yakshaAssert("Development_TestGetAllDevelopmentsByNonExistLeaderId", True, "exception")
            print("Development_TestGetAllDevelopmentsByNonExistLeaderId = Passed")
        else:
            test_obj.yakshaAssert("Development_TestGetAllDevelopmentsByNonExistLeaderId", False, "exception")
            print("Development_TestGetAllDevelopmentsByNonExistLeaderId = Failed")
