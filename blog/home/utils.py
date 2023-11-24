def is_user_logged_in(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username