from django.shortcuts import render

# Create your views here.
def home(request):
    count = request.session.get('count', 0)
    new_count = count + 1
    request.session['count'] = new_count
    return render(request, 'mycount/home.html', {'count': new_count})
