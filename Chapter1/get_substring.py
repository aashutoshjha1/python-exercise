def substring(str1):
    """
    This function will get a string and return all possible substrings.
    """
    substring_list = []
    for i in range(len(str1)):
         for j in range(i+1,len(str1)+1):
               substring_list.append(str1[i:j])
    return substring_list


# Test Result
print(substring("aashu"))

