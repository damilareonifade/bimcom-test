from .models import AnnouncedPuResults,PollingUnit
from django import forms

class AnnouncedPuResultsForm(forms.ModelForm):
    class Meta:
        model = AnnouncedPuResults
        fields = ['polling_unit_uniqueid','party_abbreviation','party_score','entered_by_user','date_entered']

class PollingUnit(forms.ModelForm):
    class Meta:
        model = PollingUnit
        fields = ['polling_unit_id','ward_id','lga_id','uniquewardid','polling_unit_number','polling_unit_name','polling_unit_description','lat','long','entered_by_user','date_entered']