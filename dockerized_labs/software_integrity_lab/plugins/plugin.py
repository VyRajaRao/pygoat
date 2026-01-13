# def run():
#     return "Safe plugin executed without integrity verification."
# def run():
#     return "🔥 MALICIOUS PLUGIN EXECUTED 🔥 Software integrity compromised."
def run(request):
    return {
        "status": "COMPROMISED",
        "leaked_user": request.user.username,
        "is_superuser": request.user.is_superuser,
        "session_id": request.session.session_key
    }
