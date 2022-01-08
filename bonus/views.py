from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.
from .models import Prize, Winner

def how(request):
    return render(
        request,
        'bonus/how.html',
    )

def about(request):
    return render(
        request,
        'bonus/about.html',
    )

def connect(request):
    return render(
        request,
        'bonus/connect.html',
    )
def recommend(request):
    rec=Prize.objects.filter(heart__gt=0)
    print(rec)
    return render(
        request,
        'bonus/recommend.html',
        context={
            'recomment_list':rec,
        }
    )

def index(request):
    prizeList = Prize.objects.all()
    winnerList = Winner.objects.all()
    winnerListDict = {} # 由 pid 取得獲獎者的 list
    prizeCNameDict = {} # 由 pid 取得 p cname
    # prizePidDict = {}

    for p in prizeList:
        wList = [w.last_ssn for w in Winner.objects.filter(prize_id=p)]
        winnerListDict[p.pid] = wList
        prizeCNameDict[p.pid] = p.cname
        # prizePidDict = p.pid

    print (str(winnerListDict))
    print (str(prizeCNameDict))
    
    return render(
        request,
        'bonus/index.html',
        context={'winnerList_dict': winnerListDict,
                 'prizeCName_dict': prizeCNameDict,
                #  'prizePid_dict': prizePidDict,
                }
    )

def heartamount(request):
    if request.method=='GET':
        if 'like' in request.GET:
            l=Prize.objects.get(pid= request.GET['like'])
            l.heart+=1
            l.save()
        elif 'dislike' in request.GET:
            l=Prize.objects.get(pid= request.GET['dislike'])
            if  l.heart>0:
                l.heart-=1
                l.save()

        return HttpResponse(l)

from django.views.generic import ListView
from django.views.generic import DetailView

class PrizeListView(ListView):
    model=Prize

class PrizeDetailView(DetailView):
    model=Prize
