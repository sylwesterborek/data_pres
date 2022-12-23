from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from .models import Dane
from .forms import DanesForm

from django.core.paginator import Paginator #import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


def data_list(request):
    searchTerm = request.GET.get('searchData')
    if searchTerm:
        danes = Dane.objects.filter(teryt__icontains=searchTerm)
        paginator = Paginator(danes, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

    else:
        danes = Dane.objects.all().order_by('teryt')
        paginator = Paginator(danes, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
#    return render(request, 'Data_list.html',
#                  {'searchTerm': searchTerm, 'danes': danes, })
    return render(request, 'Data_list.html',
                  {'searchTerm': searchTerm,'danes':page_obj })


def detail(request, dane_id):
    danes = get_object_or_404(Dane, pk=dane_id)
    return render(request, 'detail.html', {'danes': danes})

##

@login_required
def createdanes(request):
    #danes = get_object_or_404(Dane)
    if request.method == 'GET':
        return render(request, 'createdanes.html', {'form': DanesForm()})
    else:
        try:
            form = DanesForm(request.POST)
            #newDanes = form.save()
            #####
            #Review.user = request.user
            #newReview.movie = movie
            form.save()
            return redirect('data_list')

#            return redirect('detail',newReview.movie.id)
        except ValueError:
            return render(request, 'createdanes.html',
                          {'form': DanesForm(), 'error': 'bad data passed in'})

@login_required
def updatedanes(request, dane_id):
    #    danes = get_object_or_404(Dane,pk=danes_id,user=request.user)
    danes = get_object_or_404(Dane, pk=dane_id)
    if request.method == 'GET':
        form = DanesForm(instance=danes)
        return render(request, 'updatedanes.html', {'danes': danes, 'form': form})
    else:
        try:
            form = DanesForm(request.POST, instance=danes)
            form.save()
            return redirect('data_list')
        except ValueError:
            return render(request, 'updatedanes.html',
                          {'danes': danes, 'form': form, 'error': 'Bad data in form'})
        except OverflowError:
            return render(request, 'updatedanes.html',
                          {'danes': danes, 'form': form, 'error': 'Bad data in form OVERFLOW'})

@login_required
def deletedanes(request, dane_id):
    danes = get_object_or_404(Dane, pk=dane_id)
    if request.method == 'POST':
        danes.delete()
        return redirect('data_list')

    return render(request, 'deletedanes.html', {'danes': danes})
#    return redirect('data_list')
#    return redirect('confirm_delete_danes.html')
