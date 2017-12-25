
print("测试")

if True:
    print("one")
    print("one1")
else:
    print("two")

#a, b, c = 1, 2, '3'

s = "abcdedg"
print("结果" + s[1:4])

for result in 'ascd':
    print(result)

for index in range(len('ascd')):
    print(index)

def test(param1, param2 = 'default',*param3, **param4):
    print('this is a funcation param1' + param1)
    print('this is a funcation param2' + param2)
    for param in param3:
        print('this is a funcation param3' + param)
    for key, value in param4.items():
        print(key + ':' + value)

test('xxxx','yyyy', 'zzzzz','qqqqqq', param='1111', secondParam='2222')