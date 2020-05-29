test_str = "This is the string to test"
print(test_str)

substring = test_str[5:]
print(substring)

substring = test_str[:5]
print(substring)

substring = test_str[5:15]
print(substring)

#--------------------------------

test_str = "currency?euro"
print(test_str)

index = test_str.find("?")
substring = test_str[index+1:]
print(substring)

separated = test_str.split("?")
print(separated)