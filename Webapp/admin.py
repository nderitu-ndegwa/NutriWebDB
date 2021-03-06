from django.contrib import admin
from Webapp.models import Message, Order, UserProfileInfo, User

# Change db header
admin.site.site_header = "Nutrition Platform DB"


# ModelAdmin Class is a representation of user-defined models in the admin panel.
# We have to register the Admin Model alongside the model we want to change. 
# This class is used to override the default class views. 
class OrderA(admin.ModelAdmin):
    fields = ['Order_Number','Client','No_of_Samples','Sample_Type','Sample_Reciever','Analyis_Required','Remarks','Stage']#to show when entering data
    list_display = ['Order_Number','No_of_Samples','Client','Date_recieved','Sample_Reciever','Analyis_Required','Stage','Remarks']
    search_fields = ['Order_Number','Analyis_Required','Client']
    list_filter = ['Stage','Analyis_Required']

class UserProfileInfoA(admin.ModelAdmin):
    fields = ['User','contact_number','Organisation_name','Address','Town_or_City','Postcode_or_zip_code','Country']
    list_display = ['contact_number','Organisation_name','Country']
    search_fields = ['User']

# Register your models after describing them.

admin.site.register(Order, OrderA)
admin.site.register(Message)
admin.site.register(UserProfileInfo,UserProfileInfoA)