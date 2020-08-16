# https://blog.csdn.net/iteye_15612/article/list/1
from functools import reduce


class ScoreFrame:
    STRIKE = 2
    SPARE = 1
    OPEN = 0

    def __init__(self, slot1: int, slot2: int = 0, slot3: int = 0):
        self.slot1 = slot1
        self.slot2 = slot2
        self.slot3 = slot3

        if slot1 + slot2 < 10 and slot3 > 0:
            raise Exception('frame 10 cannot have slot 3 if the first two slots'
                            ' have sum less than 10')

        self.score = slot1 + slot2 + slot3

        self.bonus = ScoreFrame.OPEN
        if slot1 == 10:
            self.bonus = ScoreFrame.STRIKE
        elif slot1 + slot2 == 10:
            self.bonus = ScoreFrame.SPARE

    def __repr__(self):
        # does not have bonus/score because of the __init__
        # contract with eval (they are opposites) -> eval(repr())
        return 'bowling_score.ScoreFrame({}, {}, {})'.format(self.slot1,
                                                             self.slot2,
                                                             self.slot3)

    def __str__(self):
        return 'ScoreFrame(slot1={}, slot2={}, slot3={}, bonus={}, score={})'\
            .format(self.slot1, self.slot2, self.slot3, self.bonus, self.score)

    def is_strike(self):
        return self.bonus == ScoreFrame.STRIKE

    def is_spare(self):
        return self.bonus == ScoreFrame.SPARE


class ScoreBoard:
    def __init__(self):
        self.frames = []
        self.index = 0

    def add_frame(self, bowling_frame: ScoreFrame):
        if self.index > 9:
            raise Exception("cannot have greater than 10 frames")

        self.frames.append(bowling_frame)

        # try to set bonus for two frames back in case of a strike there.
        p2 = self.index - 2
        if p2 >= 0:
            f2 = self.frames[p2]
            if f2.is_strike():
                f1 = self.frames[self.index - 1]
                if f1.is_strike():
                    f2.score += f1.score + bowling_frame.slot1

        # try to set bonus for previous frame in case of a spare there.
        p1 = self.index - 1
        if p1 >= 0:
            f1 = self.frames[p1]
            if f1.is_spare():
                f1.score += bowling_frame.slot1
            elif f1.is_strike() and not bowling_frame.is_strike():
                f1.score += bowling_frame.slot1 + bowling_frame.slot2

        self.index += 1

    def cumul_score(self):
        scores = [x.score for x in self.frames]
        return reduce(lambda a, b: a + b, scores)
