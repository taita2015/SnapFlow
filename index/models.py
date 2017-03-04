from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
#
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             instance = ModelWithFileField(file_field=request.FILES['file'])
#             instance.save()
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})


from django.conf import settings


class UserProfileManager(models.Manager):
    def givemeabool(self):
        return True


# 用户模型扩充
from os import path
def upload_to(instance,filename):

    filename,filetype = filename.split('.')
    _= path.join("ava",str(instance.user.id)+'.'+filetype)
    print(_)
    return _

class UserProfile(models.Model):

    user = models.OneToOneField(User)
    avatar = models.ImageField(null=True,blank=True,upload_to=upload_to)
    set_avatar = models.BooleanField(default=False)
    # avatar = models.ImageField(null=True,blank=True)
    work_year = models.IntegerField(default=0)
    work_place = models.CharField(max_length=20)
    work_nickname = models.CharField(max_length=20)
    language = models.CharField(max_length=10,null=True,blank=True)
    self_introduction = models.CharField(max_length=300)
    blog_adderss = models.URLField()

    objects = UserProfileManager()

    def __str__(self):
        return "[userprofile@user_id:"+str(self.user.id)+" username:"+self.user.username+"]"



# class UserProfileManager(models.Manager):
#     def givemeabool(self):
#         return True

def create_user_profile(sender,instance,created,**kwargs):
    if(created):
        profile = UserProfile()
        profile.user = instance
        profile.save()

# 添加事件监听
post_save.connect(create_user_profile,sender=User)