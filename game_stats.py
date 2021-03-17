import json
class GameStats():

    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.filename = self.ai_settings.high_score_file
        self.reset_stats()
        self.game_active = False
        self.high_score = self.load_high_score()

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        try:
            with open(self.filename) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0
            with open(self.filename,'w') as f:
                json.dump(self.high_score,f)
        finally:
            return self.high_score

    def write_high_score(self,high_score):
        with open(self.filename,'w') as f:
            json.dump(high_score,f)