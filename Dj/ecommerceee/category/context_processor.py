from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
# {'links': <QuerySet [<Category: jacket>, <Category: jeans>, <Category: shirts>, <Category: shoes>, <Category: tshirts>]>} 