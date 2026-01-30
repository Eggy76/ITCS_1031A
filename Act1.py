Word = input("Input a word: ")

Word_length = len(Word)

numbers = []
print(f"Enter {Word_length} numbers:")

for i in range(Word_length):
    num = float(input(f"Number {i + 1}: "))
    numbers.append(num)

def compute_average(num_list):
    total = 0
    for n in num_list:
        total += n
    return total / len(num_list)

def compare_average_and_length(avg, length):
    if length > avg:
        return "The Word length is greater than the average."
    elif length < avg:
        return "The Word length is less than the average."
    else:
        return "The Word length is equal to the average."

average = compute_average(numbers)

result_message = compare_average_and_length(average, Word_length)

print("\n--- Results ---")
print("List of numbers entered:", numbers)
print("Length of the word:", Word_length)
print("Average of the numbers:", average)
print(result_message)
