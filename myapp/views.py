from django.shortcuts import render
from .models import Rating
from .forms import RatingForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404,render ,redirect

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def temp(request):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.save()
            
            rating_objs = Rating.objects.all()
            sum=0
            count=len(rating_objs)
            for r in rating_objs:
                sum+=r.rating
            rating = round((sum/count),1)
            return redirect('temp')
    else:
        form = RatingForm()
    rating_objs = Rating.objects.all()
    sum=0
    count=len(rating_objs)
    for r in rating_objs:
        sum+=r.rating
    rating = round((sum/count),1)
    return render(request, 'indextemp.html', {'form':form, 'rating': rating, 'count':count})

def test(request):
    return render(request, 'index3.html', {})

def rating(request):
    rating_objs = Rating.objects.all()
    sum=0
    count=len(rating_objs)
    for r in rating_objs:
        sum+=r.rating
    rating = round((sum/count),1)
    return JsonResponse({
            'result': [
                {'rating': str(rating), 'count': str(count)}
            ],
        })

def post_rating(request):
    rating = request.GET.get('rating', None)
    # Rating.objects.create()
    print(rating)
    data = {"rating":"3","count":"3"},
    print(json.dumps(data))
    return JsonResponse(data,safe=False)
