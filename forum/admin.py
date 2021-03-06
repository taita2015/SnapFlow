from django.contrib import admin


from .models import Class
from .models import SubClass
from .models import Thread
from .models import Comment
from .models import TAG
from .models import UserThreadStatus

class ClassAdmin(admin.ModelAdmin):
    pass
    list_display = ["display_name","create_time","order"]
    # ordering = 'order'
    # name = models.CharField("hehe", max_length=20, blank=True, null=True)
    # chinese_name = models.CharField(max_length=20, blank=True, null=True)
    # create_user = models.ForeignKey(User, default=1, blank=True, null=True)
    # create_time



class ThreadAdmin(admin.ModelAdmin):
    list_display = ["tittle","content",'create_user',"main_class","sub_class","create_time"]
# #      sub_class = models.ForeignKey(SubClass,null=True)
#     tittle = models.CharField(max_length=20,blank=True)
#     content = models.TextField(default="")
#     create_user = models.ForeignKey(User,default=1)
#     create_time = models.DateTimeField(auto_now=True,blank=True,null=True)
#     last_time = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    search_fields = ["id","tittle"]


class SubClassAdmin(admin.ModelAdmin):
    list_display = ['display_name','parent_class']



class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','content']

admin.site.register(SubClass,SubClassAdmin)
admin.site.register(Class,ClassAdmin)

admin.site.register(Thread,ThreadAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(TAG)


from .models import ThreadLike

class ThreadLikeAdmin(admin.ModelAdmin):
    list_display = ['thread','user']

admin.site.register(ThreadLike,ThreadLikeAdmin)


admin.site.register(UserThreadStatus)