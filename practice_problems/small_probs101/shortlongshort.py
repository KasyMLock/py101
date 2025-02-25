def shortlongshort(str1,str2):
    if len(str1) < len(str2):
        return str1 + str2 + str1
    else:
        return str2 + str1 + str2

print(shortlongshort('abc', 'defgh'))
print(shortlongshort('abcde', 'fgh'))