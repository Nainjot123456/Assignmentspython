g = input("Enter gender in terms of M or F: ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if g == 'M':
    if 134 <= hemoglobin <= 167:
        print("normal level of hemoglobin for men.")
    elif hemoglobin < 134:
        print("low level of hemoglobin for men.")
    else:
        print("high level of hemoglobin for men.")
elif g == 'F':
    if 117 <= hemoglobin <= 155:
        print("normal level of hemoglobin  for women")
    elif hemoglobin < 117:
        print("low level of hemoglobin women.")
    else:
        print("high level of hemoglobin for women.")
else:
    print("enter M for males and F for females")