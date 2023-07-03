s = int(input("Enter the Money: "))
if s % 2000 == 0:
    t = s//2000-1
    s -= 2000*t
if s % 500 == 0:
    f = s//500-1
    s -= 500*f
if s % 100 == 0:
    h = s//100
    s -= 100*h

print("2000 notes are: " + str(t)+"  500 notes are: " + str(f)
      + "  100 notes are: " + str(h))
