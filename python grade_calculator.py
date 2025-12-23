---

## 📄 Code Example
```python
def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return None, "Invalid input!"

    if marks >= 90:
        return "A", "Excellent performance!"
    elif marks >= 75:
        return "B", "Great job!"
    elif marks >= 60:
        return "C", "Good effort!"
    elif marks >= 40:
        return "D", "You passed!"
    else:
        return "F", "Keep trying!"
