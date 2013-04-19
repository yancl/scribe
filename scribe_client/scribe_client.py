from thrift_client import ThriftClient
from scribe import scribe

class Batch(object):
    __slots__ = '_scribe_ins'
    def __init__(self, scribe_ins):
        self._scribe_ins = scribe_ins

    def __enter__(self):
        self._scribe_ins._bucket = []
        return True

    def __exit__(self, *args):
        self._scribe_ins._commit_bucket()
        self._scribe_ins._bucket = None
        return False

class Scribe(object):
    __slots__ = '_client', '_add_newlines', '_bucket'
    def __init__(self, servers=['127.0.0.1:1463'], add_newlines=True, options={}):
        self._add_newlines = add_newlines
        self._client = ThriftClient(client_class=scribe.Client, servers=servers, options=options)
        self._bucket = None

    def log(self, category, message):
        if self._add_newlines:
            message = message + '\n'
        if self._bucket is not None:
            self._bucket.append(scribe.LogEntry(category=category, message=message))
        else:
            self._client.Log(messages=[scribe.LogEntry(category=category, message=message)])

    def _commit_bucket(self):
        if self._bucket:
            self._client.Log(messages=self._bucket)
