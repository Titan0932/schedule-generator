
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from main_app.forms import SubForm, mainForm
from main_app.models import modelMainForm,modelSubjects



def schedule_list(request):
    data1=modelMainForm.objects.all()
    data2=modelSubjects.objects.all()
    loop=range(len(data1))  
    
    form1=[]
    form2=[]

    #print(data1.values())

    for i in loop: 
        form1.append(data1[i])

    for i in loop:
        form2.append(data2[i])

    return render(request, 'list.html',{'form1':data1.values, 'form2':data2.values, 'range': loop, 'test':data1.values})




def display_form1(request):
    if request.method=='POST':
        main=mainForm(request.POST)
        if main.is_valid():
            #main.save(commit=False)
            try:
                obj=modelMainForm.objects.get(sun=main.cleaned_data['sun'],mon=main.cleaned_data['mon'],
                                tues=main.cleaned_data['tues'],wed=main.cleaned_data['wed'],thu=main.cleaned_data['thu'],fri=main.cleaned_data['fri'],
                                sat=main.cleaned_data['sat'],numofSubs=main.cleaned_data['numofSubs'],startTime=main.cleaned_data['startTime'],endTime=main.cleaned_data['endTime'])
                """ obj=modelMainForm.objects.get(sun="1",mon="1",
                                tues="0",wed="0",thu="0",fri="0",
                                sat="0",numofSubs=main.cleaned_data['numofSubs'],startTime=main.cleaned_data['startTime'],endTime=main.cleaned_data['endTime'])    """             
            except Exception as e:
                
                if str(type(e))=="<class 'main_app.models.modelMainForm.DoesNotExist'>":
                    main.save(commit=True)
                    obj=modelMainForm.objects.get(sun=main.cleaned_data['sun'],mon=main.cleaned_data['mon'],
                                tues=main.cleaned_data['tues'],wed=main.cleaned_data['wed'],thu=main.cleaned_data['thu'],fri=main.cleaned_data['fri'],
                                sat=main.cleaned_data['sat'],numofSubs=main.cleaned_data['numofSubs'],startTime=main.cleaned_data['startTime'],endTime=main.cleaned_data['endTime'])
      
                    return redirect('next/'+str(obj.id)+'-'+str(main.cleaned_data['numofSubs']))  
                else:
                    print('ERROR-------------------------- ', type(e))
                    msg='UNKNOWN ERROR!!'
                    return render(request,'main.html',{'msg':msg, 'form':main})
            else:
                msg='The Schedule Already EXISTSS'
                return render(request,'main.html',{'msg':msg, 'form':main})

        else:
            msg=main.errors['__all__']
            return render(request,'main.html',{'msg':msg, 'form':main})

         
    main=mainForm()
    return render(request,'main.html',{'form':main})

def enter_subjects(request,id,numofSubs):
    if request.method=='POST':
        
        store=[]
        dicts=dict(request.POST.items())
        for i in dicts:
            if i!='csrfmiddlewaretoken': 
                store.append(dicts[i])

        ins= modelSubjects(subjects=store,sched_id=id)
        
       
        ins.save()
        data=modelMainForm.objects.get(id=id)
        return redirect(f'/new/next/{str(data.id)}-{str(data.numofSubs)}-{str(ins.subjects)}-{str(data.startTime)}-{str(data.endTime)}/')  

    else:
        subjForm=SubForm(numofSubs)
        return render(request,'subjects.html',{'form':subjForm})


def delete_schedule(request,del_id):
    if request.method=='GET':
        del_sched=get_object_or_404(modelMainForm,id=del_id)
        del_sched.delete()
        return redirect('/')

