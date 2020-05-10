from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Contact, Create_Classroom, join_student, Question3, Question2, Question1
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.crypto import get_random_string
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'home.html')


def base(request):
    return render(request, 'base.html')


def base1(request):
    return render(request, 'base1.html')


def que1(request):
    return render(request, 'que1.html')


def que2(request):
    return render(request, 'que2.html')


def que3(request):
    return render(request, 'que3.html')


def que4(request):
    return render(request, 'que4.html')


def que5(request):
    return render(request, 'que5.html')


def scores(request):
    return render(request, 'scores.html')


def about(request):
    return render(request, 'about.html')


def pricing(request):
    return render(request, 'pricing.html')


def test1(request, class_id):
    t=Create_Classroom.objects.get(class_id=class_id)
    param = {'t': t}
    return render(request, 'test1.html', param)


def test1confirm(request):
    if request.method=='POST':
        que1=request.POST['que1']
        ans1=request.POST['ans1']
        que2=request.POST['que2']
        ans2=request.POST['ans2']
        que3=request.POST['que3']
        ans3=request.POST['ans3']
        que4=request.POST['que4']
        ans4=request.POST['ans4']
        que5=request.POST['que5']
        ans5=request.POST['ans5']
        test_code=request.POST['test_code']
        h=Create_Classroom.objects.get(class_code=test_code)
        con=Question1(testcode1=h, que1=que1, ans1=ans1, que2=que2, ans2=ans2, que3=que3, ans3=ans3, que4=que4,ans4=ans4, que5=que5, ans5=ans5)
        con.save()
        x = Create_Classroom.objects.filter(admin_name = request.user)
        params = {'msg': 'Dear User Your Quiz has been Successfully Uploaded', 'x': x}
        return render(request, 'myclassroom.html', params)
    param={'msg': 'Sorry for the inconvienace sir pls contact to the developer Pranay kavishwar -8982161715 '}
    return render(request, 'myclassroom.html', param)


def test2(request, class_id):
    t=Create_Classroom.objects.get(class_id=class_id)
    param={'t': t}
    return render(request, 'test2.html', param)


def test2confirm(request):
    if request.method == 'POST':
        que1 = request.POST['que1']
        ans1 = request.POST['ans1']
        que2 = request.POST['que2']
        ans2 = request.POST['ans2']
        que3 = request.POST['que3']
        ans3 = request.POST['ans3']
        que4 = request.POST['que4']
        ans4 = request.POST['ans4']
        que5 = request.POST['que5']
        ans5 = request.POST['ans5']
        test_code = request.POST['test_code']
        h = Create_Classroom.objects.get(class_code = test_code)
        con = Question2(testcode2 = h, que1 = que1, ans1 = ans1, que2 = que2, ans2 = ans2, que3 = que3, ans3 = ans3, que4 = que4, ans4 = ans4, que5 = que5, ans5 = ans5)
        con.save()
        x = Create_Classroom.objects.filter(admin_name = request.user)
        params = {'msg': 'Dear User Your Quiz has been Successfully Uploaded ', 'x': x}
        return render(request, 'myclassroom.html', params)
    param={'msg': 'Sorry for the inconvienace sir pls contact to the developer Pranay kavishwar -8982161715 '}
    return render(request, 'myclassroom.html', param)


def test3(request, class_id):
    t = Create_Classroom.objects.get(class_id = class_id)
    param={'t': t}
    return render(request, 'test3.html', param)


def test3confirm(request):
    if request.method == 'POST':
        que1 = request.POST['que1']
        ans1 = request.POST['ans1']
        que2 = request.POST['que2']
        ans2 = request.POST['ans2']
        que3 = request.POST['que3']
        ans3 = request.POST['ans3']
        que4 = request.POST['que4']
        ans4 = request.POST['ans4']
        que5 = request.POST['que5']
        ans5 = request.POST['ans5']
        test_code = request.POST['test_code']
        h = Create_Classroom.objects.get(class_code = test_code)
        con = Question3(testcode3 = h, que1 = que1, ans1 = ans1, que2 = que2, ans2 = ans2, que3 = que3, ans3 = ans3, que4 = que4,ans4 = ans4, que5 = que5, ans5 = ans5)
        con.save()
        x = Create_Classroom.objects.filter(admin_name = request.user)
        params = {'msg': 'Dear User Your Quiz has been Successfully Uploaded ', 'x': x}
        return render(request, 'myclassroom.html', params)
    param={'msg': 'Sorry for the inconvienace sir pls contact to the developer Pranay kavishwar -8982161715 '}
    return render(request, 'myclassroom.html', param)



def createtest(request, class_id):
    x = Create_Classroom.objects.get(class_id = class_id)
    params={'x': x}
    return render(request, 'createtest.html', params)


def joinedclasses(request):
    z = join_student.objects.filter(user = request.user).count()
    if z>0:
        x = join_student.objects.filter(user = request.user)
        params = {'x': x}
        return render(request, 'joinedclasses.html', params)
    else:
        param = {'msg': "Dear User it Seems you have Not Joined any Classroom"}
        return render(request, 'base1.html', param)

def startlearning(request, class_id):
    x=Create_Classroom.objects.filter(class_id=class_id)
    print(class_id)
    print(x)
    param={'x': x}
    return render(request, 'startlearning.html', param)


def join(request):
    if request.method == 'POST':
        join_code = request.POST.get('join_code')
        user = request.POST.get('user_name')
        y = Create_Classroom.objects.get(class_code = join_code)
        x = join_student(join_code = y, user = user)
        x.save()
        params={'y': y}
        return render(request, 'confirmclassroom.html', params)


def myclassroom(request):
    z = Create_Classroom.objects.filter(admin_name = request.user).count()
    if z > 0:
        x = Create_Classroom.objects.filter(admin_name = request.user)
        params = {'x': x}
        return render(request, 'myclassroom.html', params)
    else:
        param={'msg': "Dear user Please Create a Classroom First"}
        return render(request, 'base.html', param)


def create(request):
    class_code = get_random_string(length = 8)
    if request.method == 'POST':
        class_name = request.POST['classname']
        admin_name =request.POST['admin_name']
        section = request.POST['section']
        subject = request.POST['subject']
        desc = request.POST['desc']
        Con = Create_Classroom(class_code = class_code, admin_name = admin_name, class_name = class_name, section = section, subject = subject, desc = desc, date1 = datetime.today())
        Con.save()
        x = Create_Classroom.objects.filter(class_code = class_code).first()
        params = {"x": x}
        return render(request, 'confirmcreate.html', params)
    else:
        return HttpResponse('404 page Not Found')



def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        args = {'user': request.user}
        return render(request, 'contact.html', args)

    return render(request, 'contact.html')


def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorerneus inputs
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        param={'msg': 'Successfully signed Up as Examino User!!'}
        return render(request, 'home.html', param)

    else:
        return HttpResponse('404 - Not found')


def handlelogin(request):
    if request.method == 'POST':
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username = loginusername, password = loginpass)
        if user is not None:
            login(request, user)
            return redirect('home')





    return HttpResponse('404 page Not Found')


def handlelogout(request):
    logout(request)
    messages.success(request, "")
    return redirect('home')






