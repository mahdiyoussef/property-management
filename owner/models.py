from django.db import models

class manager(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    addressline1 = models.CharField(null=True,max_length=50)
    addressline2 = models.CharField(null=True,max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(default='MA',max_length=5)
    active = models.BooleanField(default=True)



class owner(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    nationalid = models.CharField(null=True,max_length=50)
    passportnumber = models.CharField(null=True,max_length=50)
    addressline1 = models.CharField(null=True,max_length=200)
    addressline2 = models.CharField(null=True,max_length=200)
    city = models.CharField(max_length=50)
    country = models.CharField(default='MA',max_length=5)
    managerid = models.ForeignKey(manager,null=True,on_delete=models.CASCADE)
    active = models.BooleanField(default=True)




