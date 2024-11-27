import datetime
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def showtime(request):
    Todaysdate=datetime.datetime.now()
    templatefilename="index.html"
    dict={"Todaysdate":Todaysdate}
    return render(request,templatefilename,dict)