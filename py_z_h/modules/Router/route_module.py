
class Route:

    routes = {}

    def __init__(self):
        pass

    @staticmethod
    def get(path,action):
        Route.routes[path] = action
        # print(Route.routes)
        # action()

    @staticmethod
    def apply(path):
        for route, action in Route.routes.items():
            if path == route:
                action()
                return

        raise FileNotFoundError


