from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Item
from .forms import ItemForm


@require_safe
def index(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'shops/index.html', context)

# 문제 5. 글을 생성하면 발생하는 에러를 수정하여 detail 페이지로 이동하도록 하시오.
# datail 의 경우 여러 항목 중 하나만을 보여주는 내용을 담고 있기 때문에 
# 반드시 보여주고자 하는 항목의 프라이머리키(pk)를 함께 전달해 주어야한다.
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return redirect('shops:detail',item.pk)
    else:
        form = ItemForm()

    context = {
        'form': form,
    }
    return render(request, 'shops/create.html', context)


@require_safe
def detail(request, pk):
    item = Item.objects.get(pk=pk)
    context = {
        'item': item,
    }
    return render(request, 'shops/detail.html', context)


# 문제 6. 글 수정이 아닌 새롭게 생성되고 있다. 이를 수정하시오.
# 수정하고자 하는 항목의 pk값을 가지는 항목인 item을 instance에 넣어주고 
# 그 instance를  Form의 매개변수로 넣어줘야 수정하고자 하는 항목의 테이블 key에 
# 수정한 value를 넣어줄 수 있다.
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('shops:detail', pk)
    else:
        form = ItemForm(instance = item)
    
    context = {
        'form': form,
        'pk': pk,
    }
    return render(request, 'shops/update.html', context)


@require_POST
def delete(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return redirect('shops:index')