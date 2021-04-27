import requests
import json

from errbot import BotPlugin, botcmd


class Ban(BotPlugin):
    """
    Ban/Unban from all rooms at once.
    """
    @botcmd(split_args_with=None,
            admin_only=True)
    def ban(self, msg, args):
        """
        Ban a user from all Gitter rooms at once.
        corobo ban <@username/username>
        """
        sinner = args[0]

        if sinner.startswith('@'):
            sinner = sinner[1:]

        joined_rooms = self.bot_config.ROOMS_TO_JOIN
        self.log.info(joined_rooms)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.bot_config.BOT_IDENTITY['token']
        }
        data = json.dumps({"username": sinner})

        r = requests.get('https://api.gitter.im/v1/rooms', headers=headers)
        room_data = json.loads(r.text)
        self.log.info(room_data)
        banned_rooms = []

        if room_data == []:
            yield 'No rooms found:('
        else:
            for room in filter(lambda x: x.get('uri', None) in joined_rooms,
                               room_data):
                url = 'https://api.gitter.im/v1/rooms/' + room['id'] + '/bans'
                rq = requests.post(url, data=data, headers=headers)
                self.log.info(rq.status_code)
                self.log.info(rq.json())

                if rq.status_code == 200:
                    banned_rooms.append(room['uri'])
                else:
                    self.log.info('Error ' + str(rq.status_code))
                    yield 'Error ' + str(rq.status_code) + \
                          ': Something went wrong:( Pls try again!'

            yield sinner + ' has been banned from: ' + ', '.join(banned_rooms)

    @botcmd(split_args_with=None,
            admin_only=True)
    def unban(self, msg, args):
        """
        Unban a user from all Gitter rooms at once.
        corobo unban <@username/username>
        """
        sinner = args[0]

        if sinner.startswith('@'):
            sinner = sinner[1:]

        joined_rooms = self.bot_config.ROOMS_TO_JOIN
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.bot_config.BOT_IDENTITY['token']
        }

        r = requests.get('https://api.gitter.im/v1/rooms', headers=headers)
        room_data = json.loads(r.text)
        unbanned_rooms = []

        if room_data == []:
            yield 'No rooms found:('
        else:
            for room in filter(lambda x: x.get('uri', None) in joined_rooms,
                               room_data):
                url = 'https://api.gitter.im/v1/rooms/' + \
                    room['id'] + '/bans/' + sinner
                rq = requests.delete(url, headers=headers)
                if rq.status_code == 200:
                    unbanned_rooms.append(room['uri'])
                else:
                    self.log.info('Error ' + str(rq.status_code))
                    yield 'Error ' + str(rq.status_code) + \
                          ': Something went wrong:( Pls try again!'

            yield sinner + ' has been unbanned from: ' + \
                ', '.join(unbanned_rooms)
