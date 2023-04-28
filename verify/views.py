from django.shortcuts import render
from .models import Student, Cotes, Recours
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
# Create your views here.
@login_required
def home(request):
    return render(request, 'verify/index.html')




@login_required
def view_cotes(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            student = Student.objects.get(code=code)
        except Student.DoesNotExist:
            msg = messages.error(request, 'Code invalide.')
            return redirect('verify:home')
        
        if student.user != request.user:
            msg = messages.error(request, "Vous n'êtes pas autorisé à accéder aux résultats de cet étudiant.")
            return redirect('verify:home')
        
        cotes = Cotes.objects.filter(student=student)
        recours = Recours.objects.filter(etudiant = student)
       
        context = {
            'student': student,
            'cotes': cotes, 
            'recours' : recours           
        }
    
    return render(request, 'verify/result.html', context)


@login_required
def deposer_recours(request, cotes_id):
    cotes = Cotes.objects.get(id=cotes_id)

    if request.method == 'POST':
        # Traiter le formulaire
        raison = request.POST.get('raison')
        nom = request.POST.get('nom')
        # Récupérer l'étudiant correspondant à l'utilisateur connecté
        etudiant, created = Student.objects.get_or_create(user=request.user)
        # Enregistrer le recours dans la base de données
        recours = Recours(etudiant=etudiant, point=cotes.cote, cours = nom , raison=raison)
        recours.save()
        messages.success(request, 'Votre recours a été envoyé avec succès.')
        return redirect(reverse('verify:home'))
        
    return render(request, 'verify/result.html')