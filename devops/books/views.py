from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from books.models import Product , Book

# Create your views here.
def getHomePage(request):
    # booksinfo= [
	# 	{"id":1, "name":"book1", "description":"book1_description"},
	# 	{"id":2, "name":"book2", "description":"book2_description"},
	# 	{"id":3, "name":"book3", "description":"book3_description"},
	# ]
    products = Book.objects.all()
    return render(request, "Books/homepage.html", context={"data":products})

def about(request):
    return render(request, 'Books/about.html')

def contact(request):
    return render(request, 'Books/contact.html')

def get_product_info(request , id):
    #product = Product.objects.get(id=id)
    product = get_object_or_404(Book,id=id)
    # return HttpResponse(product)
    return render(request , "Books/showproduct.html" , context={"product":product})

def delete_product(request , id):
    product = Book.objects.get(id=id)
    product.delete()
    return redirect('homepage')
    #return HttpResponse("deleted")