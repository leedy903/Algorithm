'''
Leetcode URL: https://leetcode.com/problems/longest-palindromic-substring/
Problem: Longest Palindromic Substring, 5
Level: Medium
'''

# Try 1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxS = s[0]
        def Palin(s: str, j: int, l: int) -> str:
            k = 0
            if j-l == -1:
                return s[0:2]
            while s[j-k-l] == s[j+k]:
                k += 1
                if j-k-l == 0 or j+k == len(s):
                    break
            return s[j-k-l:j+k]
            
        for i in range(1, len(s)-1):
            if s[i] == s[i-1]:
                newS = Palin(s,i,2)
            elif s[i-1] == s[i+1]:
                newS = Palin(s,i,0)
            if len(newS) > len(maxS):
                maxS = newS
        return maxS

# Wrong case: babad -> baba

# Try 2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = ""
        if len(s) <= 1:
            return s

        for i in range(len(s)):
            for j in range(len(s),i,-1):
                if len(long) >= j-i:
                    continue
                elif s[i:j] == s[i:j][::-1]:
                    long == s[i:j]
        return long

# Wrong case: Takes too much time

# Try 3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i,l=0,0
        for j in range(len(s)):
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
        return s[i: i+l]

# Success!

# Try 3.5
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        f,r = 0,0
        for i in range(len(s)):
            if s[i-r: i+1] == s[i-r: i+1][::-1]:
                f, r = i-r, r+1
            elif i-r > 0 and s[i-r-1: i+1] == s[i-r-1: i+1][::-1]:
                f, r = i-r-1, r+2
        return s[f: f+r]


# Try 4
class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = s[0]

        for i in range(len(s)):
            if len(long) > len(s[i:]):
                return long
            for j in range(len(s)-1, i, -1):
                isPalin = False
                for k in range(0, len(s)):
                    if i+k > j-k:
                        break
                    if s[i+k] == s[j-k]:
                        isPalin = True
                    else:
                        isPalin = False
                        break
                if isPalin:
                    if len(long) < len(s[i:j+1]):
                        long = s[i:j+1]
        return long

# Wrong case: "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# Time Limit Exceeded

# Try 5
class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = s[0]
        for Center in range(len(s)):   
            Radius = 0     
            while 0 <= Center - (Radius+1) and Center + (Radius+1) < len(s) and s[Center-(Radius+1)] == s[Center+(Radius+1)]:
                Radius += 1
            

        return

# Try 6 파이썬 알고리즘 인터뷰
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]

        # 해당 사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ''
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                            expand(i, i + 1),
                            expand(i, i + 2),
                            key=len)
        return result