from django.shortcuts import render, redirect
from contrib import helper_functions
from contrib import operations


# Create your views here.
from home.forms import SearchForm


def home_page(request, *args, **kwargs):
    if request.method == 'POST':
        form = SearchForm(request.POST or None)
        print(form.is_valid())
        if form.is_valid():
            search_text = form.cleaned_data.get('search_text')
            num_tweets = form.cleaned_data.get('num_tweets')
            hashtag_list = search_text.strip().split(',')
            request.session['search_text_list'] = hashtag_list
            request.session['num_tweets'] = num_tweets
            return redirect(to='dashboard')
    else:
        form = SearchForm(request.POST or None)
    context = {
        'search_form': form,
    }
    return render(request, 'home/home-search.html', context=context)


def open_dashboard(request, *args, **kwargs):
    search_text_list = request.session.get('search_text_list')
    num_tweets = request.session.get('num_tweets')
    search_query = helper_functions.prepare_search_query(search_text_list, num_tweets)
    analysis_results = operations.call_sentiment_function(search_query=search_query)
    context = operations.create_context(analysis_results)
    context['search_text_list'] = search_text_list
    return render(request, 'home/dashboard.html', context)


def credits_page(request, *args, **kwargs):
    return render(request, 'home/credits.html')