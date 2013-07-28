import gc
import time
gc.disable()

start_time = time.time()

file_input  = open('numbers.txt')
file_output = open('run_result.txt', 'w')

base   = {}
result = {}

for line in file_input:
    key = line.strip()
    try:
        base[key] += 1
        result[key] = base[key]
    except KeyError:
        base[key] = 1

for k, v in result.items():
    print >> file_output, u'"{0}", {1}'.format(k, v)

file_input.close()
file_output.close()

print time.time() - start_time
