from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject


def delete_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk) 
    subject.delete()
    return redirect('gpa_page')

def edit_subject(request, pk):
    subject = get_object_or_404(Subject, pk=pk)

    grades = ['A','A-','B+','B','B-','C+','C','C-','D+','D','F']

    if request.method == 'POST':
        subject.name = request.POST.get('name')
        subject.credits = int(request.POST.get('credits'))
        subject.letter_grade = request.POST.get('grade')
        subject.save()
        return redirect('gpa_page')

    return render(request, 'calculator/edit.html', {
        'subject': subject,
        'grades': grades,  
    })


def gpa_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        credits = int(request.POST.get('credits'))
        grade = request.POST.get('grade')

        Subject.objects.create(name=name, credits=credits, letter_grade=grade)
        return redirect('gpa_page')

    subjects = Subject.objects.all()

    total_points = 0
    total_credits = 0
    for s in subjects:
        total_points += s.grade_point * s.credits
        total_credits += s.credits

    gpa = round(total_points / total_credits, 2) if total_credits > 0 else 0

    return render(request, 'calculator/gpa.html', {'subjects': subjects, 'gpa': gpa})