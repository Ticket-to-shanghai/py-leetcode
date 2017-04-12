# 1481 / 1481 test cases passed.
# Runtime: 115 ms


import re

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        regex = re.compile("^[ ]*[+-]?([0-9]+|[0-9]+[.]|[.][0-9]+|[0-9]+[.][0-9]+|[0-9]*[.]?[0-9]+[Ee][+-]?[0-9]+|[0-9]+[.]?[0-9]*[Ee][+-]?[0-9]+)[ ]*$")
        if not(regex.match(s)):
            return False
        return True
