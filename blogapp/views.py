from django.shortcuts import render

posts = [
    {
        'author':'naseem',
        'title':'Blog post 1',
        'content':'first blog post content',
        'date_posted':'25 August 2021'
    },
        {
        'author':'jasim',
        'title':'Blog post 2',
        'content':'second blog post content',
        'date_posted':'30 August 2021'
    }
]
# Create your views here.
def home(request):
    context ={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
