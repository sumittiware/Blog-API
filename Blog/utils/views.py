from django.http import JsonResponse

def error_404(request,exception):

    response = JsonResponse(
        {
            'message':'The endpoint is not found',
            'status':404
        }
    )
    response.status_code=404

    return response


def error_500(request):
    
    response = JsonResponse(
        {
            'messege':"Internal Server Error!!",
            'status':500
        }
    )
    response.status_code=500

    return response