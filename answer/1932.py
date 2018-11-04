def get_input():
    import sys
    r = sys.stdin.readline
    n = r().strip()
    inputs = []
    for _ in range(int(n)):
        inputs.append(r().strip())
    return [n] + inputs

def int_tri(test_inputs):
    n = int(test_inputs.pop(0))
    tri = [list(map(int, i.split())) for i in test_inputs]

    if n==1: return tri[0]

    #initiating
    tri[1][0] += tri[0][0]
    tri[1][1] += tri[0][0]
    current = tri[1]

    if n==2: return max(current)
    #iteration
    for ele in tri[2:]:
        ele[0] += current[0]
        ele[-1] += current[-1]
        for k in range(len(ele)-2):
            ele[k+1] += max(current[k:k+2])
        current = ele
    return (max(current))    

def main(get_input, int_tri):
    inputs = get_input()
    output = int_tri(inputs)
    print(output)

main(get_input, int_tri)