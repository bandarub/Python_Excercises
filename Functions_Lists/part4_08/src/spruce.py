def spruce(size):
    print("a spruce!")
    for i in range(size):
        # Print leading spaces
        print(' ' * (size - i - 1), end='')  # Print leading spaces
        # Print the branches of the tree
        print('*' * (2 * i + 1))  # Print stars
    # Print the trunk of the tree
    print(' ' * (size - 1) + '*')  # Center the trunk



if __name__ == "__main__":
    spruce(3)