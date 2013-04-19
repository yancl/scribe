scribe_client
=============

A scribe client wrapper for facebook scribed(python version of twitter scribe client).

Usage
=============

Instantiate a client:

```python
from scribe_client import scribe_client
logger = scribe_client.Scribe()
logger.log('Test', 'Message')
```

You can also batch log to the scribed via the <tt>logger</tt> 

```python
from scribe_client import scribe_client
logger = scribe_client.Scribe()
with scribe_client.Batch(logger) as b:
    logger.log('Test', 'Message1')
    logger.log('Test', 'Message2')
    logger.log('Test', 'Message3')
```

Installation
=============

  sudo easy_install scribe_client

Contributing
=============

To contribute changes:

1. Fork the project
2. make your change, adding tests
3. send a pull request to me(@yancl)

Reporting problems
=============

The Github issue tracker is [here](http://github.com/yancl/scribe_client/issues).
