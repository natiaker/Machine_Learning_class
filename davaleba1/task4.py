# 4. დაწერეთ ფუნქცია merge_and_resolve(a, b), სადაც a და b არის ორი ლექსიკონი {key: int}, ოირვე რიცხვია;
# დააბრუნეთ გაერთიანებული ლექსიკონი ისე, რომ დამთხვევის შემთხვევაში აირჩიოთ key-ის უფრო დიდი მნიშვნელობა,
# ხოლო დამატებით დააბრუნეთ იმ გასაღებების სია, სადაც კონფლიქტი მოხდა (დამთხვევა).


def merge_and_resolve(a, b):
    # ვიღებთ a-ს ასლს, რომ ორიგინალი არ შევცვალოთ
    merged = a.copy()
    conflicts = []

    # გადავდივართ b ლექსიკონის ელემენტებზე
    for key, value in b.items():
        if key in merged:
            # თუ გასაღები ორივეშია, ეს კონფლიქტია
            conflicts.append(key)
            # ვიტოვებთ უფრო დიდ მნიშვნელობას
            if value > merged[key]:
                merged[key] = value
        else:
            # თუ გასაღები ახალია, უბრალოდ ვამატებთ
            merged[key] = value

    return merged, conflicts


dict1 = {"apple": 5, "banana": 10, "orange": 8}
dict2 = {"banana": 15, "orange": 3, "grape": 12}

result_dict, conflict_keys = merge_and_resolve(dict1, dict2)

print(f"United: {result_dict}")
print(f"Conflict keys: {conflict_keys}")