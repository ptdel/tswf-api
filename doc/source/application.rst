API
===

This documentation is for the backend functions behind the API, and does
not cover the API routes themselves in a fashion suitable for clint-side
code generation.

Blueprints
----------

Blueprints group http routes by prefix.  In the case of the API the only
currently prefix is ``/api``

.. automodule:: bp.routes
   :members:


Configurations
--------------

.. automodule:: config
   :members:


Error Handling
--------------

.. automodule:: errors
   :members:

.. automodule:: bp.error_handlers
   :members:


Playlist & Queue
----------------

.. automodule:: music_queue
   :members:

.. automodule:: skip
   :members:
