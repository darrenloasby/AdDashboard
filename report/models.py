from django.db import models
from datetime import datetime

class Report(models.Model):
	date_taken = models.DateTimeField(auto_now_add=True, blank=True)
	user = models.CharField(max_length=200,default='')
	
	def __str__(self):
		return self.user	
	
class GoogleCampaign(models.Model):
	campaign_name = models.CharField(max_length=200, default='')
	report = models.ForeignKey(Report, blank=True, null=True)
    
	def __str__(self):
		return self.campaign_name
		
class GoogleAdGroup(models.Model):
    ad_group_name = models.CharField(max_length=200,default='')
    campaign_name = models.CharField(max_length=200,default='')
    campaign = models.ForeignKey(GoogleCampaign)
	
    def __str__(self):
        return self.ad_group_name
         
class GoogleKeyword(models.Model):
    keyword_id = models.BigIntegerField(default=0)
    keyword_placement = models.CharField(max_length=200,default='')
    clicks = models.BigIntegerField(default = 0)
    impressions = models.BigIntegerField(default = 0)
    cost = models.FloatField(default = 0.0)
    adgroup = models.ForeignKey(GoogleAdGroup)
	
    def __str__(self):
        return self.keyword_placement
		 
class FacebookAccount(models.Model):
	account_name = models.CharField(max_length=200, default='')
	account_id = models.CharField(max_length=200,default='')
	report = models.ForeignKey(Report, blank=True, null=True)
	
	def __str__(self):
		return self.account_name
		
class FacebookCampaign(models.Model):
	name = models.CharField(max_length=200, default='')
	campaign_id = models.CharField(max_length=200, default='')
	status = models.CharField(max_length=200, default='')
	clicks = models.BigIntegerField(default=0)
	cpc = models.FloatField(default=0)
	cost = models.FloatField(default=0)
	impressions = models.BigIntegerField(default=0)
	account = models.ForeignKey(FacebookAccount)
	
	def __str__(self):
		return self.name
