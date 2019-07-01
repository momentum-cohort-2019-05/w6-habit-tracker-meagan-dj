from django.shortcuts import render

# Create your views here.
def list_habits(request):
    """View function for listing a User's habits."""
    habits = request.user.habit_set.all()
    return render(request, 'core/habit_list.html', {'habits': habits})


def habit_detail(request, pk):
    """View function for listing a specific habit."""
    habit = request.user.habit_set.filter(pk=pk).first()
    return render(request, 'core/habit_detail.html', {'habit': habit})