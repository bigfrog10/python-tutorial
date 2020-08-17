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


# map index to match digit representation
match_bin_digits = [
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


class MatchDigit:
    def __init__(self, digit: int):
        self._digit = digit
        self._match_repr = match_bin_digits[digit]

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

    def only_has_matches(self, positions):
        for p in MatchPosition:
            if p in positions:
                if not self.has_match(p):
                    return False
            else:
                if self.has_match(p):
                    return False

        return True

    def only_missing_matches(self, positions):
        for p in MatchPosition:
            if p in positions:
                if self.has_match(p):
                    return False
            else:
                if not self.has_match(p):
                    return False

        return True

    def all_matches(self):
        return [p for p in MatchPosition if self.has_match(p)]

    def digit(self):
        return self._digit

    @staticmethod
    def _rep(c, d):
        if c == '1':
            return d
        else:
            return ' '

    def __str__(self):
        bin_string = "{0:07b}".format(self._match_repr)
        ret = " " + self._rep(bin_string[0], '_') + ' ' + '\n'
        ret += self._rep(bin_string[1], '|') + ' ' + self._rep(bin_string[2], '|') + '\n'
        ret += " " + self._rep(bin_string[3], '-') + ' ' + '\n'
        ret += self._rep(bin_string[4], '|') + ' ' + self._rep(bin_string[5], '|') + '\n'
        ret += " " + self._rep(bin_string[6], '-') + ' ' + '\n'

        return ret


# used by set and take match
match_to_digit = {
    match_bin_digits[0]: MatchDigit(0),
    match_bin_digits[1]: MatchDigit(1),
    match_bin_digits[2]: MatchDigit(2),
    match_bin_digits[3]: MatchDigit(3),
    match_bin_digits[4]: MatchDigit(4),
    match_bin_digits[5]: MatchDigit(5),
    match_bin_digits[6]: MatchDigit(6),
    match_bin_digits[7]: MatchDigit(7),
    match_bin_digits[8]: MatchDigit(8),
    match_bin_digits[9]: MatchDigit(9)
}
