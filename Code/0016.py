# Ranking students?

TBHKI, TBHKII = map(float, input().split())

TBCN=(TBHKI+TBHKII*2)/3
if TBCN>=8:
    r='Gioi'
elif 6.5 <= TBCN < 8:
    r='Kha'
elif 5 <= TBCN < 6.5:
    r='Trung binh'
elif 3.5 <= TBCN < 5:
    r='Yeu'
else:
    r='Kem'

print(f"{round(TBCN,1)}\n{r}")

#TESTED