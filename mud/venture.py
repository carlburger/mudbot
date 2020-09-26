import random

class Venture:
    def __init__(self):
        self.responses = {
            'venture': 'Ihr müsst eure Gruppe erst sammeln.',
            'sammeln': 'Noch nicht, Abenteurer!'
        }
    
    async def on_message(self, message):
        for keyword in self.responses:
            if message.content == f'mud {keyword}':
                response = self.responses[keyword]
                await message.channel.send(response)