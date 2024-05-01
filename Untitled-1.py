def find_initial_macaron_length(pieces):
    # محاسبه طول هر تکه از ماکاران
    x = (pieces[0] - 3) / 2
    y = (pieces[1] - 3) / 2
    
    # محاسبه طول اولیهٔ ماکاران
    initial_length = x + y + 3
    
    return initial_length

# خواندن تعداد تکه‌های باقی مانده از ماکاران
n = int(input())

# خواندن طول هر تکه باقی مانده
pieces = [int(x) for x in input().split()]

# محاسبه و چاپ طول اولیهٔ ماکاران
print(find_initial_macaron_length(pieces))
