from events.models import Event,Participant, Schedule
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginP(request):
    
    if request.user.is_authenticated:
        user_email = request.user.email
        participant, _ = Participant.objects.get_or_create(email=user_email)
        return redirect('events')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                user_email = request.user.email
                participant, _ = Participant.objects.get_or_create(email=user_email)
                return redirect('events')
            else:
                messages.info(request,'Username or Password is incorrect')
        data = {}
        return render(request,'events/login.html',data)

def register(request):
    if request.user.is_authenticated:
        return redirect('events')
    else:
        form = CreateUserForm

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account is created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request,'events/register.html',context)

def logoutuser(request):
    logout(request)
    logged_in = False
    data = {
        'logged_in':logged_in
    }
    return redirect('events')


#@login_required(login_url='login')
def events(request):
    events = Event.objects.all()
    data = {'events':events}
    return render(request,'events/events.html',data)


@login_required(login_url='login')
def register_event(request , event_slug):
    selected_event = Event.objects.get(slug=event_slug)
    user_email = request.user.email
    
    if request.method == 'POST':
            participant, _ = Participant.objects.get_or_create(email=user_email)
            selected_event.participants.add(participant)

    return redirect('confirm_registration', event_slug=event_slug)


@login_required(login_url='login')
def deregister_event(request , event_slug):
    selected_event = Event.objects.get(slug=event_slug)
    user_email = request.user.email
    removed_participant = Participant.objects.get(email=user_email)
    selected_event.participants.remove(removed_participant)
    
    return redirect('schedule')



#@login_required(login_url='login')
def event_details(request , event_slug):
    selected_event = Event.objects.get(slug=event_slug)
    return render(request, 'events/event-details.html', {
                'event_found': True,
                'event': selected_event,
                
            })
    '''try:
        form = CreateUserForm
        selected_event = Event.objects.get(slug=event_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            form = CreateUserForm
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                #user_email = registration_form.cleaned_data['email']
                user_email = form.cleaned_data.get('email')
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_event.participants.add(participant)
                
                return redirect('confirm_registration', event_slug=event_slug)

        return render(request, 'events/event-details.html', {
                'event_found': True,
                'event': selected_event,
                'form': registration_form
            })
    except Exception as exc:
        return render(request, 'events/event-details.html', {
            'meetup_found': False
        })
    except Exception as exc:
        return render(request,'events/event-details.html',{
            'event_found': False
        })'''

@login_required(login_url='login')
def confirm_registration(request,event_slug):
    event = Event.objects.get(slug=event_slug)
    return render(request,'events/registration-success.html',{
        'organizer_email': event.organizer_email
    })

@login_required(login_url='login')
def schedule(request):
    #eventz = Event.objects.get(Participant=participant_slug)
    user_email = request.user.email
    participant = Participant.objects.get(email=user_email)
    events = participant.event_set.all()
    data = {'events':events}
    return render(request,'events/schedule.html',data)
