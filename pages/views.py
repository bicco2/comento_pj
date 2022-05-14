from django.shortcuts import render

def mainpage(request):
    return render(request, 'pages/mainpage.html')
def contact(request):
    return render(request, 'pages/contact_page.html')
def services(request):
    return render(request, 'pages/services_page.html')