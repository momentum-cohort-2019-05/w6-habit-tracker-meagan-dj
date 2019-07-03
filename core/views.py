from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from core.forms import DailyRecordForm, ObserverForm, HabitForm
from core.models import DailyRecord,Observer,Habit
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def list_habits(request):
    """View function for listing a User's habits."""
    habits = request.user.habit_set.all()
    habits_observed = request.user.observer.habit_set.all()
    return render(request, 'core/habit_list.html', {'habits': habits, 'habits_observed': habits_observed})


@login_required
def habit_detail(request, pk):
    """View function for listing a specific habit."""
    habit = request.user.habit_set.filter(pk=pk).first()
    return render(request, 'core/habit_detail.html', {'habit': habit})


@login_required
def create_daily_record(request, pk):
    """View function for adding a new daily record to a habit."""
    habit = request.user.habit_set.filter(pk=pk).first()

    if request.method == 'POST':
        form = DailyRecordForm(request.POST)

        if form.is_valid():
            daily_record = DailyRecord(
                day_number = form.cleaned_data['day_number'],
                date = form.cleaned_data['date'],
                description = form.cleaned_data['description'],
                progress = form.cleaned_data['progress'],
                user = request.user,
                habit = habit
            )
            daily_record.save()
        
        return HttpResponseRedirect(reverse_lazy('habit-detail', kwargs = {'pk': pk}))

    else:
        form = DailyRecordForm()

    context = {
        'habit': habit,
        'form': form
    }

    return render(request, 'core/create_daily_record.html', context)


@login_required
def create_observer(request, pk):
    """View function for adding a new observer to a habit."""
    habit = request.user.habit_set.filter(pk=pk).first()

    if request.method == 'POST':
        form = ObserverForm(request.POST)

        if form.is_valid():
            # check if user is already an observer
            # if user is not an observer, make them an observer
            user = form.cleaned_data['user']

            if not hasattr(user, 'observer'):
                observer = Observer(
                    user = user
                )
                observer.save()
                habit.observers.add(observer)
            else:
                habit.observers.add(user.observer)

        return HttpResponseRedirect(reverse_lazy('habit-detail', kwargs = {'pk': pk}))

    else:
        form = ObserverForm()

    context = {
        'habit': habit,
        'form': form
    }

    return render(request, 'core/add_observer.html', context)



class EditDailyRecord(UpdateView):
    """Class-based view for editing the daily record"""
    model = DailyRecord 
    fields = '__all__'
    success_url = reverse_lazy('habit-list')


def index(request):
    return render(request, 'index.html')


@login_required
def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)

        if form.is_valid():
            habit = Habit(
                name = form.cleaned_data['name'],
                description = form.cleaned_data['description'],
                target = form.cleaned_data['target'],
                user = request.user,
            )
            habit.save()
        
        return HttpResponseRedirect(reverse_lazy('habit-detail', kwargs = {'pk': habit.pk}))

    else:
        form = HabitForm()

    context = {
        'form': form
    }

    return render(request, 'core/create_habit.html', context)



