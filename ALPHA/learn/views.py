from django.shortcuts import render
from .models import Student, Teacher

# Create your views here.
# def learn(request):
#     request.session['customerid'] = 1
#     resellersdata = [
#         {'companyregid':1, 'companyname':"baabte" ,
#         'contry':'India', 'status':'Active'},

#          {'companyregid':2, 'companyname':"baabte2" ,
#         'contry':'India', 'status':'Active'},

#          {'companyregid':3, 'companyname':"baabte3" ,
#         'contry':'India', 'status':'Active'},
#     ]
#     return render(request, 'learn.html',{'resellersdata':resellersdata})

def learn(request):
    if request.method=='POST':
        std_name = request.POST["name"]
        std_age = request.POST["age"]
        std_mark = request.POST["mark"]
        std1 = Student(name=std_name,age=std_age,mark=std_mark)

        std1.save()
    return render(request,'learn.html')


def teacher(request):
    if request.method=='POST':
        tcr_name = request.POST["name"]
        tcr_age = request.POST["age"]
      
        tcr1 = Teacher(name=tcr_name,age=tcr_age)
        
        tcr1.save()
    return render(request,'techer.html')

def view_techer(request):
    tcr_data = Teacher.objects.all()

    return render(request,'viewtcr.html',{'deatails':tcr_data,})