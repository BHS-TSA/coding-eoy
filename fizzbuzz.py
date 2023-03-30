numbers = list(range(101))

finalthing = ''
for i in numbers:
    if i % 3 == 0:
        finalthing += 'Fizz'
    elif i % 5 == 0:
        finalthing += 'Buzz '
    else:
        finalthing += str(i)

    if i != numbers[len(numbers) - 1]:
        finalthing += ", "

print(finalthing)