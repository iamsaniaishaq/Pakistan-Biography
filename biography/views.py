from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import PrimeMinisters
from .forms import PrimeMinisterForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PrimeMinisters
from .serializers import PrimeMinistersSerializer
from rest_framework import status

# Check if the user is an admin
def is_admin(user):
    return user.is_staff

# Prime Ministers List View
@login_required
@user_passes_test(is_admin)
def prime_ministers_list(request):
    prime_ministers = PrimeMinisters.objects.all()
    return render(request, 'prime_ministers_list.html', {'prime_ministers': prime_ministers})

# Prime Minister Detail View
@login_required
@user_passes_test(is_admin)
def prime_minister_detail(request, pk):
    prime_minister = get_object_or_404(PrimeMinisters, pk=pk)
    return render(request, 'prime_minister_detail.html', {'prime_minister': prime_minister})

# Add Prime Minister View (admin only)
@login_required
@user_passes_test(is_admin)
def add_prime_minister(request):
    if request.method == 'POST':
        name = request.POST['name']
        english_bio = request.POST.get('english_bio', '')
        urdu_bio = request.POST.get('urdu_bio', '')
        english_achievements = request.POST.get('english_achievements', '')
        urdu_achievements = request.POST.get('urdu_achievements', '')
        youtube_link = request.POST.get('youtube_link', '')
        background_color = request.POST['background_color']
        term = request.POST['term']
        image = request.FILES.get('image')  # Handles file upload

        prime_minister = PrimeMinisters(
            name=name,
            english_bio=english_bio,
            urdu_bio=urdu_bio,
            english_achievements=english_achievements,
            urdu_achievements=urdu_achievements,
            youtube_link=youtube_link,
            background_color=background_color,
            term=term,
            image=image,
        )
        prime_minister.save()
        return redirect('prime_ministers_list')  # Adjust to your actual redirect

    return render(request, 'add_prime_minister.html')

@login_required
@user_passes_test(is_admin)
def edit_prime_minister(request, pk):
    prime_minister = PrimeMinisters.objects.get(pk=pk)
    if request.method == 'POST':
        prime_minister.name = request.POST['name']
        prime_minister.english_bio = request.POST.get('english_bio', '')
        prime_minister.urdu_bio = request.POST.get('urdu_bio', '')
        prime_minister.english_achievements = request.POST.get('english_achievements', '')
        prime_minister.urdu_achievements = request.POST.get('urdu_achievements', '')
        prime_minister.youtube_link = request.POST.get('youtube_link', '')
        prime_minister.background_color = request.POST['background_color']
        prime_minister.term = request.POST['term']
        if 'image' in request.FILES:
            prime_minister.image = request.FILES['image']  # Update image if new one is uploaded

        prime_minister.save()
        return redirect('prime_ministers_list')  # Adjust to your actual redirect

    return render(request, 'edit_prime_minister.html', {'prime_minister': prime_minister})

# Delete Prime Minister View (admin only)
@login_required
@user_passes_test(is_admin)
def delete_prime_minister(request, pk):
    prime_minister = get_object_or_404(PrimeMinisters, pk=pk)
    if request.method == "POST":
        prime_minister.delete()
        return redirect('prime_ministers_list')
    return render(request, 'delete_prime_minister.html', {'prime_minister': prime_minister})

class PrimeMinistersListView(APIView):
    def get(self, request):
        prime_ministers = PrimeMinisters.objects.all()  # Fetch all prime ministers
        serializer = PrimeMinistersSerializer(prime_ministers, many=True)  # Serialize the data
        return Response(serializer.data)  # Return the serialized data as JSON
    
class PrimeMinisterDetailView(APIView):
    def get(self, request, id):
        try:
            prime_minister = PrimeMinisters.objects.get(id=id)  # Fetch the specific prime minister by ID
            serializer = PrimeMinistersSerializer(prime_minister)  # Serialize the data
            return Response(serializer.data)  # Return the serialized data as JSON
        except PrimeMinisters.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)  # Return 404 if not found