class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False
        seen_dot = False
        seen_exp = False
        digit_after_exp = True

        for i, ch in enumerate(s):

            # Digit
            if ch.isdigit():
                seen_digit = True

                if seen_exp:
                    digit_after_exp = True

            # Decimal point
            elif ch == '.':
                # Dot cannot appear twice or after exponent
                if seen_dot or seen_exp:
                    return False

                seen_dot = True

            # Exponent
            elif ch == 'e' or ch == 'E':
                # Exponent cannot appear twice
                # and must come after at least one digit
                if seen_exp or not seen_digit:
                    return False

                seen_exp = True
                digit_after_exp = False

            # Sign
            elif ch == '+' or ch == '-':
                # Sign is valid only at the beginning
                # or immediately after e/E
                if i != 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False

            # Anything else is invalid
            else:
                return False

        return seen_digit and digit_after_exp