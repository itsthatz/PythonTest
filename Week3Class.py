while True:
  n = int(input("No of Bricks: "))
  if n >= 1 and n <= 8:
    break

#for i in range(n):
#    print("." * (n-i-1) + "#" * (i+1) )
#    print()

for i in range(n):
    for j in range(n-i-1):
        print(".", end="")
    for k in range(i+1):
        print("#", end="")
    print()
