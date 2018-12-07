from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm # For registering patient
from django.contrib import messages #FOR Messaging 

from django .utils import timezone

#The patient function returns the template file for the user to put all the details of the patient...
def patient(self):
            return render(self, 'patient/patient.html', {})  

def register(request):
            if request.method == 'POST':
                        Myform =  PostForm(request.POST)
                        if Myform.is_valid():
                                    Myform.save(commit = True)
                                    messages.success(request, 'Patients Profile Details Uploaded Successfully at  ' + str(timezone.datetime.now().strftime('%H:%M:%S')) )
                                    return render(request, 'patient/patient.html',   { }  )
                        else:
                              return HttpResponse("Something is wrong.")               
            else:
                        return HttpResponse("<h1> Security Error! Encountered GET request. </h1>")