Publishing
==========

In order to publish events one can simply:

.. code-block:: python

    from eventipy import events, Event

    event = Event("my-topic")
    events.publish(event)

now every subscriber to ``my-topic`` will receive the event.
