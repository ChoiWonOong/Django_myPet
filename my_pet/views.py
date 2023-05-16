# View에 Model(Post 게시글) 가져오기
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request,'my_pet/index.html')

# my_pet.html 페이지를 부르는 my_pet 함수
def my_pet(request):
    # 모든 Post를 가져와 postlist에 저장합니다
    postlist = Post.objects.all()
    # my_pet.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옵니다
    return render(request, 'my_pet/my_pet.html', {'postlist': postlist})

# my_pet 의 게시글(posting)을 부르는 posting 함수
def posting(request, post_id):
    # 게시글(Post) 중 pk(primary_key)를 이용해 하나의 게시글(post)를 검색
    post = get_object_or_404(Post, pk=post_id)
    # posting.html 페이지를 열 때, 찾아낸 게시글(post)을 post라는 이름으로 가져옴
    return render(request, 'my_pet/posting.html', {'post': post})

def new_post(request):
    if request.method =='POST':
        new_article=Post.objects.create(
            postname=request.POST['postname'],
            contents=request.POST['contents'],
            petimage=request.FILES['petimage'],
        )
        return redirect('/my_pet/')
    return render(request, 'my_pet/new_post.html')

def delete_post(request, post_id):
    post = Post.objects.get(pk = post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('/my_pet/')
    return render(request, 'my_pet/remove_post.html ', {'Post':post})
