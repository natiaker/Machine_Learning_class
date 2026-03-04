# 5. დაწერეთ ფუნქცია is_balanced(expr), რომელიც ამოწმებს სწორად არის თუ არა
# ფრჩხილები დალაგებული სტრიქონში (მხარდაჭერა: ()[]{}); გამოიყენეთ stack (სია) და დააბრუნეთ
# True/False, ასევე პირველი შეცდომის ინდექსი თუ არასწორია.

def is_balanced(expr):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for index, char in enumerate(expr):
        # თუ გახსნილი ფრჩხილია, ვამატებთ სტეკში
        if char in "([{":
            stack.append((char, index))

        # თუ დახურვის ფრჩხილია
        elif char in ")]}":
            # შეცდომა 1: გვაქვს დახურული ფრჩხილი, მაგრამ სტეკი ცარიელია
            if not stack:
                return False, index

            # ამოვიღებთ ბოლო გახსნილ ფრჩხილს და მის ინდექსს
            last_open, open_index = stack.pop()

            # შეცდომა 2: დახურული ფრჩხილი არ შეესაბამება ბოლო გახსნილს
            if mapping[char] != last_open:
                return False, index

    # ციკლის შემდეგ, თუ სტეკი ცარიელი არაა, ნიშნავს რომ რომელიმე ფრჩხილი არ დაიხურა
    if stack:
        # ვაბრუნებთ პირველივე იმ ფრჩხილის ინდექსს, რომელიც ღია დარჩა
        return False, stack[0][1]

    return True, None


test_expr = "{[()]}"
is_ok, err_idx = is_balanced(test_expr)

if is_ok:
    print("სტრიქონი დაბალანსებულია!")
else:
    print(f"შეცდომა ინდექსზე: {err_idx}")