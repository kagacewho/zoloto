input_data = open('input.txt', 'r') 
data = input_data.read()
a = int(data[0])
b = int(data[1])
c = int(data[2])
a,b,c=map(int,input('a b c: ').split())
if a*b==c: 
    print("Yes")
else: 
    print("No")
output_data = open('output.txt', 'w')
output_data.write(str())
input_data.close()
output_data.close()