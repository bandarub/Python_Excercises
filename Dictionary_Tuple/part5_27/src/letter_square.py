def print_square(layers):
    # Calculate the size of the square based on the number of layers
    size = 2 * layers - 1
    
    # Create the square
    for i in range(size):
        for j in range(size):
            # The letter to print depends on the minimum distance from the edge
            distance_from_edge = min(i, j, size - i - 1, size - j - 1)
            letter = chr(ord('A') + (layers - 1 - distance_from_edge))  # Start with the correct letter
            print(letter, end="")
        print()  # Move to the next line after printing one row

# Example usage
num = int(input("Layers: "))
print_square(num)
