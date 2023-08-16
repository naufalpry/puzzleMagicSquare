import random

def generate_random_numbers(total, target_sum):
    numbers = []

    while len(numbers) < total - 1:
        random_number = random.randint(1, 9)
        if random_number not in numbers:
            numbers.append(random_number)

    remaining_number = target_sum - sum(numbers)
    numbers.append(remaining_number)

    return numbers

def create_puzzle():
    target_sum = 15
    total_numbers = 9
    
    random_numbers = generate_random_numbers(total_numbers, target_sum)
    random.shuffle(random_numbers)

    return random_numbers

puzzle = create_puzzle()
print("Puzzle Numbers:", puzzle)