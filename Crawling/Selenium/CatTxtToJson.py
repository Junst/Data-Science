file_path = "묘종 목록.txt"

namedict = {}
with open(file_path, encoding='utf-8') as f:
    # lines = f.readlines()
    lines = f.read().splitlines()
# lines = [line.rstrip('\n') for line in lines]

print(lines)

for i in range(len(lines)): # list 만큼 dict에
    namedict[i] = lines[i] # 넣어줌
print(namedict) # 그 dict가 제대로 됐는지 확인

import json
with open("catnames.json",'w', encoding='utf-8') as file :
    json.dump(namedict,file, indent='\t', ensure_ascii=False) # dict를 json으로 저장


