phy = int(input())
chem = int(input())
math = int(input())
engl= int(input())
his = int(input())

per = ((phy + chem + math + engl+ his)/500)*100
print(per)
if per > 90:
    print("Grade A")
elif per > 80 and per < 90:
    print("Grade B")
elif per > 70 and per < 80:
    print("Grade C")
elif per > 60 and per < 70:
    print("Grade D")
elif per > 50 and per < 60:
    print("Grade E")