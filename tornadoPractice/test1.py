# https://github.com/tornadoweb/tornado/blob/master/demos/blog/blog.py#L87

import json
from datetime import date

import tornado.escape
import tornado.httpclient
import tornado.ioloop
from tornado.web import Application, RequestHandler

SUPPORTED_METHODS = ("GET", "HEAD", "POST", "DELETE", "PATCH", "PUT", "OPTIONS")


class printApiList(RequestHandler):
    def initialize(self, apis):
        self.itList = apis

    def get(self):
        # self.write("hello apis: ")
        # self.write(self.itList)
        for k, v in self.itList.items():
            # print("APIs: ", k,v)
            self.write('<a href="' + v + '">API===>   ' + v + '</a><br/>')
        # self.set_header("Content-Type", "text/html")


class MainHandler(RequestHandler):
    def get(self):
        for i in range(10):
            self.write('<a href="/story/' + str(i + 1) + '/dp">Story Details ' + str(i + 1) + '</a>  '
                        '<a href="/storyparam?id=' + str(i + 1) + '&name=dp">Story Query Details ' + str(i + 1) + '</a><br/>')


class MainHandlerHello(RequestHandler):
    def get(self):
        self.write("Hello new Main Handler...")

class StoryHandlerQuery(RequestHandler):
    def get(self):
        id=self.get_argument("id")
        name=self.get_argument("name")
        self.write('this is story by query args, id: '+id+', name:'+name)


class StoryHandler(RequestHandler):
    def initialize(self, db):
        self.db = db
    def get(self,id,name):
        self.write("this is story " + str(self.path_kwargs)+'id:'+id+', name:'+name)


class VersionHandler(RequestHandler):
    def get(self):
        response = {'version': '3.6.10',
                    'last_build': date.today().isoformat()}
        self.write(response)


class GetGameByIdHandler(RequestHandler):
    def get(self, id):
        response = {'id': int(id),
                    'name': 'Crazy Game',
                    'release_date': date.today().isoformat()}
        self.write(response)


# this is like async -- await in ES6, non blocking IO concept
class getFullPageOrAPIHandler(RequestHandler):
    @tornado.gen.coroutine
    def get(self):
        http_client =tornado.httpclient.AsyncHTTPClient()
        # http_response = yield http_client.fetch("http://www.drdobbs.com/web-development")
        urlapi="https://jsonplaceholder.typicode.com/todos/"
        apiResponse = yield http_client.fetch(urlapi)
        response = apiResponse.body
        self.write(response)
        # self.set_header("Content-Type", "text/html")
        self.set_header("Content-Type", "application/json")


# class GetFullPageAsyncNewHandlerUsingDecorator(RequestHandler):
#     @asynchronous
#     def get(self):
#         http_client = tornado.httpclient.AsyncHTTPClient()
#         http_client.fetch("http://www.drdobbs.com/web-development", callback=self.on_fetch)
#
#     def on_fetch(self, http_response):
#         if http_response.error: raise HTTPError(500)
#         response = http_response.body.decode().replace("Most Recent Premium Content", "Most Recent Content")
#         self.write(response)
#         self.set_header("Content-Type", "text/html")
#         self.finish()

items = []


class ToDoItems(RequestHandler):
    def get(self):
        self.obj = json.load(self.request.body)
        items.append(self.obj)
        self.write({'msg': self.obj})

    def delete(self, id):
        global items
        new_items = [x for x in items if x['id'] is not int(id)]
        items = new_items
        # new_items = filter(lambda item: item['id'] != int(id), items)
        self.write({'message': id, 'left_items': new_items})


class ToDOAPI(RequestHandler):
    def get(self):
        items = [1, 2, 2, 3, 4]
        itemsObj = {'items': items}
        self.write(itemsObj)

def make_app():
    apisListMaster = []
    apisList = [
        (r"/", MainHandler),
        (r"/hello", MainHandlerHello),
        (r"/story/([0-9]+)/([^/]+)?", StoryHandler, dict(db={})),
        (r"/storyparam", StoryHandlerQuery),
        (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
        (r"/call2apiorhtml", getFullPageOrAPIHandler),
        (r"/version", VersionHandler),
        (r"/todo", ToDOAPI),
        (r"/todo/api/items/([^/]+)?", ToDoItems)
    ]
    keys = [i.__str__() for i, v in enumerate(apisList)]
    valuesApiList = [v[0] for v in apisList]
    printListObj = dict(zip(keys, valuesApiList))
    print("list of apis: ", printListObj)
    apisListMaster = apisList
    newObj = (r"/apis", printApiList, dict(apis=printListObj))
    apisListMaster.append(newObj)
    urls = apisListMaster
    print("urls", urls)
    return Application(urls, debug=True)  # with debug=true, its like a live update


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
