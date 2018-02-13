from django.shortcuts import render

# Create your views here.

def fourOfour(request):
    # View code here...
    return render(request, 'mysite/404.html')

def about(request):
    # View code here...
    return render(request, 'mysite/about.html')

def blog1(request):
    # View code here...
    return render(request, 'mysite/blog-home-1.html')

def blog2(request):
    # View code here...
    return render(request, 'mysite/blog-home-2.html')

def blogpost(request):
    # View code here...
    return render(request, 'mysite/blog-post.html')

def contact(request):
    # View code here...
    return render(request, 'mysite/contact.html')

def faq(request):
    # View code here...
    return render(request, 'mysite/faq.html')

def portfolio1(request):
    # View code here...
    return render(request, 'mysite/portfolio-1-col.html')

def portfolio2(request):
    # View code here...
    return render(request, 'mysite/portfolio-2-col.html')

def portfolio3(request):
    # View code here...
    return render(request, 'mysite/portfolio-3-col.html')

def portfolio4(request):
    # View code here...
    return render(request, 'mysite/portfolio-4-col.html')

def pricing(request):
    # View code here...
    return render(request, 'mysite/pricing.html')

def services(request):
    # View code here...
    return render(request, 'mysite/services.html')

def index(request):
    # View code here...
    return render(request, 'mysite/index.html')

def sidebar(request):
    # View code here...
    return render(request, 'mysite/sidebar.html')

def base(request):
    # View code here...
    return render(request, 'mysite/base.html')

def portfolio_item(request):
    # View code here...
    return render(request, 'mysite/portfolio-item.html')



