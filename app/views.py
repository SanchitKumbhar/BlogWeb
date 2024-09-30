import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404

# Create your views here.
from urllib.parse import urlparse
from faker import Faker


def index(request):
    # Dummy Data
    '''
    fake = Faker()
    def get_client_ip():
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ipno=get_client_ip()
    for j in range(30):
        User.objects.create_user(
            username=fake.user_name(), password=fake.password())
    users=User.objects.all()
    user_list=[]
    for i in users:
        user = User.objects.get(username=i.username)
        user_list.append(user)
    for i in range(0,30):
        userdetails.objects.create(
            name=fake.name(),
            phonenumber=fake.phone_number(),
            college=fake.name(),
            email=fake.email(),
            hobbies=fake.name(),
            user=user_list[i]
        )
        '''
    if request.user.is_authenticated:
        views = Blog.objects.all()
        return render(request, "home.html", {'view': views})
    else:
        return redirect("/login")


def signuppage(request):
    return render(request, "signup.html")


def loginuserpage(request):
    return render(request, "authenticate.html")


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
    return redirect("/")


def loginuser(request):
    username = request.POST.get('username')
    Password = request.POST.get('password')
    print(username)
    # check if user has entered correct crede`ntials
    user = authenticate(username=username, password=Password)
    print(user)
    if user is not None:
        # A backend authenticated the credentials
        print("yess")
        login(request, user)
        return redirect('/')
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
    previous_url = request.session.get('previous_url', 'No previous URL')
    parsed_url = urlparse(previous_url)
    blogobj = get_object_or_404(Blog, id=idip)
    userobj = User.objects.get(username=blogobj.user)
    followuser = userdetails.objects.get(user=userobj.id)
    if request.user in blogobj.views.all():
        pass
    else:
        blogobj.views.add(request.user)
        print("user add")
        views = Blog.objects.all()
    return render(request, "blog.html", {'blogpost': blogobj, 'follow': followuser})

    # total_followings=followers.objects.filter(user_follows=post.user)


def like_view(request):
    if request.method == 'POST':
        # Load the JSON data from the request body
        data = json.loads(request.body)
        blogid = data.get('blogid')
        blogobj = get_object_or_404(Blog, id=blogid)
        if request.user in blogobj.userliked.all():
            pass
        else:
            blogobj.userliked.add(request.user)
            print("user add")
        print(data)
        return JsonResponse({
            'succ': 200
        })


def comment_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        comment = data.get('text')
        blogid = data.get('blogid')
        comments.objects.create(
            comment=comment, blogid=blogid, usercomment=request.user)
        return JsonResponse({
            'succ': 200
        })


def dislike_view(request):
    if request.method == "POST":
        # Load the JSON data from the request body
        data = json.loads(request.body)
        blogid = data.get('blogid')
        obj = get_object_or_404(Blog, id=blogid)
        obj.userliked.remove(request.user)
        return JsonResponse({
            'succ': 200
        })


def view_profile(request, user):
    return redirect(f"/profile/{user}")


# def profile(request, user):
#     # profile_details=userdetails.objects.filter(user=user)
#     try:
#         user = User.objects.get(username=user)
#         totalblogs = Blog.objects.filter(user=user).count()
#         totalfollowers = followers.objects.filter(followed_user=user).count()
#         followings = followers.objects.filter(user_follows=user).count()
#         context = {
#             'username': user,
#             'totalfollowers': totalfollowers,
#             'totalblogs': totalblogs,
#             'followings': followings
#         }
#         profileuser = followers.objects.filter(followed_user=user)
#         followingusercheck = profileuser.filter(user_follows=request.user)

#         if followingusercheck.exists():
#             context["flag"] = 0
#         else:
#             context['flag'] = 1

#     except User.DoesNotExist:
#         # Handle the case where the user does not exist
#         return render(request, 'user_not_found.html')

#     return render(request, 'profile.html', context=context)


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


def follow(request, user):
    previous_url = request.session.get('previous_url', 'No previous URL')
    parsed_url = urlparse(previous_url)
    userobj = User.objects.get(username=user)
    followuser = userdetails.objects.get(user=userobj.id)
    followuser.followers.add(request.user)
    return redirect(f"{parsed_url.path}")


# def unfollow(request, user):
#     user = User.objects.get(username=user)
#     unfollowuser = followers.objects.filter(followed_user=user)
#     followinguser = unfollowuser.filter(user_follows=request.user)
#     followinguser.delete()
#     return HttpResponse("Done")


def taged_user(request):
    pass


def EditProfile(request):
    if request.method == 'GET':
        userinstance = userdetails.objects.get(user=request.user)
        profile = {
            'name': userinstance.name,
            'college': userinstance.college,
            'phonenumber': userinstance.phonenumber
        }
        return JsonResponse(profile)
    elif request.method == 'POST':
        data = json.loads(request.body)
        flag = data.get('flag')
        print(flag)
        if flag == 'changename':
            name = data.get('name')
            userinstance = userdetails.objects.get(user=request.user)
            userinstance.name = name
            userinstance.save()
            return JsonResponse({
                'succ': 200
            })
        elif flag == 'changecollege':
            college = data.get('college')
            userinstance = userdetails.objects.get(user=request.user)
            userinstance.college = college
            userinstance.save()
            return JsonResponse({
                'succ': 200
            })
        else:
            phonenumber = data.get('phonenumber')
            userinstance = userdetails.objects.get(user=request.user)
            userinstance.phonenumber = phonenumber
            userinstance.save()
            return JsonResponse({
                'succ': 200
            })


def EditProfilePage(request):
    return render(request, 'Edit-profile.html')
