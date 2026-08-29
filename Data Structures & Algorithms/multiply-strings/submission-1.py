class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Create a dictionary to map string characters to integers
        digit_map = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }
        
        # Convert num1 to an integer starting from the right (1, 10, 100...)
        n1 = 0
        place = 1
        for char in reversed(num1):
            n1 += digit_map[char] * place
            place *= 10
            
        # Convert num2 to an integer starting from the right (1, 10, 100...)
        n2 = 0
        place = 1
        for char in reversed(num2):
            n2 += digit_map[char] * place
            place *= 10
            
        # Multiply the two numbers and convert the result back to a string
        return str(n1 * n2)