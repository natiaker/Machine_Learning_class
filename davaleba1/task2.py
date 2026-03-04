# 2. შექმენით ფუნქცია, რომელსაც გადაეცემა ლისტი group_by_parity(numbers),
# სია აბრუნებს ლექსიკონს ორი გასაღებით "even" და "odd"; თითოეული მნიშვნელობა უნდა
# იყოს შესაბამისი რიცხვების სია დალაგებული ზრდადობით, ხოლო საბოლოოდ დაბეჭდეთ რომელი ჯგუფის
# ჯამი უფრო დიდია და რამდენით.

def group_by_parity(numbers):
    # დავახარისხოთ მთლიანი სია
    numbers.sort()

    result = {"even": [], "odd": []}

    for number in numbers:
        if number % 2 == 0:
            result["even"].append(number)
        else:
            result["odd"].append(number)

    return result


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

grouped_data = group_by_parity(numbers_list)

even_sum = sum(grouped_data["even"])
odd_sum = sum(grouped_data["odd"])

print(grouped_data)

if even_sum > odd_sum:
    diff = even_sum - odd_sum
    print(f"Even sum {even_sum} is greater than odd sum {odd_sum} and difference is {diff}")
elif even_sum < odd_sum:
    diff = odd_sum - even_sum
    print(f"Odd sum {odd_sum} is greater than even sum {even_sum} and difference is {diff}")
else:
    print(f"Both are equal: {even_sum}")
