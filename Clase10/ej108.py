from vigilante import vigilar

def filematch(lines, substr):
        for line in lines:
            if substr in line:
                yield line

lines = vigilar('../Data/mercadolog.csv')
naranjas = filematch(lines, 'Naranja')
for line in naranjas:
        print(line)