output = []
state = [1,0,0,1,1,0,0,0,0,1]
zhangsan = []

for num in range(512):
    state.insert(0,state[2] ^ state[9])
    output.append(int(state.pop()))
    zhangsan.append(1)
