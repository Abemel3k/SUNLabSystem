# lab_access/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AccessLog, User
from datetime import datetime

@csrf_exempt 
def log_access(request):
    if request.method == "POST":
        try:
            student_id = request.POST.get("student_id")
            action = request.POST.get("action")  

            if not student_id:
                return JsonResponse({"error": "Missing student ID"}, status=400)

            if not student_id.isdigit() or len(student_id) != 10:
                return JsonResponse({"error": "Invalid student ID format"}, status=400)

            try:
                user = User.objects.get(student_id=student_id)
            except User.DoesNotExist:
                return JsonResponse({"error": "Access Denied"}, status=403)

            if action not in ["entry", "exit"]:
                return JsonResponse({"error": "Invalid action"}, status=400)

            AccessLog.objects.create(user=user, action=action, timestamp=datetime.now())
            return JsonResponse({"message": "Access logged successfully"}, status=201)

        except Exception as e:
            print(f"Internal server error: {e}")
            return JsonResponse({"error": "Internal server error", "details": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)
