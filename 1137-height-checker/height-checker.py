class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Find the maximum height in the list
        max_height = max(heights)
        
        # Initialize a list to count the occurrences of each height
        height_counts = [0] * (max_height + 1)
        
        # Count the occurrences of each height
        for height in heights:
            height_counts[height] += 1
        
        # Iterate through the original list and compare heights with their sorted order
        count = 0
        sorted_index = 0
        for height in heights:
            # Find the next non-zero count in the height_counts list
            while height_counts[sorted_index] == 0:
                sorted_index += 1
            # If the current height doesn't match the sorted height, increment count
            if height != sorted_index:
                count += 1
            # Decrement the count for the sorted height
            height_counts[sorted_index] -= 1
        
        return count
