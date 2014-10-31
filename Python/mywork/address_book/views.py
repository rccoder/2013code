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
    
    
def delete_people(request):
    delete_id = request.GET["id"]
    People.objects.filter(id = delete_id).delete()
    return render_to_response("deleted_successfully.html")
    
def change_people_list(request):
    change_id = request.GET["id"]
    new_people = People.objects.get(id = change_id)
    if request.POST:
        post = request.POST
        new_people.sm = post["sm"]
        new_people.name= post["name"]
        new_people.birthday = post["birthday"]
        new_people.phone = post["phone"]
        new_people.qq = post["qq"]
        new_people.email = post["email"]
        new_people.address = post["address"]    
        if post["sex"] == 'M':
            new_people.sex = True
        else:
            new_people.sex = False       
        new_people.save()
    c = Context({"new_people":new_people,})
    return render_to_response("change_people.html", c)
def search_people(request):
    post=request.POST
    searching=post["name"]
    try:   
        a=People.objects.get(name=searching)
        c=Context({"people":a})
        return render_to_response("Search_Results.html", c)
    except:       
       return render_to_response("no_searched.html")
