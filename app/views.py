from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from faker import Faker


def index(request):
    fake = Faker()
    # def get_client_ip():
    #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if x_forwarded_for:
    #         ip = x_forwarded_for.split(',')[0]
    #     else:
    #         ip = request.META.get('REMOTE_ADDR')
    #     return ip
    # ipno=get_client_ip()
    # for j in range(30):
    #     User.objects.create_user(username=fake.user_name(), password=fake.password())
    # users=User.objects.all()
    # user_list=[]
    # for i in users:
    #     user = User.objects.get(username=i.username)
    #     user_list.append(user)
    # for i in range(0,30):
    #     userdetails.objects.create(
    #         name=fake.name(),
    #         phonenumber=fake.phone_number(),
    #         college=fake.name(),
    #         email=fake.email(),
    #         hobbies=fake.name(),
    #         user=user_list[i]
    #     )
    views = Blog.objects.filter(user=request.user)

    return render(request, "home.html", {'view': views})


def signuppage(request):
    return render(request, "signup.html")


def loginuserpage(request):
    return render(request, "login.html")


def signup_user(request):
    username = request.POST.get("username")
    password = request.POST.get("passsword")
    user = User.objects.create_user(username=username, password=password)
    login(request, user)
    return redirect("/personal-details")


def personal_details(request):
    return render(request, "personal-details.html")


def personal_details_registered(request):
    name = request.POST.get("name")
    phonenumber = request.POST.get("phonenumber")
    college = request.POST.get("college")
    email = request.POST.get("email")

    userdetails(name=name, phonenumber=phonenumber, college=college,
                email=email, user=request.user).save()
    return redirect("/Dashboard")


def loginuser(request):
    username = request.POST.get('username')
    Password = request.POST.get('password')
    print(username)
    # check if user has entered correct credentials
    user = authenticate(username=username, password=Password)
    print(user)
    if user is not None:
        # A backend authenticated the credentials
        print("yess")
        login(request, user)
        return redirect('/Dashboard')
    else:
        return HttpResponse("Login Failed!")


def Dashboard(request):
    return render(request, "Dashboard.html")


def blog_content_save(request):
    blogtitle = request.POST.get("title")
    blogcontent = request.POST.get("content")

    Blog(blogtitle=blogtitle, blogcontent=blogcontent, user=request.user).save()
    return redirect("/Dashboard")


def ip_view(request, idip):
    def get_client_ip():
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ipno = get_client_ip()

    if ip.objects.filter(blogid=idip).exists():
        obj = ip.objects.filter(blogid=idip)
        if obj.filter(ipadd=ipno).exists():
            pass
        else:
            ip.objects.create(ipadd=ipno, blogid=idip)
            post = Blog.objects.get(pk=idip)
            post.views.add(obj.get(ipadd=ipno))
    else:
        obj = ip.objects.filter(blogid=idip)
        ip.objects.create(ipadd=ipno, blogid=idip)
        post = Blog.objects.get(pk=idip)
        post.views.add(obj.get(ipadd=ipno))

    blogpost = Blog.objects.get(pk=idip)

    post = likeip.objects.filter(blogid=idip)

    flag = []
    if post.filter(likedip=ipno).exists():
        flag.append(True)
    else:
        flag.append(False)
    flagcheck = flag[0]
    return render(request, "blog.html", {'blogpost': blogpost, 'flag': flagcheck})


def like_view(request, pkid):
    def get_client_ip():
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ipno = get_client_ip()

    if likeip.objects.filter(blogid=pkid).exists():
        obj = likeip.objects.filter(blogid=pkid)
        if obj.filter(likedip=ipno).exists():
            pass
        else:
            likeip.objects.create(likedip=ipno, blogid=pkid)
            post = Blog.objects.get(pk=pkid)
            post.ipliked.add(obj.get(likedip=ipno))
            post.userliked.add(request.user)
    else:
        obj = likeip.objects.filter(blogid=pkid)
        print(obj)
        likeip.objects.create(likedip=ipno, blogid=pkid)
        post = Blog.objects.get(pk=pkid)
        print(obj)
        post.ipliked.add(obj.get(likedip=ipno))
        post.userliked.add(request.user)

    return redirect(f"/blog/{pkid}")


def comment_view(request, blogid):
    comment = request.POST.get("comment")
    comments.objects.create(
        comment=comment, blogid=blogid, usercomment=request.user)
    return redirect(f"/blog/{blogid}")


def dislike_view(request, blogid):
    def get_client_ip():
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ipno = get_client_ip()
    obj = likeip.objects.filter(blogid=blogid)
    obj.get(likedip=ipno).delete()
    return redirect(f"/blog/{blogid}")


def view_profile(request, user):
    return redirect(f"/profile/{user}")


def profile(request, user):
    # profile_details=userdetails.objects.filter(user=user)
    try:
        user = User.objects.get(username=user)
        print(user)
    except User.DoesNotExist:
        # Handle the case where the user does not exist
        return render(request, 'user_not_found.html', {'username': user})

    return render(request, 'profile.html', {'user': user})


def search_view(request):
    search = request.GET.get('search')
    obj = userdetails.objects.filter(name__startswith=search)
    payload = []
    if search:
        obj = userdetails.objects.filter(name__startswith=search)
        print(obj)
    # print(obj)
        for i in obj:
            payload.append({
                'name': i.name
            })

    return JsonResponse({
        'status': True,
        'payload': payload,
    })
