'''
Leetcode URL: https://leetcode.com/problems/most-common-word/
Problem: Most Common Word, 819
Level: Easy
'''
import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        _paragraph = re.sub('[\W]', ' ', paragraph).lower().split()
        words = []
        for word in _paragraph:
            if word not in banned:
                words.append(word)
        words_count = collections.Counter(words)
        return words_count.most_common(1)[0][0]

    # for test
    def mostCommonWords(self, paragraph: str, banned: list[str]) -> str:
        _paragraph = re.sub('[\W]', ' ', paragraph).lower().split()
        words = []
        for word in _paragraph:
            if word not in banned:
                words.append(word)
        return words

    # solution2 without any other library
    def mostCommonWord2(self, paragraph: str, banned: list[str]) -> str:
        words = {}

        for elem in paragraph:
            if not elem.isalnum():
                paragraph = paragraph.replace(elem, ' ')

        paragraph = paragraph.lower().split()

        for word in paragraph:
            if word not in banned:
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1

        max_count = 0
        most_common_word = ""
        for i, v in words.items():
            if max_count < v:
                max_count = v
                most_common_word = i

        return most_common_word

    # Solution3 파이썬 알고리즘 인텨뷰 정답
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                .lower().split()
                        if word not in banned]
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

# TEST
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
sol = Solution()
# TEST check words
print(sol.mostCommonWords(paragraph, banned))
# TEST Solution
print(sol.mostCommonWord(paragraph, banned))
# TEST Solution2
print(sol.mostCommonWord2(paragraph, banned))
