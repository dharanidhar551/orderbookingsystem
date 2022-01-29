from audioop import reverse
from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector
from .__init__ import xlrd
from django.db import connection
import csv
from templates import forms
from django.contrib.auth import authenticate
from django.contrib import messages

def home(request):
    l=[]
    with open('C:\\Users\\SKAIK SHAHIN\\dbs\\web\\media\\CSV\\ex.csv') as csv_file:
        csv.reader(csv_file, delimiter=',')
        for row in csv_file:
            l.append(list(map(str,row.split(","))))
    l=l[1::]
    #q="insert into students(id,name,con)values(%s,%s,%s)"
    ks=[]
    with connection.cursor() as cursor:
        q="insert into students(id,name,con)values(%s,%s,%s)"
        cursor.executemany(q,l)
        connection.commit()
    return HttpResponse('done')
def login(request):
    uservalue=''
    passwordvalue=''
    form= forms.Loginform(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")
        user1= authenticate(username=uservalue, password=passwordvalue)
        render(request,'index.html')
        if user1 is not None:
            #login(request,user1)
            context= {'form': form,
                      'error': 'The login has been successful'}
            return render(request, 'user.html', context)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            return render(request, 'index.html', context )
    else:
        context= {'form': form}
        return render(request, 'index.html', context)
    
def user(request):
    messages.info(request,"order succesful")
    return render(request,"user.html")