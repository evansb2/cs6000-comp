try:
   mark = int(input("Please enter the exam mark out of 100 "))
except ValueError:
   print("\nPlease only use integers")

if mark < 60:
    print("\nFail")
elif mark < 101:
    print("\nPass")
else:
    print("\nThe mark is out of range")
