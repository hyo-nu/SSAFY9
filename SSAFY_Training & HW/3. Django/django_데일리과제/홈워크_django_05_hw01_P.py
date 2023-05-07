def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
<<<<<<< HEAD
            title = form['title']
            content = form['content']
            article = Article(title=title,content=content)
            article.save
=======
            title = form.cleaned_data['title']
            content = form.cleaned_data.get('content')
            article = Article(title=title,content=content)
            article.savee()
>>>>>>> bae261c23e717288b08410aeb5166dbee69e2ed0
            return redirect('articles:detail',article.pk)
    form = ArticleForm()
    context = {
        'form':form
    }
    return render(request,'articles/create.html',context)