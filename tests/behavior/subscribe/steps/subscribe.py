from uuid import uuid4

from behave import *


@given("topic")
def step_impl(context):
    context.topic = str(uuid4())


@given("event handler")
def step_impl(context):
    def event_handler(event):
        pass

    context.event_handler = event_handler


@given("subscribed")
def step_impl(context):
    pass


@when("event occurred")
def step_impl(context):
    pass
