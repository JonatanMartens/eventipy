Welcome to eventipy's documentation!
====================================

In-memory python event library.


Current version is |version|.


Library installation
====================

.. code-block:: bash

   $ pip install eventipy

Getting Started
===============

Publishing an event:

.. code-block:: python

    import asyncio
    from eventipy import events, Event

    event = Event(topic="my-topic")
    asyncio.run(events.publish(event))


Subscribing to a topic:

.. code-block:: python

    from eventipy import events

    @events.subscribe("my-topic")
    async def event_handler(event: Event):
        print(event.id)
        print(event.topic)

Dependencies
============

* dataclasses (for python 3.6 compatability)


Table Of Contents
=================
.. toctree::
   :maxdepth: 2

    Publishing events <publishing>
    Subscribing to topics <subscribing>
    Reference <reference>
