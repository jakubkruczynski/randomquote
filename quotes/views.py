from django.shortcuts import render, redirect, get_object_or_404
from .models import Quote, FavouriteQuote
from django.contrib.auth.decorators import login_required
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.contrib import messages


def random_quote(request):
    count = Quote.objects.count()
    random_quote = None
    if count > 0:
        random_index = random.randint(0, count - 1)
        random_quote = Quote.objects.all()[random_index]
    return render(request, 'random_quote.html', {'quote': random_quote})


@login_required
def toggle_favourite(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    favourite, created = FavouriteQuote.objects.get_or_create(user=request.user, quote=quote)

    if created:
        action = 'added'
        messages.success(request, 'Quote added to favorites.')
    else:
        pass
    return redirect('random_quote')  # Redirect to the random_quote view


@login_required
def favourite_quotes(request):
    favourites_list = FavouriteQuote.objects.filter(user=request.user)
    page = request.GET.get('page', 1)

    paginator = Paginator(favourites_list, 2)  # Show 2 favourites per page

    try:
        favourites = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        favourites = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        favourites = paginator.page(paginator.num_pages)

    return render(request, 'favourite_quotes.html', {'favourites': favourites})

@login_required
def remove_favourite(request, favourite_id):
    favourite = get_object_or_404(FavouriteQuote, id=favourite_id, user=request.user)
    favourite.delete()
    messages.success(request, 'Removed from favourites')
    return redirect('favourite_quotes')



