#!/usr/bin/env python2
#encoding: UTF-8

#https://www.toptal.com/python/python-design-patterns
import this
"""
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

"""
Python is a dynamic and flexible language. Python design patterns are a great way of harnessing its vast potential
everything in Python is an object. Functions are objects, first class objects (whatever that means). This fact about functions being objects is important, so please remember it

Crux of design patterns
Program to an interface not an implementation.
Favor object composition over inheritance.
Duck Typing principal- program to an interface.
If it looks like a duck and quacks like a duck, it's a duck!
Teaching the ducks to type takes a while, but saves you a lot of work afterwards!
"""
try:
    bird.quack()
except AttributeError:
    self.lol()

"""
Favor object composition over inheritance
11 behavioural design patterns - not all are explicitely needed in python, most are implicit by nature of language
Chain of responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template, Visitor
"""
class User:
    _persist_methods = ['get', 'save', 'delete']

    def __init__(self, persister):
        self._persister = persister

    def __getattr__(self, attribute):
        if attribute in self._persist_methods:
            return getattr(self._persister, attribute)

#Chain of responsibility but best is single responsibilty
#Every piece of code must do one, and only one, thing.
#class that is responsible for filtering web contents at runtime
class ContentFilter(object):
    def __init__(self, filters=None):
        self._filters = list()
        if filters is not None:
            self._filters += filters

    def filter(self, content):
        for filter in self._filters:
            content = filter(content)
        return content

filter = ContentFilter([
                offensive_filter,
                ads_filter,
                porno_video_filter])
filtered_content = filter.filter(content)

"""
Command Pattern
the advantage is that encapsulating actions in such a way enables Python developers to add additional functionalities 
related to the executed actions, such as undo/redo, or keeping a history of actions and the like
"""
class RenameFileCommand(object):
    def __init__(self, from_name, to_name):
        self._from = from_name
        self._to = to_name

    def execute(self):
        os.rename(self._from, self._to)

    def undo(self):
        os.rename(self._to, self._from)
        
class History(object):
    def __init__(self):
        self._commands = list()

    def execute(self, command):
        self._commands.append(command)
        command.execute()

    def undo(self):
        self._commands.pop().undo()

history = History()
history.execute(RenameFileCommand('docs/cv.doc', 'docs/cv-en.doc'))
history.execute(RenameFileCommand('docs/cv1.doc', 'docs/cv-bg.doc'))
history.undo()
history.undo()

"""
Creational Patterns - not commonly used in Python. Why? Because of the dynamic nature of the language
Someone wiser than I once said that Factory is built into Python. It means that the language itself provides us with all the 
flexibility we need to create objects in a sufficiently elegant fashion; we rarely need to implement anything on top, like Singleton or Factory
In one Python Design Patterns tutorial, I found a description of the creational design patterns that stated these design 
“patterns provide a way to create objects while hiding the creation logic, rather than instantiating objects directly using a new operator.”
That pretty much sums up the problem: We don’t have a new operator in Python!
Nevertheless, let’s see how we can implement a few, should we feel we might gain an advantage by using such patterns.
"""
# singleton
"""
The Singleton pattern is used when we want to guarantee that only one instance of a given class exists during runtime. 
Do we really need this pattern in Python? Based on my experience, it’s easier to simply create one instance intentionally and 
then use it instead of implementing the Singleton pattern.
But should you want to implement it, here is some good news: In Python, we can alter the instantiation process (along with virtually anything else). 
Remember the __new__() method I mentioned earlier? Here we go:
"""
class Logger(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_logger'):
            cls._logger = super(Logger, cls
                    ).__new__(cls, *args, **kwargs)
        return cls._logger
"""
These are the alternatives to using a Singleton in Python: Use a module.
Create one instance somewhere at the top-level of your application, perhaps in the config file.
Pass the instance to every object that needs it. That’s a dependency injection and it’s a powerful

Dependency Injection
it’s a very good mechanism of implementing loose couplings, and it helps make our application maintainable and extendable. 
Combine it with Duck Typing and the Force will be with you. Always.
object is created outside. Better to say that the objects are not created at all where we use them, 
so the dependency is not created where it is consumed
analogy: Don’t get things to drink from the fridge yourself, state a need instead. Tell your parents that you need something to drink with lunch
"""
class Command:
    def __init__(self, authenticate=None, authorize=None):
        self.authenticate = authenticate or self._not_authenticated
        self.authorize = authorize or self._not_autorized

    def execute(self, user, action):
        self.authenticate(user)
        self.authorize(user, action)
        return action()

if in_sudo_mode:
    command = Command(always_authenticated, always_authorized)
else:
    command = Command(config.authenticate, config.authorize)
command.execute(current_user, delete_user_action)
# We inject the authenticator and authorizer methods in the Command class
#DI using properties in a class
command = Command()
if in_sudo_mode:
    command.authenticate = always_authenticated
    command.authorize = always_authorized
else:
    command.authenticate = config.authenticate
    command.authorize = config.authorize
command.execute(current_user, delete_user_action)

# Prototype, Builder and Factory design patterns.
"""
Structural Patterns: Facade
This may very well be the most famous Python design pattern.
Imagine you have a system with a considerable number of objects. Every object is offering a rich set of API methods. 
You can do a lot of things with this system, but how about simplifying the interface? 
Why not add an interface object exposing a well thought-out subset of all API methods? A Facade!
Facade is an elegant Python design pattern. It's a perfect way of streamlining the interface.
"""
class Car(object):
    def __init__(self):
        self._tyres = [Tyre('front_left'),Tyre('front_right'),Tyre('rear_left'),Tyre('rear_right'), ]
        self._tank = Tank(70)
    def tyres_pressure(self):
        return [tyre.pressure for tyre in self._tyres]
    def fuel_level(self):
        return self._tank.level
#There is no surprise, no tricks, the Car class is a Facade, and that’s all.


"""
Adapter
If Facades are used for interface simplification, Adapters are all about altering the interface. 
Like using a cow when the system is expecting a duck.    
I would say it is a well written method with dependency injection, which allows for great extensibility. 
Say you want to log to some UDP socket instead to a file,you know how to open this UDP socket but the only problem is
that the socket object has no write() method. You need an Adapter!
*master bridge and proxy design patterns
"""
import socket

class SocketWriter(object):

    def __init__(self, ip, port):
        self._socket = socket.socket(socket.AF_INET,
                                     socket.SOCK_DGRAM)
        self._ip = ip
        self._port = port

    def write(self, message):
        self._socket.send(message, (self._ip, self._port))

def log(message, destination):
    destination.write('[{}] - {}'.format(datetime.now(), message))

upd_logger = SocketWriter('1.2.3.4', '9999')
log('Something happened', udp_destination)

"""
Decorator
The decorator pattern is about introducing additional functionality and in particular, doing it without using inheritance.
achieved mostly by built-in Python functionality

"""
def execute(user, action):
    self.authenticate(user)
    self.authorize(user, action)
    return action()
# What is not so good here is that the execute function does much more than executing something. We are not following the single responsibility principle to the letter.
# We can implement any authorization and authentication functionality in another place, in a decorator, like so:
def execute(action, *args, **kwargs):
    return action()

def autheticated_only(method):
    def decorated(*args, **kwargs):
        if check_authenticated(kwargs['user']):
            return method(*args, **kwargs)
        else:
            raise UnauthenticatedError
    return decorated

def authorized_only(method):
    def decorated(*args, **kwargs):
        if check_authorized(kwargs['user'], kwargs['action']):
            return method(*args, **kwargs)
        else:
            raise UnauthorizeddError
    return decorated

execute = authenticated_only(execute)
execute = authorized_only(execute)
"""
Now the execute() method is:
Simple to read
Does only one thing (at least when looking at the code)
Is decorated with authentication & authorization
"""
# We write the same using Python’s integrated decorator syntax:
def autheticated_only(method):
    def decorated(*args, **kwargs):
        if check_authenticated(kwargs['user']):
            return method(*args, **kwargs )
        else:
            raise UnauthenticatedError
    return decorated


def authorized_only(method):
    def decorated(*args, **kwargs):
        if check_authorized(kwargs['user'], kwargs['action']):
            return method(*args, **kwargs)
        else:
            raise UnauthorizedError
    return decorated


@authorized_only
@authenticated_only
def execute(action, *args, **kwargs):
    return action()


from mymodule import rm
import mock
import unittest

class RmTestCase(unittest.TestCase):
    # we have fundamentally changed the way that the test operates. Now, we have an insider, an object we can use to verify the functionality of another.
    # Mock an item where it is used, not where it came from
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os):
        rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")

"""
Adding Validation to ‘rm’
The rm method defined earlier is quite oversimplified. We’d like to have it validate that a path exists and is a file before just blindly 
attempting to remove it. Let’s refactor rm to be a bit smarter:
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)
# Great. Now, let’s adjust our test case to keep coverage up.
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm
import mock
import unittest
class RmTestCase(unittest.TestCase):
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False
        rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True
        rm("any path")
        mock_os.remove.assert_called_with("any path")

# File-Removal as a Service with Mock Patch
from mymodule import RemovalService
import mock
import unittest
class RemovalServiceTestCase(unittest.TestCase):
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        # set up the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")


# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import os.path
# removal service is DI to uploaderService
class RemovalService(object):
    """A service for removing objects from the filesystem."""
    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)

class UploadService(object):
    def __init__(self, removal_service):
        self.removal_service = removal_service
    def upload_complete(self, filename):
        self.removal_service.rm(filename)


# Mocking Instance Methods

"""
Mocking simulates the existence and behavior of a real object, allowing software engineers to test code in various hypothetical 
scenarios without the need to resort to countless system calls. Mocking can thereby drastically improve the speed and efficiency of unit tests.

The mock library has a special method decorator for mocking object instance methods and properties, the @mock.patch.object decorator:
"""
from mymodule import RemovalService, UploadService
import mock
import unittest

class RemovalServiceTestCase(unittest.TestCase):
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        # set up the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")

class UploadServiceTestCase(unittest.TestCase):
    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)
        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")
        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded file")
        # check that it called the rm method of _our_ removal_service
        removal_service.rm.assert_called_with("my uploaded file")

"""
Mock Patch Pitfall: Decorator Order
When using multiple decorators on your test methods, order is important, and it’s kind of confusing. Basically, when mapping decorators to method parameters, work backwards. Consider this example:

    @mock.patch('mymodule.sys')
    @mock.patch('mymodule.os')
    @mock.patch('mymodule.os.path')
    def test_something(self, mock_os_path, mock_os, mock_sys):
        pass
Notice how our parameters are matched to the reverse order of the decorators? 
That’s partly because of the way that Python works With multiple method decorators, here’s the order of execution in pseudocode:
"""

Creating
Mock
Instances
Instead
of
mocking
the
specific
instance
method, we
could
instead
just
supply
a
mocked
instance
to
UploadService
with its constructor.I prefer option 1 above, as it’s a lot more precise, but there are many cases where option 2 might be efficient or necessary.Let’s refactor our test again:

# !/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import RemovalService, UploadService

import mock
import unittest


class RemovalServiceTestCase(unittest.TestCase):
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()
        # set up the mock
        mock_path.isfile.return_value = False
        reference.rm("any path")
        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")
        # make the file 'exist'
        mock_path.isfile.return_value = True
        reference.rm("any path")
        mock_os.remove.assert_called_with("any path")

class UploadServiceTestCase(unittest.TestCase):
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        mock_removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)
        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")
        # test that it called the rm method
        mock_removal_service.rm.assert_called_with("my uploaded file")



"""
Python Mock Example: Mocking a Facebook API Call
To finish up, let’s write a more applicable real-world python mock example, one which we mentioned in the introduction: posting a message to Facebook. We’ll write a nice wrapper class and a corresponding test case.
"""

import facebook


class SimpleFacebook(object):

    def __init__(self, oauth_token):
        self.graph = facebook.GraphAPI(oauth_token)

    def post_message(self, message):
        """Posts a message to the Facebook wall."""
        self.graph.put_object("me", "feed", message=message)


#         Here’s our test case, which checks that we post the message without actually posting the message:
import facebook
import simple_facebook
import mock
import unittest


class SimpleFacebookTestCase(unittest.TestCase):

    @mock.patch.object(facebook.GraphAPI, 'put_object', autospec=True)
    def test_post_message(self, mock_put_object):
        sf = simple_facebook.SimpleFacebook("fake oauth token")
        sf.post_message("Hello World!")

        # verify
        mock_put_object.assert_called_with(message="Hello World!")







if __name__ == "__main__":
    print("Hello World")



