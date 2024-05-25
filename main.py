age = int(input("Enter your age: "))

if age < 2:
    print("You are an infant.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior.")

if age < 13:
    print("Enjoy your childhood!")
elif age < 20:
    print("These are your teenage years, make the most of them!")
elif age < 30:
    print("These are your young adult years, explore and learn.")
elif age < 50:
    print("These are your middle-aged years, stay healthy and happy.")
else:
    print("These are your golden years, cherish them!")

if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")

if age < 16:
    print("You are not eligible to drive.")
elif age < 18:
    print("You might be eligible for a learner's permit.")
else:
    print("You are eligible to drive.")

if age < 30:
    print("Stay active and eat well to maintain your health.")
elif age < 50:
    print("Regular check-ups and a balanced diet are important.")
else:
    print("Maintain a healthy lifestyle and stay engaged in social activities.")
