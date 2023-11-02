from django.shortcuts import render

def init_page(request):
    return render(request=request,
                  template_name="init_page.html",
                  context={})