import datetime
from tornado.gen import coroutine
from tornado_sqlalchemy import as_future
from tornadoPractice.archive.models import Profile, Task
from tornadoPractice.archive.BaseView import *

class TaskListView(BaseView):
    """View for reading and adding new tasks."""
    SUPPORTED_METHODS = ("GET", "POST",)

    @coroutine
    def get(self, username):
        """Get all tasks for an existing user."""
        with self.make_session() as session:
            profile = yield as_future(session.query(Profile).filter(Profile.username == username).first)
            if profile:
                tasks = [task.to_dict() for task in profile.tasks]
                self.send_response({
                    'username': profile.username,
                    'tasks': tasks
                })
    @coroutine
    def post(self, username):
        """Create a new task."""
        with self.make_session() as session:
            profile = yield as_future(session.query(Profile).filter(Profile.username == username).first)
            if profile:
                due_date = self.form_data['due_date'][0]
                task = Task(
                    name=self.form_data['name'][0],
                    note=self.form_data['note'][0],
                    creation_date=datetime.now(),
                    due_date=datetime.strptime(due_date, '%d/%m/%Y %H:%M:%S') if due_date else None,
                    completed=self.form_data['completed'][0],
                    profile_id=profile.id,
                    profile=profile
                )
                session.add(task)
                self.send_response({'msg': 'posted'}, status=201)


