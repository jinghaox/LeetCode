class Solution(object):
    def __init__(self):
        self.num_dict = {"2":"abc",
                         "3": "def",
                         "4": "ghi",
                         "5": "jkl",
                         "6": "mno",
                         "7": "pqrs",
                         "8": "tuv",
                         "9": "wxyz"
                    }
    def LetterCombPhoneNum(self, digits):
        """
        :param digits:
        :return:

        when we see each letter of the first digit, i.e. a, b, c,
        we presume other digits have been combined already, i.e. 2nd digit 3, 3rd digit 4 have been combined

                             ""
         2:      a            b         c
         3:  d   e   f    d   e   f   d e f
         4: ghi ghi ghi

         first, path_so_far is "", then we loop with "abc"
         for a, we recursively append "d", "e", "f" to it
         then for b, we append "d", "e", "f" again
         then for c...
        """
        # don't use set(), otherwise the order is not well controlled
        combinations = list()
        def recurse(all_digits, path_so_far):
            if not all_digits: # if all_digits == "", then appending 
                combinations.append(path_so_far)
                return

            # split to first digit and other digits
            first, rest = all_digits[0], all_digits[1:]
            letters = self.num_dict[first] # e.g. for '2', it's 'abc'
            # loop the letters in the first digit
            # for each letter, recursively call this func for rest of the digits
            # append the current letter to the output path_so_far
            for letter in letters:
                print("append {} to path_so_far {}".format(letter, path_so_far))
                recurse(rest, path_so_far + letter)

        recurse(digits, "")
        return combinations

if __name__ == '__main__':
    s = Solution()
    res = s.LetterCombPhoneNum('23')
    print(res)



