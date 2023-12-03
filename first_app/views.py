from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    d={'name':'sagar','age':16,'list':[1,2,3,4,5],'course':[
        {'id':1,
        'name':'python',
        'fee':5000
        },
        {'id':1,'name':'django','fee':7000},
        {'id':1,'name':'C','fee':3000},
    ],
    'student':
     [
     {'name': 'zed', 'age': 19},
      {'name': 'amy', 'age': 22},
       {'name':'joe', 'age': 31}, 
       ],
         'today':datetime.now(),
    'blog':'4 days, 6 hours',
    'unorder':'  [‘States’, [‘Kansas’, [‘Lawrence’, ‘Topeka’], ‘Illinois’]]'
    }
    
    return render(request,'home.html',d)

def about(request):
    return render(request,'about.html')
def contact (request):
    return render(request,'contact.html')


