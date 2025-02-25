def get_grade(num1, num2, num3):
    grade_ave = (int(num1) + int(num2) + int(num3)) / 3
    match grade_ave:
        case _ if grade_ave >= 90:
            return 'A'
        case _ if grade_ave >= 80 and grade_ave <= 90:
            return 'B'
        case _ if grade_ave >= 70 and grade_ave <= 80:
            return 'C'
        case _ if grade_ave >= 60 and grade_ave <= 70:
            return 'D'
        case _ if grade_ave < 60:
            return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True