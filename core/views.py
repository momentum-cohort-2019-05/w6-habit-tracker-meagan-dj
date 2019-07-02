from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from core.forms import DailyRecordForm
from core.models import DailyRecord
from django.views.generic.edit import UpdateView


# Create your views here.
def list_habits(request):
    """View function for listing a User's habits."""
    habits = request.user.habit_set.all()
    habits_observed = request.user.observer.habit_set.all()
    return render(request, 'core/habit_list.html', {'habits': habits, 'habits_observed': habits_observed})


def habit_detail(request, pk):
    """View function for listing a specific habit."""
    habit = request.user.habit_set.filter(pk=pk).first()
    return render(request, 'core/habit_detail.html', {'habit': habit})


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


class EditDailyRecord(UpdateView):
    """Class-based view for editing the daily record"""
    model = DailyRecord 
    fields = '__all__'
    success_url = reverse_lazy('habit-list')
