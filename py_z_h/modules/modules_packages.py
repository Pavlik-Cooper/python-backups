from Router.route_module import Route
from Router.HiWorld.hi_world_module import say_hi

from IndexController import IndexController



say_hi()

path = input("Enter address: ")



Route.get('/',IndexController.index)
Route.get('/about',IndexController.about)

Route.apply(path)




