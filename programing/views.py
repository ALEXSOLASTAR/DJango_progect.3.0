from django.shortcuts import render




def page1(request):
    title="page1"
    content = "One Hellow"

    return render(request, "page1.html", {"title": title, "content": content})

def page2(request):
    title = "page2"
    content = "Two Hellow"

    return render(request, "page2.html", {"title": title, "content": content})