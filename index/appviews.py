from django.shortcuts import render

from django.http import HttpResponse
from django.template.response import TemplateResponse

from django.views.generic.base import TemplateView

class AppBaseTemplateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["tittle"] = "AppBaseTemplateView -- DEBUG"
        context.update(self.additional_data)
        return context;

    def get(self, request, *args, **kwargs):
        # 设置用户登陆 TAG
        self.additional_data = {}
        if request.user.is_authenticated():
            self.additional_data['logined'] = True
            user = dict()
            user['username'] = request.user.username
            user['is_staff'] = request.user.is_staff

            self.additional_data['user'] = user
        else:
            self.additional_data['logined'] = False

        print(request.user.is_staff)

        return super().get(request,*args,**kwargs)


