from django.shortcuts import render

posts=[
    {
        'author':'Mayank',
        'title':'DjangoLearn',
        'content':'Learning from Youtube channels',
        'date_posted':'Oct 5,2019'
    },
    {
        'author':'Nahar',
        'title':'Python',
        'content':'Learning from Youtube channels',
        'date_posted':'Oct 5,2019'
    },
    {
        'author':'Allan',
        'title':'Web Development',
        'content':'Learning from Youtube channels',
        'date_posted':'Oct 5,2019'
    }
]


def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})