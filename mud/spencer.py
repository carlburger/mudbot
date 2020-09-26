import yaml
import random

class Spencer:
    def __init__(self):
        self.spencer_quotes = []
        with open('data/spencer.yml', 'r', encoding='utf8') as stream:
            try:
                yaml_content = yaml.safe_load(stream)
                if yaml_content:
                    self.spencer_quotes = yaml_content['quotes']
            except yaml.YAMLError as exc:
                print(exc)
    
    async def on_message(self, message):
        if message.content == 'mud spencer':
            response = random.choice(self.spencer_quotes)
            await message.channel.send(response)