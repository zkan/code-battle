file_input = open('numbers.txt')

given_series = set(line.strip() for line in file_input)
base_series  = set(['{0:04}'.format(num) for num in xrange(0, 10000)])

result = base_series.difference(given_series)

file_output = open('run_result.txt', 'w')

for item in result:
    print >> file_output, item

file_input.close()
file_output.close()
