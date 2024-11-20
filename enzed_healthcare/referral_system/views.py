from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Person, Referral
from .forms import PersonForm, ReferralForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
# Create your views here.

# Home
def home(request):
    return render(request, "referral_system/home.html")

#People
# List all people

@login_required
def person_list(request):
    people = Person.objects.all()
    return render(request, "referral_system/person_list.html", {"people": people})


# Detail page for a person
@login_required
def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, "referral_system/person_detail.html", {"person": person})


# Add new person
@login_required
def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("person_list")
    else:
        form = PersonForm()
    return render(request, "referral_system/person_form.html", {"form": form})


# Update person's details
@login_required
def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("person_list")
    else:
        form = PersonForm(instance=person)
    return render(request, "referral_system/person_form.html", {"form": form})


# Delete person
@login_required
def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        person.delete()
        return redirect("person_list")
    return render(request, "referral_system/person_confirm_delete.html", {"person": person})

# Referrals
# List all referrals
@login_required
def referral_list(request):
    referrals = Referral.objects.all()
    return render(request, "referral_system/referral_list.html", {"referrals": referrals})


# Detail page of referral
@login_required
def referral_detail(request, pk):
    referral = get_object_or_404(Referral, pk=pk)
    return render(request, "referral_system/referral_detail.html", {"referral": referral})


# Add new referral
@login_required
def referral_create(request):
    if request.method == "POST":
        form = ReferralForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("referral_list")
    else:
        form = ReferralForm()
    return render(request, "referral_system/referral_form.html", {"form": form})


# Update referral
@login_required
def referral_update(request, pk):
    referral = get_object_or_404(Referral, pk=pk)
    if request.method == "POST":
        form = ReferralForm(request.POST, instance=referral)
        if form.is_valid():
            form.save()
            return redirect("referral_list")
    else:
        form = ReferralForm(instance=referral)
    return render(request, "referral_system/referral_form.html", {"form": form})


# Delete referral
@login_required
def referral_delete(request, pk):
    referral = get_object_or_404(Referral, pk=pk)
    if request.method == "POST":
        referral.delete()
        return redirect("referral_list")
    return render(request, "referral_system/referral_confirm_delete.html", {"referral": referral})

