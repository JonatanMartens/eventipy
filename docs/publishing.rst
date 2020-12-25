Publishing
==========

In order to publish events one can simply:

.. code-block:: python

    import asyncio
    from eventipy import events, Event

    event = Event("my-topic")
    asyncio.run(events.publish(event))  # Or await it in an async function

now every subscriber to ``my-topic`` will receive the event.
