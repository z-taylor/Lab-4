grade = float(input("Enter the score of your exam: "))
match(grade):
    case grade if 97 < grade <= 100:
        print("Letter grade is: A+")
    case grade if 94 < grade <= 97:
        print("Letter grade is: A")
    case grade if 91 < grade <= 94:
        print("Letter grade is: A-")
    case grade if 88 < grade <= 91:
        print("Letter grade is: B+")
    case grade if 85 < grade <= 88:
        print("Letter grade is: B")
    case grade if 82 < grade <= 85:
        print("Letter grade is: B-")
    case grade if 79 < grade <= 82:
        print("Letter grade is: C+")
    case grade if 76 < grade <= 79:
        print("Letter grade is: C")
    case grade if 73 < grade <= 76:
        print("Letter grade is: C-")
    case grade if 70 < grade <= 73:
        print("Letter grade is: D+")
    case grade if 67 < grade <= 70:
        print("Letter grade is: D")
    case grade if 64 < grade <= 67:
        print("Letter grade is: D-")
    case grade if 0 <= grade <= 64:
        print("Letter grade is: F")