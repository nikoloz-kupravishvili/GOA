print("Mile To KM (1)")
print("KM To Mile (2)")

ans = input("1 or 2?: ")
if ans == "1":
    mile = input("Enter Miles:")
    mile = int(mile)
    print(mile * 1.609344 , "KM")
elif ans == "2":
    km = input("Enter KM:")
    km = int(km)
    print(km * 0.6213712 , "Miles")
else:
    print("invalid input !")