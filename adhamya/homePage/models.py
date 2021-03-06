from django.db import models
from django.forms import TextInput
from datetime import datetime

#-- User Database --
class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    FName = models.CharField("User's First Name", max_length=50)
    LName = models.CharField("User's Last Name", max_length=50)
    EmailID = models.EmailField("User's Email Id", max_length=254, unique=True)
    Password = models.CharField("User's Password", max_length=50)
    MobileNo = models.CharField("User's Mobile Number", max_length=10)
    Type = models.CharField("User's Type", max_length=50)
    IsLoggedIn = models.IntegerField()

#-- Payment Database --
class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    EventID = models.ForeignKey('Events', on_delete=models.CASCADE)
    TransactionID = models.CharField("Transaction ID", max_length=50, unique=True)
    TransactionDateTime = datetime.now()
    EmailID = models.ForeignKey('User', on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Status = models.IntegerField()

#--NewsFeed Database--
class NewsFeed(models.Model):
    NewsFeedID = models.AutoField(primary_key=True)
    Title = models.CharField("Title", max_length=50)
    Content = models.CharField("Content", max_length=1000)
    Image = models.ImageField(upload_to=None, height_field=50, width_field=50, max_length=100)
    Category = models.CharField("Category", max_length=50)
    CreatedBy = models.CharField("CreatedBy User ID", max_length=10)
    CreatedOn = datetime.now()
    UpdatedBy = models.CharField("UpdatedBy User ID", max_length=10, null=True)
    UpdatedOn = models.DateField(null=True)
    Status = models.IntegerField(default=1)

#--Events Database--
class Events(models.Model):
    Event = models.AutoField(primary_key=True)
    EventName = models.CharField("Event Name", max_length=50)
    Description = models.CharField("Event Description", max_length=1000)
    Image = models.ImageField(upload_to=None, height_field=50, width_field=50, max_length=100)
    Organiser1 = models.CharField("Organisers1 Name", max_length=50)
    Organiser2 = models.CharField("Organisers2 Name", max_length=50)
    Organiser3 = models.CharField("Organisers3 Name", max_length=50)
    MobileNo1 = models.CharField("Organiser1's Mobile Number", max_length=10)
    MobileNo2 = models.CharField("Organiser2's Mobile Number", max_length=10)
    MobileNo3 = models.CharField("Organiser3's Mobile Number", max_length=10)
    IsActive = models.IntegerField()


# --Donation Database--
class Donation(models.Model):
    DonationID = models.AutoField(primary_key=True)
    TransactionID = models.CharField("Transaction ID", max_length=50,unique=True)
    EmailID = models.ForeignKey('User',on_delete=models.CASCADE)
    Amount = models.IntegerField()
    Status = models.IntegerField()
    TransactionDateTime = datetime.now()

#--FeedBack Database--
class Feedback(models.Model):
    FeedbackID =  models.AutoField(primary_key=True)
    Name = models.CharField("Name", max_length=100)
    EmailID = models.EmailField("Email Id", max_length=254)
    Comment = models.CharField("Feedback....", max_length=1000)

# Create your models here.
