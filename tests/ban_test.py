from unittest.mock import MagicMock, patch, PropertyMock

import plugins.ban

from tests.corobo_test_case import CoroboTestCase


class TestBan(CoroboTestCase):

    def setUp(self):
        super().setUp((plugins.ban.Ban,))
        self.ban = self.load_plugin('Ban')
        self.ban.bot_config.ROOMS_TO_JOIN = (
                'coala/coala', 'coala/coala-bears')
        self.ban.bot_config.BOT_IDENTITY['token'] = 'mocked?'

    @patch('plugins.ban.requests')
    @patch('plugins.ban.json')
    def test_ban_cmd(self, mockjson, mockreq):
        status_mock = MagicMock()
        type(status_mock).status_code = PropertyMock(return_value=200)
        mockreq.post.return_value = status_mock

        fake_room_data = [
            {'id': '130', 'uri': 'coala/coala'},
            {'id': '234', 'name': 'Nitanshu'},
            {'id': '897', 'uri': 'coala/coala-bears'}
        ]
        testbot = self
        mockjson.loads.return_value = fake_room_data
        testbot.assertCommand('!ban @nvzard',
                              'nvzard has been banned from: coala/coala, '
                              'coala/coala-bears')
        testbot.assertCommand('!ban nvzard',
                              'nvzard has been banned from: coala/coala, '
                              'coala/coala-bears')

        mockjson.loads.return_value = []
        testbot.assertCommand('!ban @nvzard', 'No rooms found:(')

        mockjson.loads.return_value = fake_room_data
        status_mock = MagicMock()
        type(status_mock).status_code = PropertyMock(return_value=403)
        mockreq.post.return_value = status_mock

        with testbot.assertLogs() as cm:
            testbot.assertCommand('!ban @nvzard',
                                  'Error 403: '
                                  'Something went wrong:( Pls try again!')
            testbot.assertIn('INFO:errbot.plugins.Ban:'
                             'Error 403', cm.output)

    @patch('plugins.ban.requests')
    @patch('plugins.ban.json')
    def test_unban_cmd(self, mockjson, mockreq):
        status_mock = MagicMock()
        type(status_mock).status_code = PropertyMock(return_value=200)
        mockreq.delete.return_value = status_mock

        fake_room_data = [
            {'id': '130', 'uri': 'coala/coala'},
            {'id': '234', 'name': 'Nitanshu'},
            {'id': '897', 'uri': 'coala/coala-bears'}
        ]
        mockjson.loads.return_value = fake_room_data
        testbot = self
        testbot.assertCommand('!unban @nvzard',
                              'nvzard has been unbanned from: coala/coala, '
                              'coala/coala-bears')
        testbot.assertCommand('!unban nvzard',
                              'nvzard has been unbanned from: coala/coala, '
                              'coala/coala-bears')

        mockjson.loads.return_value = []
        testbot.assertCommand('!unban @nvzard', 'No rooms found:(')

        mockjson.loads.return_value = fake_room_data
        status_mock = MagicMock()
        type(status_mock).status_code = PropertyMock(return_value=403)
        mockreq.delete.return_value = status_mock

        with testbot.assertLogs() as cm:
            testbot.assertCommand('!unban @nvzard',
                                  'Error 403: '
                                  'Something went wrong:( Pls try again!')
            testbot.assertIn('INFO:errbot.plugins.Ban:'
                             'Error 403', cm.output)
