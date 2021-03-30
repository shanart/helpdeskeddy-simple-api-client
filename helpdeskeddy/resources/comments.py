from .abstract import Resource

class Comments(Resource):

    def __init__(self, client=None):
        self.client = client

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass
    
    def delete(self):
        pass