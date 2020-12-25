Subscribing
===========

In order to subscribe to events:

.. code-block:: python

    from eventipy import events, Event

    @events.subscribe("my-topic")
    async def event_handler(event: Event):
        # Do something with event
        print(event.id)

every time that an event with topic ``my-topic`` is published, ``event_handler`` will be called.

You can also subscribe using a regular function (not async):

.. code-block:: python

    from eventipy import events, Event

    @events.subscribe("my-topic")
    def event_handler(event: Event):
        # Do something with event
        print(event.id)

Or without using a decorator like this:

.. code-block:: python

    from eventipy import events, Event

    async def event_handler(event: Event):
        # Do something with event
        print(event.id)

    events.subscribe("my-topic", event_handler)

This is useful if you don't want to subscribe right away.


Subscribing to all topics
-------------------------

In order to subscribe to all topics:

.. code-block:: python

    from eventipy import events, Event

    @events.subscribe_to_all
    async def event_handler(event: Event):
        # Do something with event
        print(event.id)

Without decorator:

.. code-block:: python

    from eventipy import events, Event

    async def event_handler(event: Event):
        # Do something with event
        print(event.id)

    events.subscribe_to_all(event_handler)


Internally this uses ``"*"`` as topic so:

.. code-block:: python

    from eventipy import events, Event

    @events.subscribe("*")
    async def event_handler(event: Event):
        # Do something with event
        print(event.id)


would also work, but is not recommended.
