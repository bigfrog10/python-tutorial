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

    TOP = 0
    UPPER_LEFT = 1
    UPPER_RIGHT = 2
    MIDDLE = 3
    LOWER_LEFT = 4
    LOWER_RIGHT = 5
    BOTTOM = 6


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
        # shift to the left to kill positions after
        mask_right = self._match_repr >> (MatchPosition.BOTTOM.value - position.value)
        # mask to kill positions before
        return mask_right & 1 == 1

    def set_match(self, position: MatchPosition):
        if self.has_match(position):
            return None

        # compute position in bits
        x = 1 << (MatchPosition.BOTTOM.value - position.value)
        new_digit = self._match_repr + x
        return match_to_digit.get(new_digit, None)

    def remove_match(self, position: MatchPosition):
        if not self.has_match(position):
            return None

        x = 1 << (MatchPosition.BOTTOM.value - position.value)
        new_digit = self._match_repr - x
        return match_to_digit.get(new_digit, None)

    def digit(self):
        return self._digit

    def all_matches(self):
        return [p for p in MatchPosition if self.has_match(p)]

    def _rep(self, c, d):
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