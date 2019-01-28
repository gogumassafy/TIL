def strcmp(str1, str2):
    i = 0
    if len(str1) != len(str2):
        return False
    while i < len(str1):
        if str1[i] != str2[i]:
            return False
        i+= 1

    return True

a = "abc"
b = 'abb'

print(strcmp(a, b))
