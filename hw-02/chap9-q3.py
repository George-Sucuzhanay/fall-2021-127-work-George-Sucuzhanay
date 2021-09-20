# Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text - perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.

# Write a function that counts the number of alphabetic characters (a through z, or A through Z) in your text and then keeps track of how many are the letter ‘e’. Your function should print an analysis of the text like this:

# Your text contains 243 alphabetic characters, of which 109 (44.8%) are 'e'.



for char in lowercase_text:    
    # Check if we have an alphanumeric string and continue the loop if not
    if not char.isalpha():
        continue
    # Increment the total character counter
    char_counter += 1
    # Additionaly, increment the 'e' counter if we have an 'e'
    if char == 'e':
        e_counter += 1
