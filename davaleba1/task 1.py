# 1. დაწერეთ პროგრამა, რომელიც იღებს რიცხვების სიას და აბრუნებს სამ მნიშვნელობას:
# (ა) უნიკალური ელემენტების სიას შესაბამისი ინდექსებით,
# (ბ) დუბლიკატების რაოდენობას,
# (გ) ყველაზე ხშირად გამეორებული ელემენტის მნიშვნელობასა და მის სიხშირეს.

# ვიღებთ სტრინგების ინფუთს, ვსფლითავთ, map ფუნქციით გარდავქმნით ინტ-ებად და ვაქცევთ ლისტად
nums = list(map(int, input("Input numbers separated by space: ").split()))

# ვიყენებთ ლექსიკონს სიხშირეების და ინდექსების შესანახად
stats = {}
for i, val in enumerate(nums):
    if val not in stats:
        stats[val] = [i] # ვინახავთ ინდექსს სიაში
    else:
        stats[val].append(i)

print(stats)
# ა) უნიკალური ელემენტები (რომლებიც მხოლოდ 1-ხელ გვხვდება)
unique_elements = [(val, idxs[0]) for val, idxs in stats.items() if len(idxs) == 1]

# ბ) ვთვლით მხოლოდ იმ რიცხვებს, რომლებიც 1-ზე მეტჯერ გვხვდება
duplicates_count = sum(1 for idxs in stats.values() if len(idxs) > 1)

# გ) ყველაზე ხშირი
most_frequent = max(stats.items(), key=lambda x: len(x[1]))

print(f"Unique Elements: {unique_elements}")
print(f"Duplicates count = {duplicates_count}")
print(f"Most frequent: {most_frequent[0]}, Frequency: {len(most_frequent[1])}")




