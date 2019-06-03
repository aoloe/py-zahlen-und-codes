import re
import bisect

def read_arguments():
    import argparse
    parser = argparse.ArgumentParser(description='Match names with codes by values')

    parser.add_argument('codes', default=None, help='text file with the codes')
    parser.add_argument('names', default=None, help='text file with the names')
    parser.add_argument('-o', dest='output', default=None, help='output file')

    args = parser.parse_args()
    return vars(args)

def get_codes(filename):
    codes = []
    with open(filename) as f:
        for line in f:
            print(line.strip())
            result = re.match('(\d+)\s*-\s*(\d+)\s*(\w)\s*(\w)', line.strip())
            codes.append((int(result[1]), (result[3], result[4])))

    # print(codes)
    return codes

def process_names_and_codes(filename_codes, filename_names, filename_output):

    codes = get_codes(filename_codes)

    with open(filename_names) as f_n:
        with open(filename_output, 'w') as f_o:
            for line in f_n:
                name, wert = line.strip().split(' ')
                # print(wert)
                pos = bisect.bisect_right(codes, (int(wert),))
                # print(pos)
                # print(codes[pos - 1])
                code = codes[pos - 1][1]

                f_o.write(f'{name}\t{wert}\t{code[0]}\t{code[1]}\n')


if __name__ == "__main__":
    filenames = read_arguments()
    print(filenames)
    codes = process_names_and_codes(filenames['codes'], filenames['names'], filenames['output'])
