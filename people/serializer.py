from rest_framework import serializers

from .models import Staff, ResearchStaff

# class HeroSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = Hero
# 		fields = ("id", "name","alias")

class StaffSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Staff
		fields = ("name", "email", "affiliation", "title", "director", "committee")

class ResearchSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ResearchStaff
		fields = ("name", "email", "affiliation", "title", "research_status")