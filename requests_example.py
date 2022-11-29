import requests

import json



#url='https://train-z47mcrvoyuu8z51wzjip-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune'

#url='https://train-apgvsf6fu3r69b8eykct-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune'

url='https://train-fgixn9wtlmw9ywgxc1mt-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-ko-small-finetune'

input = "그는 동굴속으로 들어간후 칼을 뺴들었다. 그 동굴에는 마법의  불꽃과 검을 비롯한 무기와 갑옷, 거기에  금속제 갑옷"
nosamples =5
output_length=200

data=json.dumps({
        'text': input,
        'num_samples': nosamples,
        'length': output_length
    })

response = requests.post(url, headers={'Content-Type': 'application/json'}, data=data)

if response.status_code == 200:
    res = response.json() 
    print(res)

else:
    print("Failed requests")