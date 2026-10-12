def compress_string(s):
    # Edge case: empty string
    if not s:
        return s

    compressed = []  # We will store character-count pairs here
    current_char = s[0]
    count = 1

    # Loop through the string starting from the 2nd character (index 1)
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            # Character changed! Append the previous char and count
            compressed.append(current_char + str(count))
            current_char = s[i]
            count = 1

    # Append the last character group after loop ends
    compressed.append(current_char + str(count))

    # Join the list into a single string
    result = "".join(compressed)

    # Return the shorter string
    return result if len(result) < len(s) else s
#peak element task
def find_peak_element(nums):
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i
    return -1
