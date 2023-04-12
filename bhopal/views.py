from django.shortcuts import render
from .models import People
from django.contrib import messages

# Create your views here.
def index(r):
    return render(r,'index.html')
def contact(r):
    if r.method=='POST':
        if r.POST['name']and r.POST['email']and r.POST['mobile']and r.POST['message'] :
            record=People()
            record.name=r.POST['name']
            record.email=r.POST['email']
            record.mobile=r.POST['mobile']
            record.message=r.POST['message']
            record.save()
            messages.info(r,'Your Input is Received ,Thanks !')
            return render(r,'contact.html')
    else:
         return render (r,'contact.html')
def temple(r):
    return render(r,'temple.html')
def birla(r):
    return render(r,'birla.html')
def gufa(r):
    return render(r,'gufa.html')
def karuna(r):
    return render(r,'karuna.html')
def iskcon(r):
    return render(r,'iskcon.html')
def lake(r):
    return render(r,'lake.html')
def lower(r):
    return render(r,'lower.html')
def upper(r):
    return render(r,'upper.html')
def shahpura(r):
    return render(r,'shahpura.html')
def hotel(r):
    return render(r,'hotel.html')
def noor(r):
    return render(r,'noor.html')
def jehan(r):
    return render(r,'jehan.html')
def marriott(r):
    return render(r,'marriott.html')
def taj(r):
    return render(r,'taj.html')
def radisson(r):
    return render(r,'redisson.html')
def museum(r):
    return render(r,'museum.html')
def indira(r):
    return render(r,'indira.html')
def tribal(r):
    return render(r,'tribal.html')
def state(r):
    return render(r,'state.html')
def science(r):
    return render(r,'science.html')
def golghar(r):
    return render(r,'golghar.html')
def regional(r):
    return render(r,'regional.html')
def park(r):
    return render(r,'park.html')
def ekant(r):
    return render(r,'ekant.html')
def chinar(r):
    return render(r,'chinar.html')
def van(r):
    return render(r,'van.html')
def kamla(r):
    return render(r,'kamla.html')
def dam(r):
    return render(r,'dam.html')
def kaliyasot(r):
    return render(r,'kaliyasot.html')
def kerwa(r):
    return render(r,'kerwa.html')
def bhadbhada(r):
    return render(r,'bhadbhada.html')
def more(r):
    return render(r,'more.html')
def sanchi(r):
    return render(r,'sanchi.html')
def bhim(r):
    return render(r,'bhim.html')
def bhoj(r):
    return render(r,'bhoj.html')
def satpura(r):
    return render(r,'satpura.html')
def vidisha(r):
    return render(r,'vidisha.html')
def raisen(r):
    return render(r,'raisen.html')
def pachmarhi(r):
    return render(r,'pachmarhi.html')
def salkanpur(r):
    return render(r,'salkanpur.html')
def halali(r):
    return render(r,'halali.html')
def amar(r):
    return render(r,'amar.html')
def kolar(r):
    return render(r,'kolar.html')
def mall(r):
    return render(r,'mall.html')
def db(r):
    return render(r,'db.html')
def aura(r):
    return render(r,'aura.html')
def people(r):
    return render(r,'people.html')
def ashima(r):
    return render(r,'ashima.html')
def capital(r):
    return render(r,'capital.html')
def time(r):
    return render(r,'time.html')

