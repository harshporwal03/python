candyType = [1,1,2,3]
# Calculate the maximum number of candies Alice can eat
max_candies = len(candyType) // 2
print ("Maximum number of candies", max_candies)
        
        # Use a set to store unique candy types
unique_candies = set(candyType)
print ("Unique candies", unique_candies)
        
        # Return the minimum of unique candies and max_candies
print(min(len(unique_candies), max_candies))