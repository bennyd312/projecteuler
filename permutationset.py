
def permutationset(digits):
    """
    Input: list of numbers, we want all permutations of these numbers

    Output: All permutations of given numbers
    """
    permutations = []
    if len(digits) == 1:
        permutations.append(digits[0])

    else:
        for i in digits:
            newdigits = []
            for j in digits:
                
                if i!=j:
                    newdigits.append(j)
            temp = permutationset(newdigits)
            
            if type(temp[0]) == list: # Clears nested lists in all other cycles
                for item in temp:
                    item.append(i)
                    permutations.append(item)
            else: # We get a list of lists
                temp.append(i)
                permutations.append(temp)

            """
            for i in temp:
                permutations.append(i)
            """

    return permutations
