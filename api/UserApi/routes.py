from .userResource import UserResource

def init_routes(api):
    api.add_resource(UserResource,'/user/<email>')