from django.shortcuts import render
from apps.base.models import InfoUser, Skills, MyService, Education
from apps.secondary.models import Secondary, Colleagues, Blogs, PersentShow, Projects

# Create your views here.
def index(request):
    projects = Projects.objects.all()
    blogs = Blogs.objects.all()
    colleagues = Colleagues.objects.all()
    persent = PersentShow.objects.all()
    skills = Skills.objects.all()
    myservice = MyService.objects.all()
    education = Education.objects.all()
    infouser = InfoUser.objects.latest("id")
    secondary = Secondary.objects.latest("id")
    return render(request, "index.html", locals())

def blog_details(request, id):
    blogs = Blogs.objects.get(id=id)
    infouser = InfoUser.objects.latest("id")
    return render(request, "blog-details.html", locals())