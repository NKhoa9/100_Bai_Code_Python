# Define age cohort

a = int(input())

if 0<a<=11:
    temp = "Thieu nhi"
elif 11<a<=25:
    temp = "Thieu nien"
elif 25<a<=50:
    temp = "Trung nien"
else:
    temp = "Lao nien"

print(temp)

#TESTED