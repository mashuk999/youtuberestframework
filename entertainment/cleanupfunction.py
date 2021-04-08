from firebase import Firebase
from django.http import HttpResponse, JsonResponse, Http404
def cleanupfunctions(request):
    firebaseConfig = {
        'apiKey': "AIzaSyBexTA9lK-ruTMWVWEFaAzSKuIrNBjZ7vs",
        'authDomain': "tiktokvideos-378aa.firebaseapp.com",
        'storageBucket': "tiktokvideos-378aa.appspot.com",
        "databaseURL": "https://tiktokvideos-378aa-default-rtdb.firebaseio.com/",
        "serviceAccount": "./service_account.json",
    }


    firebase = Firebase(firebaseConfig)
    storage = firebase.storage()
    return HttpResponse('okk')
    # b=storage.child('AllVideos/')
    # b.list_files()
    #
    #
    # print(b)
    # # b=storage.bucket(1)
    # # print(b)
    # print(storage)
    # # a=requests.get('https://tiktokvideos-378aa.appspot.com/AllVideos/')
    # # print(a)
    # # storage.get
    # # storage.delete('AllVideos/')