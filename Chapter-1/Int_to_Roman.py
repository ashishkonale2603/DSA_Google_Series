def intToRoman(num):
    store=[
        [1000,'M'],[900,'CM'],[500,'D'],[400,'CD'],
        [100,'C'],[90,'XC'],[50,'L'],[40,'XL'],
        [10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']
           ]
    result=''
    for i in range(len(store)):
        while num >= store[i][0]:
            result+=store[i][1]
            num-=store[i][0]
    return result

print(intToRoman(58))
