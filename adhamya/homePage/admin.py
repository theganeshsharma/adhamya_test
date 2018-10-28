from django.contrib import admin
from . models import User,Payment,Donation,Feedback,NewsFeed,Events

admin.site.register(User)
admin.site.register(Payment)
admin.site.register(Donation)
admin.site.register(Feedback)
admin.site.register(NewsFeed)
admin.site.register(Events)



# Register your models here.
