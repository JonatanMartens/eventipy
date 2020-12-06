Subscribing
===========

In order to subscribe to events:

.. code-block:: python

    from eventipy import events, Event

    @events.subscribe("my-topic")
    def event_handler(event: Event):
        # Do something with event
        print(event.id)

every time that an event with topic ``my-topic`` is published, ``event_handler`` will be called.

You can also subscribe without using a decorator like this:

.. code-block:: python

    from eventipy import events, Event

    def event_handler(event: Event):
        # Do something with event
        print(event.id)

    events.subscribe("my-topic", event_handler)

This is useful if you don't want to subscribe right away.
