## App middleware catalog
from django.shortcuts import redirect
from django.urls import reverse  ## Since a name it searches the url in the urls file

class ProfileCompletiontMiddleware:
    ## Ensures that every user in the platform have their picture and biography

    def __init__(self, get_response):    
        self.get_response = get_response
    
    def __call__(self, request):
        ## Code to be executed for each request before the view is called
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography: 
                    ## If the user has no a complete register it doesn't let their leave until their 
                    # complete the register with picture and biography
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')

        response = self.get_response(request)
        return response 
    