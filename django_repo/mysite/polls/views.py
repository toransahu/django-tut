from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
from .models import Question
from django.http import Http404
from django.urls import reverse
from django.views import generic

# Create your views here.

'''
#normal
def index(request):
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    output=','.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


#version 1 of index: to use template
def index(request):
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context ={
        'latest_question_list':latest_question_list,
        }
    return HttpResponse(template.render(context,request))
'''

'''
#version 2 of index:  
#Shortcut: to use template & render() (no need to import HttpResponse & loader
def index(request):
    latest_question_list= Question.objects.order_by('-pub_date')[:5]
    context ={
        'latest_question_list':latest_question_list,
        }
    return render(request,'polls/index.html',context)

'''

#version 3 of index: Used Generic Views (display a list of objects)

class IndexView(generic.ListView):
    template_name='polls/index.html' #defualt variable
    context_object_name='latest_question_list' #defualt variable

    #for ListView, the automatically generated context variable is "question_list". To override this we provide the context_object_name attribute, specifying that we want to use "latest_question_list" instead.

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]



'''
#version 1 of detail: 
#1. added Http404
#2. removed HttpResponse, used render shortcut & added detail.html template
def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        #1.
        raise Http404("Question does not exist")
    #2 return HttpResponse("You're looking at question %s." % question_id)
    return render(request, 'polls/detail.html',{'question':question})
'''

'''
#version 2 of detail: 
# used shortcut for http404 handling "get_object_or_404"
def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, 'polls/detail.html',{'question':question})
'''

#version 3 of detail: Implemented Generic Views (display a detail page for a particular type of object)

class DetailView(generic.DetailView):
    model=Question #default var model tells DetailView to work on a particular model object
    template_name='polls/detail.html' #default var, tells to do not autogenerate template & pick specific template
    #By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html
    #For DetailView the question variable is provided automatically – since we’re using a Django model (Question)
    
'''
#version 1 of results
def results(request, question_id):
    #1 response= "You're looking at the results of question %s."
    #1 return HttpResponse(response % question_id)
    question = get_object_or_404(Question,pk=question_id)
    return render (request, 'polls/results.html',{'question':question})
'''

#version 2 of results: Implemented Generic Views (display a detail page for a particular type of object)

class ResultsView(generic.DetailView):
    model=Question
    template_name='polls/results.html'

#No any suitable Generic view
#implementation pending: avoid race condition using F()
def vote(request, question_id):
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request,'polls/details.html',{'question':question,
                                                    'error_message':"You didn't select a choice.",}
                      )
    #ELSE used here is just for beautification and alignment, it continues the TRY block
    else:
        selected_choice.votes+=1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
    
        #return HttpResponse("You're voting on question %s." % question_id)
