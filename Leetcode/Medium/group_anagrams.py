'''
Leetcode URL: https://leetcode.com/problems/group-anagrams/
Problem: Group Anagrams, 49
Level: Medium
'''
import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # keywords
        keys = []
        # ans list
        anagrams = []

        # take ordered words for key
        for word in strs:
            '''
            # slow code; use list to sort
            # ordering the word use list, sort()
            _word = list(word)
            _word.sort()

            # make word string
            key = "".join(_word)
            '''
            # faster code
            key = "".join(sorted(word))
            # if key is not in keywords list, take it
            if key not in keys:
                keys.append(key)
                anagrams.append([])
            
            # use keywords list to take the index and adds the word in anagrams
            anagrams[keys.index(key)].append(word)
        
        '''
        # reorder the anagrams
        for anagram in anagrams:
            anagram.sort()
        '''
        return anagrams

    # solution2 파이썬 알고리즘 인텨뷰 정답
    def groupAnagrams2(self, strs: list[str]) -> list[list[str]]:
        '''
        # 딕셔너리에서 존재하지 않는 키를 삽입 할 때 KeyError가 나는 것을 방지하기 위해 defaultdict()로 선언하여 해결
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        '''
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))
            # 정렬하여 딕셔너리에 추가, defaultdict를 사용하지 않았기 떄문에 key값 예외처리를 해준다.
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)

        # dict.values() 함수를 통해 dictionary의 value값을 받을 수 있다.
        return list(anagrams.values())


# TEST 1
Input1 = ["eat","tea","tan","ate","nat","bat"]
# Output1: [["bat"],["nat","tan"],["ate","eat","tea"]]

sol = Solution()
# TEST 1.1 groupAnagrams
print(sol.groupAnagrams(Input1))
# TEST 1.2 groupAnagrams2
print(sol.groupAnagrams2(Input1))