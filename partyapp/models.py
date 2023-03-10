from django.db import models
class PoliticalPartyModel(models.Model):
    party_id =models.AutoField(primary_key=True)
    party_name=models.CharField(max_length=20)
    party_founder=models.CharField(max_length=100)


class PoliticalLeaderModel(models.Model):
    leader_id =models.AutoField(primary_key=True)
    party_id =models.IntegerField()
    candidate_name =models.CharField(max_length=20)
    state_name =models.CharField(max_length=100)


class DevelopmentModel(models.Model):
    development_id =models.AutoField(primary_key=True)
    leader_id =models.IntegerField()
    development_title =models.CharField(max_length=20)
    development_activity  =models.CharField(max_length=100)
    development_budget =models.DecimalField(decimal_places=2,max_digits=100)
    development_state  =models.CharField(max_length=100)
    development_activity_month=models.IntegerField()
    development_activity_year=models.IntegerField()
