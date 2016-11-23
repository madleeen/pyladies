#nasobilka
def nasobeniPole(iterace,pole):
    novySeznam=[]
    for element in pole:
        novySeznam.append(element*iterace)
    return novySeznam

for i in range(1,11):
    print(nasobeniPole(i,range(1,11)))
