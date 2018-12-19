import unittest
import socc

class TestSocc(socc.socc):
    """For Testing"""
    def __init__(self, socket):
        self._host = '127.0.0.1'
        self._port = 65535
        self.socket = socket

class FakeSocket():
    def __init__(self):
        self.message_queue = []
        self.cloase = False

    def recv(self, bufsize):
        if len(self.message_queue) == 0:
            self.message_queue.append(b'Empty\n')
        return self.message_queue.pop(0)

    def send(self, message):
        self.add_queue(message)

    def add_queue(self, message):
        self.message_queue.append(message)

    def get_queue(self):
        return self.message_queue

    def reset_queue(self):
        self.message_queue = []

    def close(self):
        self.close = True

class SoccTest(unittest.TestCase):
    def setUp(self):
        self.socket = FakeSocket()
        self.s = TestSocc(self.socket)

    def test_send_message(self):
        self.s.send('Message')
        self.assertEqual(self.socket.get_queue(), [b'Message\n'])

    def test_send_bytes(self):
        self.s.send_bytes(b'Message')
        self.assertEqual(self.socket.get_queue(), [b'Message\n'])

    def test_recv_message(self):
        self.socket.add_queue(b'Message\n')
        self.assertEqual(self.s.recv(), 'Message\n')

    def test_recv_message_bytes(self):
        self.socket.add_queue(b'Message\n')
        self.assertEqual(self.s.recv_bytes(), b'Message\n')

    def test_ignore(self):
        for i in range(0, 5):
            self.socket.add_queue(b'Message\n')
        self.socket.add_queue(b'Goal\n')
        self.s.ignore(5)
        self.assertEqual(self.s.recv(), 'Goal\n')

    def test_close(self):
        self.assertTrue(self.s.close)

if __name__ == '__main__':
    unittest.main()
