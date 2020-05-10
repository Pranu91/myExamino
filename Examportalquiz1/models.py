from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from django.utils.timezone import now
from django.contrib.auth.models import User

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    phone=models.CharField(max_length=50,default='')
    desc=models.TextField(max_length=300,default='')
    date=models.DateTimeField(default=now)


    def __str__(self):
        return self.name

alphanumeric=RegexValidator(r'^[0-9a-zA-Z]*$')
class Create_Classroom(models.Model):

    class_id=models.AutoField(primary_key=True,blank=True)
    class_code=models.CharField(max_length=9,default='')
    class_name=models.CharField(max_length=50,default='')
    admin_name=models.CharField(max_length=50,default='')
    date1=models.DateTimeField(default=now)
    slug=models.CharField(max_length=130,null=True,blank=True,default='')
    section=models.CharField(max_length=50,default='')
    subject=models.CharField(max_length=50,default='')
    desc=models.CharField(max_length=150,default='')

    def __unicode__(self):
        return self.class_code

    class Meta:
        unique_together=('class_code','slug')

    def __str__(self):

        return self.class_code +'By'+ self.admin_name

class join_student(models.Model):
    sno2=models.AutoField(primary_key=True)
    user=models.CharField(max_length=130,default='')
    join_code=models.ForeignKey(Create_Classroom, on_delete=models.CASCADE)



    def __str__(self):
        return self.user


class Question1(models.Model):
    sno1=models.AutoField(primary_key=True)
    testcode1=models.ForeignKey(Create_Classroom,on_delete=models.CASCADE)
    que1=models.CharField(max_length=500,default='')
    ans1=models.CharField(max_length=500,default='')
    que2=models.CharField(max_length=500,default='')
    ans2=models.CharField(max_length=500,default='')
    que3=models.CharField(max_length=500,default='')
    ans3 = models.CharField(max_length=500,default='')
    que4=models.CharField(max_length=500,default='')
    ans4 = models.CharField(max_length=500,default='')
    que5=models.CharField(max_length=500,default='')
    ans5 = models.CharField(max_length=500,default='')



    def __str__(self):
        return self.testcode1.admin_name




class Question2(models.Model):
    sno1=models.AutoField(primary_key=True)
    testcode2=models.ForeignKey(Create_Classroom,on_delete=models.CASCADE)

    que1=models.CharField(max_length=500,default='')
    ans1=models.CharField(max_length=500,default='')
    que2=models.CharField(max_length=500,default='')
    ans2=models.CharField(max_length=500,default='')
    que3=models.CharField(max_length=500,default='')
    ans3 = models.CharField(max_length=500,default='')
    que4=models.CharField(max_length=500,default='')
    ans4 = models.CharField(max_length=500,default='')
    que5=models.CharField(max_length=500,default='')
    ans5 = models.CharField(max_length=500,default='')




    def __str__(self):
        return self.testcode2.admin_name
class Question3(models.Model):
    sno1=models.AutoField(primary_key=True)
    testcode3=models.ForeignKey(Create_Classroom,on_delete=models.CASCADE)
    que1=models.CharField(max_length=500,default='')
    ans1=models.CharField(max_length=500,default='')
    que2=models.CharField(max_length=500,default='')
    ans2=models.CharField(max_length=500,default='')
    que3=models.CharField(max_length=500,default='')
    ans3 = models.CharField(max_length=500,default='')
    que4=models.CharField(max_length=500,default='')
    ans4 = models.CharField(max_length=500,default='')
    que5=models.CharField(max_length=500,default='')
    ans5 = models.CharField(max_length=500,default='')



    def __str__(self):
        return self.testcode3.admin_name





