from tornado.gen import coroutine
from tornado.web import Application, RequestHandler
from tornado_sqlalchemy import as_future, make_session_factory, SessionMixin

class NativeCoroutinesRequestHandler(SessionMixin, RequestHandler):
    async def get(self):
        with self.make_session() as session:
            count = await as_future(session.query(UserModel).count)
        self.write('{} users so far!'.format(count))

class GenCoroutinesRequestHandler(SessionMixin, RequestHandler):
    @coroutine
    def get(self):
        with self.make_session() as session:
            count = yield as_future(session.query(UserModel).count)
        self.write('{} users so far!'.format(count))

class SynchronousRequestHandler(SessionMixin, RequestHandler):
    def get(self):
        with self.make_session() as session:
            count = session.query(UserModel).count()
        self.write('{} users so far!'.format(count))

handlers = (
    (r'/native-coroutines', NativeCoroutinesRequestHandler),
(r'/gen-coroutines', GenCoroutinesRequestHandler),
(r'/sync', SynchronousRequestHandler),
)

elephant_sql_api_key='2f7fa9e0-a47c-4a4e-b03c-7bc11af04f91'
postgre_url='postgres://nozzljfs:ebJHsuKPNzYJ5lWN_DNoqsERbCVeoC0s@baasu.db.elephantsql.com:5432/nozzljfs'
app = Application(
    handlers,
    session_factory=make_session_factory(postgre_url)
)

