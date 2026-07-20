a = {"x": 1, "y": 2}
b = {"y": 5, "z": 3}

merged = {**a, **b}

# print(merged)  


marks = {"Ali": 85,
          "Sara": 92,
            "Bilal": 78}

sorted_marks = sorted(marks.items(), key=lambda pair: pair[1], reverse=True)
print(sorted_marks)   # [('Sara', 92), ('Ali', 85), ('Bilal', 78)]