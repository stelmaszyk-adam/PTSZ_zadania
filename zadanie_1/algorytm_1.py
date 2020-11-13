import numpy as np

indexes = ["136805", "136792", "136683", "132231", "136730", "136682",
           "136764", "136782", "136723", "136778", "136309", "136718", "136315", "136759"]
for index in indexes:
    # print()
    # print("<--" + index + "-->")
    for samples in range(50, 550, 50):
        inputFile = []
        outputFile = []
        # print("<"+str(samples) + ">")
        with open(f'test/'+index+'/in'+index+'_'+str(samples)+'.txt', "r") as instance:
            rows = instance.read().split('\n')
            n = int(rows[0])
            for iterator, column in enumerate(rows[1:]):
                if column == '':
                    continue
                p, r, d, w = column.split(' ')
                p, r, d, w = int(p), int(r), int(d), int(w)
                inputFile.append(
                    {"i": iterator+1, "p": p, "r": r, "d": d, "w": w, "dr": d - r})

        time = 0
        weight = 0

        inputFile = sorted(inputFile, key=lambda k: k['d'])

        for i in range(1, samples+1):
            minDueToTime = min(inputFile[:int(samples/3)], key=lambda x: x['r'])
            if(time < minDueToTime['r']):
                time = minDueToTime['r']

            time += minDueToTime['p']
            outputFile.append(minDueToTime['i'])

            if not minDueToTime['r'] <= time - minDueToTime['p']:
                print("Some problems")

            if time > minDueToTime['d']:
                weight += minDueToTime['w']

            inputFile.remove(minDueToTime)
        
        with open(f'test/'+index+'/out'+index+'_'+str(samples)+'.txt', "w") as f:
            f.write(f"{str(weight)}\n")
            f.write(f"{' '.join([str(x) for x in outputFile])}\n")

        print(weight)
