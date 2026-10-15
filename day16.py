# # from collections import Counter


# # def top_k_categories(transactions: list[dict], k: int = 3) -> list[tuple[str, float | int]]:
# #     """
# #     Aggregates sales amounts by category and returns the top K categories
# #     sorted by total sales in descending order.
# #     """
# #     # Sum amounts per category
# #     totals = Counter()
# #     for item in transactions:
# #         totals[item["category"]] += item["amount"]

# #     # return top K categories as (category, total_amount) tuples
# #     return totals.most_common(k)


# # # --- Alternative Solution (Standard Dictionary) ---
# # def top_k_categories_dict(transactions: list[dict], k: int = 3) -> list[tuple[str, float | int]]:
# #     totals = {}
# #     for item in transactions:
# #         cat = item["category"]
# #         amt = item["amount"]
# #         totals[cat] = totals.get(cat, 0) + amt

# #     # Sort dictionary items by value in descending order and slice top k
# #     sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
# #     return sorted_totals[:k]


# # # --- Example Run ---
# # if __name__ == "__main__":
# #     sample_transactions = [
# #         {"category": "Electronics", "amount": 1200},
# #         {"category": "Books", "amount": 45},
# #         {"category": "Electronics", "amount": 300},
# #         {"category": "Clothing", "amount": 150},
# #         {"category": "Books", "amount": 30},
# #         {"category": "Home", "amount": 200},
# #     ]

# #     result = top_k_categories(sample_transactions, k=2)
# #     print("Top 2 Categories:", result)
# #     # Expected Output: [('Electronics', 1500), ('Home', 200)]
# from collections import Counter
# import string


# def count_word_frequency():
#         text=input("Enter a string: ")
#         words=text.lower().split()
#         frequency=Counter(words)
#         counter=0
#         cleaned_text = text.translate(str.maketrans("", "", string.punctuation))
#         for word in frequency:
#             counter+=1
#             print(f"{word}: {frequency[word]}")
# task 3
# def find_palindrome(s):
#     cleaned="".join(c.lower() for c in s if c.isalnum())
#     return cleaned==cleaned[::-1]
#     s.lower()
#     oringinal=s
#     reverse=s[::-1]
#     if oringinal==reverse:
#         return {s:"is palindrome"}
#     else:
#         return {s:"is not palindrome"}
# task4

# def find_second_largest(nums: list[int]) -> int | None:
#     largest = float("-inf")
#     second_largest = float("-inf")

#     for num in nums:
#         if num > largest:
#             # Shift current largest to second_largest
#             second_largest = largest
#             largest = num
#         elif num > second_largest and num != largest:
#             # Update second_largest if it's smaller than largest but bigger than current second_largest
#             second_largest = num

#     # If second_largest was never updated, no valid second largest exists
#     return second_largest if second_largest != float("-inf") else None


# # --- Test Cases ---
# print(find_second_largest([10, 20, 4, 45, 99]))  # Output: 45
# print(find_second_largest([10, 10, 10]))  # Output: None
# print(find_second_largest([5, 2]))  # Output: 2
# print(find_second_largest([1]))  # Output: None
# def make_capitalizer(s):
#     for word in s.lower().split():
#         if word[0].isupper():
#             return word
#         else:
#           return word
# 
text=input("Enter a string: ")
words=text.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"Longest word: {longest_word}")