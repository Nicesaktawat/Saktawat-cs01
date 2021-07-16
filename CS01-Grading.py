a = int(input("คะแนนนักเรียน ="))
b = int(input("คะแนนสอบกลางภาคนักเรียน ="))
c = int(input("คะแนนสอบปลายภาคนักเรียน ="))
d = (a+b+c)
if (d>100):
    print("ตรวจสอบคะแนนอีกครั้ง")
elif (d<0):
    print("ตรวจสอบคะแนนอีกครั้ง")
elif (d>=75):
    print("Grade A")
elif (d>=70):
    print("Grade B+")
elif (d>=65):
    print("Grade B")
elif (d>=60):
    print("Grade C+")
elif (d>=55):
    print("Grade D+")
elif (d>=50):
    print("Grade D")
else :
    print("Grade F")