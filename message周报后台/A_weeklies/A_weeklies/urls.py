"""A_weeklies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
# username: admin, passwd: wxywxywxy
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from users.views import SmsCodeViewset, UserViewset
from weeklies.views import WeekliesViewset
from groups.views import GroupViewset
from teamprojects.views import ProjectViewset
from applications.views import ApplicationViewset
from utils.forget.views import ForgetViewset

router = DefaultRouter()

router.register('codes', SmsCodeViewset, base_name="codes")

# 用户url
router.register('users', UserViewset, base_name="users")

# 周报url
router.register('weeklies', WeekliesViewset, base_name="weeklies")

# 团队项目
router.register('projects', ProjectViewset, base_name="projects")

# 小组url
router.register('groups', GroupViewset, base_name="groups")

# 申请url
router.register('applications', ApplicationViewset, base_name="applications")


urlpatterns = [
    path('xadmin/', xadmin.site.urls),

    path('docs/', include_docs_urls(title="星火周报")),

    path('api-auth/', include('rest_framework.urls')),

    path('api/', include(router.urls)),

    # jwt认证
    path('api/login/', obtain_jwt_token),

    path('api/forget/', ForgetViewset.as_view({'patch': 'partial_update'})),
]
