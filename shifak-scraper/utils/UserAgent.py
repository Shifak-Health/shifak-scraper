import json
import os
import random
import constants

class UserAgent:
    def __init__(self):
        self.user_agents = self.load(file=os.path.join(constants.HOME_DIR, 'config/agents.json'))

    @staticmethod
    def load(file):
        with open(file) as fp:
            data = json.load(fp)
        if not data:
            print("Empty {} file".format(file))
            raise
        return data['browsers']

    def user_agent(self):
        browser = random.choice([*self.user_agents])
        return random.choice(self.user_agents[browser])