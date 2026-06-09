# Function to display the array
def display_array(arr):
    print("Current array:", arr)  # Proper indentation for function definition

# Create an array (list)
array = [10, 20, 30, 40]

# Display the initial array
display_array(array)

# Append an item to the array
array.append(50)
print("After appending 50:")
display_array(array)

# Insert an item at a specific index
array.insert(2, 25)  # Insert 25 at index 2
print("After inserting 25 at index 2:")
display_array(array)

# Reverse the order of the array
array.reverse()
print("After reversing the array:")
display_array(array)
