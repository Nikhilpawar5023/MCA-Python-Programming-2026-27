import os
# Delete old placeholder files
for f in ["Unit-02-Functions-and-Modular-Programming", "Unit-03-Strings-and-Python-Collections", "Unit-04-Exception-File-and-Standard-Libraries"]:
    if os.path.exists(f) and os.path.isfile(f):
        os.remove(f)
        print(f"Deleted {f}")

# Unit 02
os.makedirs("Unit-02-Functions-and-Modular-Programming", exist_ok=True)
open("Unit-02-Functions-and-Modular-Programming/factorial.py","w").write('def factorial(n):\n    return 1 if n<=1 else n*factorial(n-1)\nnum=int(input("Enter number: "))\nprint("Factorial:",factorial(num))')
open("Unit-02-Functions-and-Modular-Programming/fibonacci.py","w").write('def fibonacci(n):\n    a,b=0,1\n    for i in range(n):\n        print(a,end=" ")\n        a,b=b,a+b\nnum=int(input("Enter terms: "))\nfibonacci(num)')
open("Unit-02-Functions-and-Modular-Programming/prime_check.py","w").write('def is_prime(n):\n    if n<=1: return False\n    for i in range(2,n):\n        if n%i==0: return False\n    return True\nnum=int(input("Enter number: "))\nprint("Prime" if is_prime(num) else "Not prime")')
open("Unit-02-Functions-and-Modular-Programming/sum_list.py","w").write('def sum_list(lst):\n    total=0\n    for i in lst: total+=i\n    return total\nnums=[10,20,30,40]\nprint("Sum:",sum_list(nums))')
open("Unit-02-Functions-and-Modular-Programming/calculator.py","w").write('def add(a,b): return a+b\ndef sub(a,b): return a-b\ndef mul(a,b): return a*b\ndef div(a,b): return a/b\nx=int(input("Enter first: "))\ny=int(input("Enter second: "))\nprint("Add:",add(x,y))\nprint("Sub:",sub(x,y))')

# Unit 03
os.makedirs("Unit-03-Strings-and-Python-Collections", exist_ok=True)
open("Unit-03-Strings-and-Python-Collections/string_reverse.py","w").write('s=input("Enter string: ")\nprint("Reverse:",s[::-1])')
open("Unit-03-Strings-and-Python-Collections/palindrome.py","w").write('s=input("Enter string: ")\nprint("Palindrome" if s==s[::-1] else "Not palindrome")')
open("Unit-03-Strings-and-Python-Collections/list_methods.py","w").write('lst=[1,2,3]\nlst.append(4)\nprint(lst)\nlst.remove(2)\nprint(lst)')
open("Unit-03-Strings-and-Python-Collections/dict_example.py","w").write('student={"name":"Nikhil","roll":23}\nprint(student["name"])\nstudent["marks"]=85\nprint(student)')
open("Unit-03-Strings-and-Python-Collections/tuple_count.py","w").write('t=(1,2,2,3,2)\nprint("Count of 2:",t.count(2))')

# Unit 04
os.makedirs("Unit-04-Exception-File-and-Standard-Libraries", exist_ok=True)
open("Unit-04-Exception-File-and-Standard-Libraries/exception_handling.py","w").write('try:\n    a=int(input("Enter num: "))\n    print(10/a)\nexcept ZeroDivisionError:\n    print("Cannot divide by zero")')
open("Unit-04-Exception-File-and-Standard-Libraries/file_read_write.py","w").write('f=open("test.txt","w")\nf.write("Hello Nikhil")\nf.close()\nf=open("test.txt","r")\nprint(f.read())')
open("Unit-04-Exception-File-and-Standard-Libraries/math_lib.py","w").write('import math\nprint(math.sqrt(16))\nprint(math.factorial(5))')
open("Unit-04-Exception-File-and-Standard-Libraries/datetime_lib.py","w").write('import datetime\nprint(datetime.datetime.now())')
open("Unit-04-Exception-File-and-Standard-Libraries/random_lib.py","w").write('import random\nprint(random.randint(1,100))')

print("All 15 files created!")