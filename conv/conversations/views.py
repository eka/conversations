# Create your views here.
from conversations.forms import LoginForm, ConversationForm, ConversationMessageForm
from conversations.models import Conversation, Message
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated():
        return redirect('/conversations')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                user = User.objects.create_user(username)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
    return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))


@login_required
def conversation_list(request):
    form = ConversationForm()
    cs = Conversation.objects.all()
    if request.method == 'POST':
        form = ConversationForm(request.POST)
        if form.is_valid():
            ci = Conversation.objects.create(title=form.cleaned_data['title'])
            ci.users.add(request.user)
            return redirect('/conversations/%s' % ci.id)
    return render_to_response('conversations.html', {'form': form, 'conversations': cs}, context_instance=RequestContext(request))


@login_required
def conversation_get(request, cid):
    ci = get_object_or_404(Conversation, id=cid)
    form = ConversationMessageForm()
    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            msg = Message.objects.create(user=request.user, text=form.cleaned_data['text'])
            ci.messages.add(msg)
    return render_to_response('conversation.html', {'form': form, 'conversation': ci}, context_instance=RequestContext(request))
