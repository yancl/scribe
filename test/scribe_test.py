import sys
sys.path.insert(0, '../')

import os
import time
import subprocess
from nose.tools import raises, ok_, eq_

from scribe_client import scribe_client

class TestScribe(object):
    def setUp(self):
        self._category = 'Test'
        self._scribe = scribe_client.Scribe(servers=['127.0.0.1:11463'])
        #clear history data
        os.popen('echo "" > /tmp/scribetest/%s/%s_current' % (self._category, self._category))
        #start the scribed server
        self._popen = subprocess.Popen(['/usr/sbin/scribed', '-c', '../conf/scribe.conf'])
        time.sleep(1)

    def tearDown(self):
        self._popen.kill()
        self._popen.wait()

    def test_logging(self):
        self._scribe.log(self._category,'test logging')
        eq_('test logging', self._last_line(self._category))

    def test_batch(self):
        with scribe_client.Batch(self._scribe) as b:
            self._scribe.log(self._category,'test logging batch0')
            self._scribe.log(self._category,'test logging batch1')
            ok_('test logging batch1' != self._last_line(self._category))
        eq_('test logging batch1', self._last_line(self._category))

    def _last_line(self, category):
        time.sleep(3)
        return os.popen('tail -n1 /tmp/scribetest/%s/%s_current' % (category, category)).read().rstrip()
