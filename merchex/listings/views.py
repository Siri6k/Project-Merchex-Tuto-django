from django.shortcuts import render
from .models import Band

def hello(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/hello.html',
                  {'bands': bands})
def about(request):
    return HttpResponse("""<h1>hello Django</h1>
<p>je m'appelle Adam chris Kayungura</p>
<p>Mon num +243 994126699 <br> email: adamchrisk@gmail.com</p>
""")
