import unittest
import puzzles.bowling.bowling_score as bowling_score


class BowlingScoreTest(unittest.TestCase):
    def test_strike(self):
        score_board = bowling_score.ScoreBoard()
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(3, 6))  # open
        print(f'the cumulative score is {score_board.cumul_score()}')
        # 1st frame: 10 + (3 + 6), 2nd frame: 3 + 6
        self.assertTrue(score_board.cumul_score() == 28)

    def test_double(self):
        score_board = bowling_score.ScoreBoard()
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(3, 6))  # open
        print('the cumulative score is {}'.format(score_board.cumul_score()))
        # 1st frame: 10 + 10 + 3, 2nd frame: 10 + 3 + 6, 3rd frame: 3 + 6
        self.assertTrue(score_board.cumul_score() == 51)

    def test_spare(self):
        score_board = bowling_score.ScoreBoard()
        score_board.add_frame(bowling_score.ScoreFrame(4, 6))
        score_board.add_frame(bowling_score.ScoreFrame(3, 7))
        print('the cumulative score is {}'.format(score_board.cumul_score()))
        # 1st: 4+6 + 3(bonus from 2nd frame); 2nd: 3 + 7 (it's also a spare,
        # but no 3rd frame yet).
        self.assertTrue(score_board.cumul_score() == 23)

    def test_frame_count(self):
        score_board = bowling_score.ScoreBoard()
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
        score_board.add_frame(bowling_score.ScoreFrame(10))  # strike

        try:
            score_board.add_frame(bowling_score.ScoreFrame(10))  # strike
            self.fail("shouldn't be here")
        except Exception as e:
            self.assertTrue(e.args[0] == 'cannot have greater than 10 frames')

    def test_slot_count(self):
        score_board = bowling_score.ScoreBoard()
        try:
            score_board.add_frame(bowling_score.ScoreFrame(1, 1, 3))  # strike
            self.fail("shouldn't be here")
        except Exception as e:
            self.assertTrue(e.args[0] == 'frame 10 cannot have slot 3 if the'
                                         ' first two slots have sum less than 10')

    def test_repr(self):
        bowling_frame = bowling_score.ScoreFrame(3, 6)
        print(bowling_frame)
        bf = repr(bowling_frame)
        print(bf)
        # implicitly used in eval
        from puzzles.bowling.bowling_score import ScoreFrame
        print(eval(bf))
