from ninja import NinjaAPI

api = NinjaAPI()

@api.get("dummy/")
def get_dummy(request):
    return { "message": "hello world!" }