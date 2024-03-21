#测试


from naga2.individual import Individual
from naga2.decode import decode
for i in range(50):
    indi=Individual()
    decode(indi)
    print(indi.fitness)