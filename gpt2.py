# Function to create a pyramid of letters
def letter_pyramid(custom_letter='*', height=5):
    for i in range(1, height + 1):
        # Print spaces for alignment
        print(' ' * (height - i), end='')
        # Print the custom letter in pyramid shape
        print((custom_letter + ' ') * i)
#
# Example usage
if __name__ == "__main__":
    # Customize the letter and height here
    letter = input("Enter the letter for the pyramid: ")
    height = int(input("Enter the height of the pyramid: "))
    letter_pyramid(letter, height)