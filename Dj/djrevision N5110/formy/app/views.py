from django.shortcuts import redirect, render
from app.form import ReviewFormM,ReviewForm

# Create your views here.
def review(request):
    if request.method == 'POST':
        print('post')
        fp = ReviewFormM(request.POST)
        if fp.is_valid():
            # print(fp.cleaned_data) 
            fp.save()
            return redirect('thx')
    else:
        print('else')
        fp = ReviewFormM()
    return render(request,'app/review.html',{'form':fp})
    
def thank(request):
    return render(request,'app/thank.html')