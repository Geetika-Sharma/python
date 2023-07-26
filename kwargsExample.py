def func(**k):
    ans = k['a'] * k['b'] + k['c']
    print(ans)

func(a=1,b=3,c=5)