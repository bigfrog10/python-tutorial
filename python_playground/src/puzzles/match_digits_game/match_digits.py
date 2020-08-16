# https://blog.csdn.net/iteye_15612/article/details/81725865
import enum


class MatchPosition(enum.Enum):
    #           TOP
    #            _
    # UPPERLEFT | | UPPERRIGHT
    # MIDDLE     -
    # LOWERLEFT | | LOWERRIGHT
    #            -
    #          BOTTOM

    TOP         = 0b1000000
    UPPER_LEFT  = 0b0100000
    UPPER_RIGHT = 0b0010000
    MIDDLE      = 0b0001000
    LOWER_LEFT  = 0b0000100
    LOWER_RIGHT = 0b0000010
    BOTTOM      = 0b0000001


class MatchDigit:
    # map index to match digit representation
    match_repr = [
        0b1110111,
        0b0010010,
        0b1011101,
        0b1011011,
        0b0111010,
        0b1101011,
        0b1101111,
        0b1010010,
        0b1111111,
        0b1111011
    ]

    def __init__(self, digit: int):
        self._digit = digit
        self._match_repr = self.match_repr[digit]

    def has_match(self, position: MatchPosition):
        return self._match_repr & position.value == position.value

    def set_match(self, position: MatchPosition):
        if self.has_match(position):
            return None

        new_digit = self._match_repr + position.value
        return match_to_digit.get(new_digit, None)

    def remove_match(self, position: MatchPosition):
        if not self.has_match(position):
            return None

        new_digit = self._match_repr - position.value
        return match_to_digit.get(new_digit, None)

    def digit(self):
        return self._digit

    def all_matches(self):
        return [p for p in MatchPosition if self.has_match(p)]

    @staticmethod
    def _rep(c, d):
        if c == '1':
            return d
        else:
            return ' '

    def __str__(self):
        bin_string = "{0:07b}".format(self._match_repr)
        ret = " " + self._rep(bin_string[0], '_') + '\n'
        ret += self._rep(bin_string[1], '|') + ' ' + self._rep(bin_string[2], '|') + '\n'
        ret += " " + self._rep(bin_string[3], '-') + '\n'
        ret += self._rep(bin_string[4], '|') + ' ' + self._rep(bin_string[5], '|') + '\n'
        ret += " " + self._rep(bin_string[6], '-') + '\n'

        return ret


# used by set and take match
match_to_digit = {
    0b1110111: MatchDigit(0),
    0b0010010: MatchDigit(1),
    0b1011101: MatchDigit(2),
    0b1011011: MatchDigit(3),
    0b0111010: MatchDigit(4),
    0b1101011: MatchDigit(5),
    0b1101111: MatchDigit(6),
    0b1010010: MatchDigit(7),
    0b1111111: MatchDigit(8),
    0b1111011: MatchDigit(9)
}
