import os

directory = 'C:/Users/toby1/Desktop/D-analyze' #更改路径！！！


files = [filename for filename in os.listdir(directory) if filename.endswith('.txt')]

results = {} 


for filename in files:
    filepath = os.path.join(directory, filename)
    with open(filepath, 'r') as f:
        data = [[float(num) for num in line.strip().split()] for line in f.readlines()]
        

        distances = [abs(point[0]) + abs(point[1]) for point in data]


        min_distance = min(distances)
        min_index = distances.index(min_distance)
        min_value = data[min_index]

        results[filename] = {'min_distance': min_distance, 'min_value': min_value, 'min_index': min_index}

for filename, result in results.items():
    print(f"{filename}: 最接近 0 的值是 {result['min_value']}，其距离为 {result['min_distance']}。")
