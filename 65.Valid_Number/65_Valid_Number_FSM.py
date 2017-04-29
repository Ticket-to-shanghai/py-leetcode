# 1481 / 1481 test cases passed.
# Runtime: 62 ms

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        current_state = 0
        current_char = 0
        next_state = 0
        fsm = [[0, 1, 2, 3, -1],
               [6, 1, 7, -1, 4],
               [-1, 5, -1, -1, -1],
               [-1, 9, 2, -1, -1],
               [-1, 8, -1, 10, -1],
               [6, 5, -1, -1, 4],
               [6, -1, -1, -1, -1],
               [6, 7, -1, -1, 4],
               [6, 8, -1, -1, -1],
               [6, 9, 7, -1, 4],
               [6, 11, -1, -1, -1],
               [6, 11, -1, -1, -1]]
        good_state = [1, 5, 6, 7, 8, 9, 11]
        return_boolean = False
        for i, char in enumerate(s):
            if char == ' ':
                current_char = 0
            elif char.isdigit():
                current_char = 1
            elif char == '.':
                current_char = 2
            elif char == '+' or char == '-':
                current_char = 3
            elif char == 'e':
                current_char = 4
            else:
                return False
            next_state = fsm[current_state][current_char]
            if next_state in good_state:
                return_boolean = True
            else:
                return_boolean = False
            if next_state == -1:
                return_boolean = False
                return return_boolean
            current_state = next_state
        return return_boolean
