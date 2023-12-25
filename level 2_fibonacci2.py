def generate_fibonacci_sequence(num_terms):
    fibonacci_sequence = [0, 1]
    for i in range(2, num_terms):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)

    return fibonacci_sequence

num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    sequence = generate_fibonacci_sequence(num_terms)
    print("Fibonacci sequence up to {} terms:".format(num_terms))
    print(sequence)