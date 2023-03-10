
from rest_framework.test import APITestCase
from partyapp.models import PoliticalPartyModel,PoliticalLeaderModel,DevelopmentModel
from partyapp.test.TestUtils import TestUtils
class PoliticalAPIFunctionalTest(APITestCase):
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

#Political Party
    def test_fetch_all_registered_political_parties(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("PoliticalParty_TestFetchAllRegisteredPoliticalParties", True, "functional")
            print("PoliticalParty_TestFetchAllRegisteredPoliticalParties=Passed")
        else:
            test_obj.yakshaAssert("PoliticalParty_TestFetchAllRegisteredPoliticalParties", False, "functional")
            print("PoliticalParty_TestFetchAllRegisteredPoliticalParties=Failed")

    def test_get_political_party_by_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/1/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("PoliticalParty_TestGetPoliticalPartyById", True, "functional")
            print("PoliticalParty_TestGetPoliticalPartyById=Passed")
        else:
            test_obj.yakshaAssert("PoliticalParty_TestGetPoliticalPartyById", False, "functional")
            print("PoliticalParty_TestGetPoliticalPartyById=Failed")

    def test_register_political_party(self):#updated now
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty/'
        data={
        "party_id": 1,
        "party_name": "TDP",
        "party_founder": "NTR"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==201:
            test_obj.yakshaAssert("PoliticalParty_TestRegisterPoliticalParty", True, "functional")
            print("PoliticalParty_TestRegisterPoliticalParty=Passed")
        else:
            test_obj.yakshaAssert("PoliticalParty_TestRegisterPoliticalParty", False, "functional")
            print("PoliticalParty_TestRegisterPoliticalParty=Failed")

    def test_update_political_party(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/1/'
        data={
        # "party_id": 1,
        # "party_name": "TDP",
        "party_founder": "RamaRao"
        }
        response=self.client.patch(url,data,format='json')
        if response.status_code==200:
            test_obj.yakshaAssert("PoliticalParty_TestUpdatePoliticalParty", True, "functional")
            print("PoliticalParty_TestUpdatePoliticalParty=Passed")
        else:
            test_obj.yakshaAssert("PoliticalParty_TestUpdatePoliticalParty", False, "functional")
            print("PoliticalParty_TestUpdatePoliticalParty=Failed")

    def test_delete_political_party(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalparty_pk/1/'
        response=self.client.delete(url)
        if response.status_code==200:
            test_obj.yakshaAssert("PoliticalParty_TestDeletePoliticalParty", True, "functional")
            print("PoliticalParty_TestDeletePoliticalParty=Passed")
        else:
            test_obj.yakshaAssert("PoliticalParty_TestDeletePoliticalParty", False, "functional")
            print("PoliticalParty_TestDeletePoliticalParty=Failed")

#PoliticalLeader

    def test_fetch_all_registered_political_leaders(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("PoliticalLeader_TestFetchAllRegisteredPoliticalLeaders", True, "functional")
            print("PoliticalLeader_TestFetchAllRegisteredPoliticalLeaders=Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestFetchAllRegisteredPoliticalLeaders", False, "functional")
            print("PoliticalLeader_TestFetchAllRegisteredPoliticalLeaders=Failed")

    def test_get_political_leader_by_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/1/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("PoliticalLeader_TestGetPoliticalLeaderById", True, "functional")
            print("PoliticalLeader_TestGetPoliticalLeaderById=Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestGetPoliticalLeaderById", False, "functional")
            print("PoliticalLeader_TestGetPoliticalLeaderById=Failed")

    def test_register_political_leader(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader/'
        data={
            "leader_id": 1,
            "party_id": 1,
            "candidate_name": "Naidu",
            "state_name": "Telangana"
        }
        response=self.client.post(url,data,format='json')
        if response.status_code==201:
            test_obj.yakshaAssert("PoliticalLeader_TestRegisterPoliticalLeader", True, "functional")
            print("PoliticalLeader_TestRegisterPoliticalLeader=Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestRegisterPoliticalLeader", False, "functional")
            print("PoliticalLeader_TestRegisterPoliticalLeader=Failed")

    def test_update_political_leader(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/1/'
        data={
            "leader_id": 1,
            "party_id": 1,
            "candidate_name": "C Babu Naidu",
            "state_name": "AP"
        }
        response=self.client.patch(url,data,format='json')
        if response.status_code==200:
            test_obj.yakshaAssert("PoliticalLeader_TestUpdatePoliticalLeader", True, "functional")
            print("PoliticalLeader_TestUpdatePoliticalLeader= Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestUpdatePoliticalLeader", False, "functional")
            print("PoliticalLeader_TestUpdatePoliticalLeader=Failed")

    def test_delete_political_leader(self):  #updated now
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleader_pk/1/'
        response=self.client.delete(url)
        if response.status_code==200:
            test_obj.yakshaAssert("PoliticalLeader_TestDeletePoliticalLeader", True, "functional")
            print("PoliticalLeader_TestDeletePoliticalLeader=Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestDeletePoliticalLeader", False, "functional")
            print("PoliticalLeader_TestDeletePoliticalLeader=Failed")

    def test_get_political_leader_by_party_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/politicalleaderbyparty/?party_id=1'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("PoliticalLeader_TestGetPoliticalLeaderByPartyId", True, "functional")
            print("PoliticalLeader_TestGetPoliticalLeaderByPartyId=Passed")
        else:
            test_obj.yakshaAssert("PoliticalLeader_TestGetPoliticalLeaderByPartyId", False, "functional")
            print("PoliticalLeader_TestGetPoliticalLeaderByPartyId=Failed")

#Development

    def test_fetch_all_created_developments(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("Development_TestFetchAllCreatedDevelopments", True, "functional")
            print("Development_TestFetchAllCreatedDevelopments = Passed")
        else:
            test_obj.yakshaAssert("Development_TestFetchAllCreatedDevelopments", False, "functional")
            print("Development_TestFetchAllCreatedDevelopments = Failed")

    def test_get_development_by_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/1/'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("Development_TestGetDevelopmentById", True, "functional")
            print("Development_TestGetDevelopmentById = Passed")
        else:
            test_obj.yakshaAssert("Development_TestGetDevelopmentById", False, "functional")
            print("Development_TestGetDevelopmentById = Failed")

    def test_create_development(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development/'
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
        response=self.client.post(url,data,format='json')
        if response.status_code==201:
            test_obj.yakshaAssert("Development_TestCreateDevelopment", True, "functional")
            print("Development_TestCreateDevelopment = Passed")
        else:
            test_obj.yakshaAssert("Development_TestCreateDevelopment", False, "functional")
            print("Development_TestCreateDevelopment = Failed")

    def test_update_development(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/1/'
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
        if response.status_code==200:
            test_obj.yakshaAssert("Development_TestUpdateDevelopment", True, "functional")
            print("Development_TestUpdateDevelopment = Passed")
        else:
            test_obj.yakshaAssert("Development_TestUpdateDevelopment", False, "functional")
            print("Development_TestUpdateDevelopment = Failed")

    def test_delete_development(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/development_pk/1/'
        response=self.client.delete(url)
        if response.status_code==200:
            test_obj.yakshaAssert("Development_TestDeleteDevelopment", True, "functional")
            print("Development_TestDeleteDevelopment = Passed")
        else:
            test_obj.yakshaAssert("Development_TestDeleteDevelopment", False, "functional")
            print("Development_TestDeleteDevelopment = Failed")

    def test_get_all_developments_by_leader_id(self):
        test_obj = TestUtils()
        url='http://127.0.0.1:8000/developmentbyleader/?leader_id=1'
        response=self.client.get(url)
        if response.status_code==200:
            test_obj.yakshaAssert("Development_TestGetAllDevelopmentsByLeaderId", True, "functional")
            print("Development_TestGetAllDevelopmentsByLeaderId = Passed")
        else:
            test_obj.yakshaAssert("Development_TestGetAllDevelopmentsByLeaderId", False, "functional")
            print("Development_TestGetAllDevelopmentsByLeaderId = Failed")
