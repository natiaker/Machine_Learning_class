# 10. შექმენით Rectangle და Square კლასები მემკვიდრეობითობით: Square(Rectangle);
# დაამატეთ მეთოდი scale(factor) რომელიც ცვლის ზომებს  და აბრუნებს ახალ ობიექტს  და დაწერეთ პროგრამა,
# რომელიც იღებს სხვადასხვა ფიგურების სიას და პოულობს (ა) ყველაზე დიდ ფართობს, (ბ) საშუალო პერიმეტრს ტიპების
# მიხედვით (Rectangle vs Square).

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def scale(self, factor):
        return Rectangle(self.width * factor, self.height * factor)

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def scale(self, factor):
        return Square(self.width * factor)


def analyze_shapes(shapes):
    if not shapes:
        return 0, {}

    max_area = max(shape.area() for shape in shapes)

    # (ბ) საშუალო პერიმეტრი ტიპების მიხედვით
    stats = {
        "Rectangle": {"total_perim": 0, "count": 0},
        "Square": {"total_perim": 0, "count": 0}
    }

    for shape in shapes:
        type_name = type(shape).__name__
        stats[type_name]["total_perim"] += shape.perimeter()
        stats[type_name]["count"] += 1

    averages = {}
    for name, data in stats.items():
        if data["count"] > 0:
            averages[name] = data["total_perim"] / data["count"]

    return max_area, averages


shapes_list = [
    Rectangle(10, 5),
    Square(4),
    Rectangle(8, 2),
    Square(6)
]

max_a, avg_p = analyze_shapes(shapes_list)

print(f"ა) ყველაზე დიდი ფართობი: {max_a}")
print(f"ბ) საშუალო პერიმეტრები: {avg_p}")