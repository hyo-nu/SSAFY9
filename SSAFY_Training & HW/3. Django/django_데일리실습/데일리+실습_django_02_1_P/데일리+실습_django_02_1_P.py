from django.shortcuts import render

# Create your views here.
def price(request,food,number):
    product_price = {
        "라면" : 980,
        "홈런볼" : 1500,
        "칙촉" : 2300, 
        "식빵" : 1800
    }
    money = product_price.get(food, -1) * number

    context = {
        'product_price' : product_price,
        'food' : food,
        'number' : number,
        'money' : money,
    }
    return render(request, 'price.html',context)


