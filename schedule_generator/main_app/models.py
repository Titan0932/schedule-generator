
from django.db import models



class modelMainForm(models.Model):
    id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    sun=models.BooleanField()
    mon=models.BooleanField()
    tues=models.BooleanField()
    wed=models.BooleanField()
    thu=models.BooleanField()     
    fri=models.BooleanField()
    sat=models.BooleanField()
    numofSubs=models.CharField(max_length=150)
    startTime=models.TimeField()
    endTime=models.TimeField()
    

    def __str__(self):
        return str(self.id)

    


class modelSubjects(models.Model):
    id=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    subjects=models.TextField(null=False,primary_key=False)
    sched=models.OneToOneField(modelMainForm,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sched_id)


""" class modelSubjectForm(models.Model):

    sub_id=models.OneToOneField(modelMainForm, on_delete=models.CASCADE)
    def __init__(self, numofSubs,  *args, **kwargs):
        super(modelSubjectForm, self).__init__(numofSubs,*args, **kwargs)
        
        
        if numofSubs:
            for i in range(0,numofSubs):
                self.fields[f"Subject {i+1}"] = models.CharField(max_length=100) """



    