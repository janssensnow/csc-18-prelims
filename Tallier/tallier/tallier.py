class Tallier(object):
    def __init__(self):
        self.scores = {}

    def add_score(self, scores):
        self.scores[score.team_score] = team.points

    def get_score(self, team_score):
        return self.scores.get(team_score)