"""bpltour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
MEDIA_URL = '/media/'
from django.contrib import admin
from django.urls import path
from bhopal.views import index,contact,temple,birla,gufa,karuna,iskcon,lake,upper,lower,shahpura,hotel,noor,jehan,radisson,taj,marriott,museum,golghar,tribal,science,indira,state,regional,park,van,kamla,ekant,chinar,dam,kaliyasot,kerwa,bhadbhada,more,bhim,satpura,sanchi,bhoj,vidisha,raisen,pachmarhi,salkanpur,halali,amar,kolar,mall,ashima,aura,db,people,capital,time


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('contact',contact,name='contact'),
    path('temple',temple,name='temple'),
    path('birla',birla,name='birla'),
    path('iskcon',iskcon,name='iskcon'),
    path('karuna',karuna,name='karuna'), 
    path('gufa',gufa,name='gufa'),
    path('lake',lake,name='lake'),
    path('upper',upper,name='upper'),
    path('lower',lower,name='lower'),
    path('shahpura',shahpura,name='shahpura'),
    path('hotel',hotel,name='hotel'),
    path('marriott',marriott,name='marriott'),
    path('taj',taj,name='taj'),
    path('radisson',radisson,name='radisson'),
    path('jehan',jehan,name='jehan'),
    path('noor',noor,name='noor'),
    path('museum',museum,name='museum'),
    path('regional',regional,name='regional'),
    path('tribal',tribal,name='tribal'),
    path('state',state,name='state'),
    path('indira',indira,name='indira'),
    path('science',science,name='science'),
    path('golghar',golghar,name='golghar'),
    path('park',park,name='park'),
    path('van',van,name='van'),
    path('chinar',chinar,name='chinar'),
    path('ekant',ekant,name='ekant'),
    path('kamla',kamla,name='kamla'),
    path('dam',dam,name='dam'),
    path('kaliyasot',kaliyasot,name='kaliyasot'),
    path('kerwa',kerwa,name='kerwa'),
    path('bhadbhada',bhadbhada,name='bhadbhada'),
    path('more',more,name='more'),
    path('sanchi',sanchi,name='sanchi'),
    path('bhim',bhim,name='bhim'),
    path('satpura',satpura,name='satpura'),
    path('bhoj',bhoj,name='bhoj'),
    path('vidisha',vidisha,name='vidisha'),
    path('raisen',raisen,name='raisen'),
    path('pachmarhi',pachmarhi,name='pachmarhi'),
    path('salkanpur',salkanpur,name='salkanpur'),
    path('halali',halali,name='halali'),
    path('amar',amar,name='amar'),
    path('kolar',kolar,name='kolar'),
    path('mall',mall,name='mall'),
    path('aura',aura,name='aura'),
    path('db',db,name='db'),
    path('people',people,name='people'),
    path('ashima',ashima,name='ashima'),
    path('capital',capital,name='capital'),
    path('time',time,name='time'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
