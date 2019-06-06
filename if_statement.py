print("1.")
#using if function
is_male = True

if is_male:
    print("You are a male")
else:
    print("You are not a male")


print("2.")
#if with two boolean
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male and tall")
else:
    print("You are not a male or tall or both")

print("3.")
#if function with elif (else + if)
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are male and not tall")
elif not(is_male) and is_tall:
    print("You are not male and you are tall")
else:
    print("You are not a male and not tall")