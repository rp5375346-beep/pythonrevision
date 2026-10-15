# def first_non_repeating_char(s):
#     char_count={}
#     for char in s:
#         char_count[char]=char_count.get(char,0)+1
#     for char in s:
#         if char_count[char]==1:
#             return char
#     return None
# def is_anagram(s1,s2):
    # s1=s1.lower().replace(" ","")
    # s2=s2.lower().replace(" ","")
    # return sorted(s1)==sorted(s2)
# def count(s):
#     char_count={}
#     for char in s:
#         if char in ('a','e','i','o','u'):
#             char_count[char]=char_count.get(char,0)+1
#     return char_count
# def is_longest(s1,s2):
#     words1=s1.split()
#     words2=s2.split()
#     longest_word1=max(words1,key=len)
#     longest_word2=max(words2,key=len)
#     return len(longest_word1)>len(longest_word2)
# def reverse_str(s):
#     str=s.split()
#     reversed_str=" ".join(str[::-1])
#     return reversed_str
def rotate_string(s,n):
    for i in range(n):
        s=s[-1]+s[:-1]
        return s
    