from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm, MovieModelForm
# Create your views here.
def list(request):
    # 전체 무비목록 가져오기
    movies = Movie.objects.all()
    return render(request, "movie/list.html", {"movies":movies})

def detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, "movie/detail.html", {"movie":movie})

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        title_en = request.POST.get("title_en")
        audience = request.POST.get("audience")
        open_date = request.POST.get("open_date")
        genre = request.POST.get("genre")
        watch_grade = request.POST.get("watch_grade")
        score = request.POST.get("score")
        poster_url = request.POST.get("poster_url")
        description = request.POST.get("description")
        
        movie = Movie.objects.create(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade,score=score, poster_url=poster_url,description=description)
        return redirect("movies:list")
    else:
        return render(request, "movie/create.html")
        
def form_create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid(): # 통과하면 검증이 된 데이터-> cleaned_data
            title = form.cleaned_data.get("title")
            title_en = form.cleaned_data.get("title_en")
            audience = form.cleaned_data.get("audience")
            open_date = form.cleaned_data.get("open_date")
            genre = form.cleaned_data.get("genre")
            watch_grade = form.cleaned_data.get("watch_grade")
            score = form.cleaned_data.get("score")
            poster_url = form.cleaned_data.get("poster_url")
            description = form.cleaned_data.get("description")
            
            movie = Movie.objects.create(title=title, title_en=title_en, audience=audience, open_date=open_date, genre=genre, watch_grade=watch_grade,score=score, poster_url=poster_url,description=description)

            return redirect("movies:list")
    else:
        form = MovieForm() # 클래스를 인스턴스화함.
    return render(request, "movie/form_create.html", {"form":form})
    
    
def form_update(request, id):
    movie = Movie.objects.get(id=id) # 어떤 글을 업데이트하는가에 대한 정보
    if request.method == "POST":
        # 저장이 되도록
        form = MovieForm(request.POST)
        if form.is_valid(): # 통과하면 검증이 된 데이터-> cleaned_data
            title = form.cleaned_data.get("title")
            title_en = form.cleaned_data.get("title_en")
            audience = form.cleaned_data.get("audience")
            open_date = form.cleaned_data.get("open_date")
            genre = form.cleaned_data.get("genre")
            watch_grade = form.cleaned_data.get("watch_grade")
            score = form.cleaned_data.get("score")
            poster_url = form.cleaned_data.get("poster_url")
            description = form.cleaned_data.get("description")
            
            movie.title = title
            movie.title_en = title_en
            movie.audience = audience
            movie.open_date = open_date
            movie.genre = genre
            movie.watch_grade = watch_grade
            movie.score = score
            movie.poster_url = poster_url
            movie.description = description
            movie.save()
            
            return redirect("movies:list")

    else:
        # 데이터를 딕셔너리형태로 만듦.
        data = {"title":movie.title, "title_en":movie.title_en, "audience":movie.audience,
                "open_date":movie.open_date, "genre":movie.genre, "watch_grade":movie.watch_grade,
                "score":movie.score, "poster_url":movie.poster_url, "description":movie.description
        }
        form = MovieForm(data) # 폼을 만들고 + 미리 데이터를 넣어줌.
    return render(request, "movie/form_update.html", {"form":form})
    
def model_form_create(request):
    if request.method == "POST":
        form = MovieModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movies:list")
    else:
        form = MovieModelForm()
    return render(request, "movie/model_form_create.html",{"form":form})
    
def model_form_update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        form = MovieModelForm(request.POST, instance=movie)
        # 이제 검증
        if form.is_valid():
            form.save()
            return redirect("movies:detail", id) # 수정한 글로 갈 수 있도록
    else:
        form = MovieModelForm(instance=movie)
    return render(request, "movie/model_form_update.html", {"form":form})