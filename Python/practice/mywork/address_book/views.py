#from django.shortcuts import render
from models import People
# Create your views here.
from django.template import Context
from django.shortcuts import render_to_response 



def addr_book(request):
    if request.POST:
        post = request.POST
        new_people = People(
            sm = post["sm"],
            name = post["name"],
            birthday = post["birthday"],
            phone = post["phone"],
            qq = post["qq"],
            email = post["email"],
            address = post["address"])    
        if post["sex"] == 'M':
            new_people.sex = True
        else:
            new_people.sex = False       
        new_people.save()
    return render_to_response("address_book.html")        
        
        
def people_list(request):
    people_list = People.objects.all()
    c = Context({"people_list":people_list,})   
    return render_to_response("address_book_show.html", c)
    
    
