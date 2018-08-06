import json
lines = [] 
with open('ptt_0726_s.json', 'r',encoding='utf-8-sig') as f:
    ptt_push=json.load(f)
    number=len(ptt_push)
    for i in range(number-1):
        if ptt_push[i]["h_推文總數"]=={}:
            ptt_push[i]["h_推文總數"]['all']=0
    ptt_push=sorted(ptt_push,key=lambda ptt_push: ptt_push["h_推文總數"]['all'],reverse=True)
    
    for j in range(number-1):          #方便助教檢查
        print(ptt_push[j])

    with open('ptt_0726_ssort.json','w') as fi:
        ptt_pushd=json.dumps(ptt_push)
        json.dump(ptt_push,fi)