from django.contrib import admin

from .models import PoliticalPartyModel,PoliticalLeaderModel,DevelopmentModel

class PoliticalPartyModelAdmin(admin.ModelAdmin):
    list_display=['party_id','party_name','party_founder']
admin.site.register(PoliticalPartyModel,PoliticalPartyModelAdmin)

class PoliticalLeaderModelAdmin(admin.ModelAdmin):
    list_display=['leader_id','party_id','candidate_name','state_name']
admin.site.register(PoliticalLeaderModel,PoliticalLeaderModelAdmin)

class DevelopmentModelAdmin(admin.ModelAdmin):
    list_display=['development_id','leader_id','development_title','development_activity','development_budget','development_state','development_activity_month','development_activity_year']
admin.site.register(DevelopmentModel,DevelopmentModelAdmin)
