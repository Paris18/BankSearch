# Django Inports
from django.urls import include, path
from django.contrib import admin

# Project Level Imports
from accounts import views as account_views
from banks import views as banks_views

# Third Party Imports
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt import views as jwt_views

# intialize DefaultRouter
router = SimpleRouter()

# register accounts app urls with router
router.register(r'accounts', account_views.UserViewSet, base_name='accounts')
router.register(r'banks', banks_views.BanksViewSet, base_name='banks')

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('api/v1/', include((router.urls, 'api'), namespace='v1')),
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]


