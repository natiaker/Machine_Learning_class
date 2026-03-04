# 8. დაწერეთ ფუნქცია parse_log(lines), სადაც lines არის სტრიქონების სია ფორმატით "YYYY-MM-DD user action",
# მაგალითად “2025-01-25 Giorgo Login; დააბრუნეთ
# (ა) თითო მომხმარებელზე action-ების რაოდენობა,
# (ბ) ყველაზე აქტიური მომხმარებელი,
# (გ) დღის მიხედვით action-ების რაოდენობა დალაგებული თარიღით.


def parse_log(lines):
    user_counts = {}
    date_counts = {}

    for line in lines:
        parts = line.split(" ")
        if len(parts) < 3:
            continue  # გამოვტოვოთ არასწორი ფორმატის ხაზები

        date = parts[0]
        user = parts[1]

        # (ა) მომხმარებლების აქტივობის დათვლა
        user_counts[user] = user_counts.get(user, 0) + 1

        # (გ) დღის მიხედვით აქტივობის დათვლა
        date_counts[date] = date_counts.get(date, 0) + 1

    # (ბ) ყველაზე აქტიური მომხმარებლის პოვნა
    most_active_user = max(user_counts.items(), key=lambda x: x[1])[0] if user_counts else None

    # (გ) თარიღების მიხედვით დახარისხება
    sorted_dates = dict(sorted(date_counts.items()))

    return user_counts, most_active_user, sorted_dates


log_data = [
    "2025-01-25 Giorgi Login",
    "2025-01-25 Nino Logout",
    "2025-01-26 Giorgi Upload",
    "2025-01-25 Giorgi Delete",
    "2025-01-26 Nino Login"
]

users, active, dates = parse_log(log_data)

print(f"ა) აქტივობა მომხმარებელზე: {users}")
print(f"ბ) ყველაზე აქტიური მომხმარებელი: {active}")
print(f"გ) აქტივობა დღეების მიხედვით: {dates}")

