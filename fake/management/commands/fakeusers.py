from django.core.management.base import BaseCommand,CommandError
from django.contrib.auth.models import User
import random


from django.contrib.auth.models import User
from index.models import UserProfile

def get_random_username():
    start_with = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@.+-_"
    sa = []
    sa.append(random.choice(start_with))
    for i in range(7):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

class Command(BaseCommand):
    help = 'what the fuck you are doing?'


    def handle(self, *args, **options):

        print("creating fake users")

        import os
        import random
        base_dir = 'fake/fake_user_avatar/'
        dest_dir = 'media_cdn/ava/'

        file_list = os.listdir(base_dir)
        while file_list:
            # 创建随机名字
            _name = get_random_username()

            # 移动头像文件
            file_list = os.listdir(base_dir)
            if not file_list:
                print("avatar_path_has_no_file")
                return
            this_file = random.choice(file_list)


            suffix = this_file[this_file.rfind('.'):]
            if not suffix:
                print(this_file+"has no suffix")
                return

            file_path = base_dir+this_file
            new_file_path = dest_dir+_name+suffix
            os.rename(file_path,new_file_path)

            # 创建用户
            u = User()
            u.username = _name
            u.email = _name+"@gmail.com"
            u.save()

            u.userprofile.language = "english"
            u.work_place = "google"
            u.userprofile.work_nickname = "hacker-painter"
            u.userprofile.self_introduction = "もしも彼らが君の何かを盗んだとして それはくだらないものだよ  返して贳うまでもない筈甚至何故なら価値は生命に従って付いている"

            u.userprofile.avatar="ava/"+_name+suffix
            u.userprofile.save()
            print("created user:"+_name)
            
        print("finished creating users")