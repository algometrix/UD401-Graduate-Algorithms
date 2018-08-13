# Code to find the length of the longest increasing sequence

length_longest = []

def lis(sn):
    global length_longest
    for i in range(0, len(sn)):
        print(" I : {}".format(i))
        for j in range(0, i ):
            print(" J : {}".format(j))
            print('sn[{}] : {} | sn[{}] : {} | ll[{}] : {} | ll[{}]:{}'.format(j,sn[j],i,sn[i],j,length_longest[j],i,length_longest[i] ))
            if sn[j] < sn[i] and length_longest[j] >= length_longest[i]:
                length_longest[i] = 1 + length_longest[j]

def max_lis_length(sequence_of_numbers):
    lis(sequence_of_numbers)

def main(sequence_of_numbers):
    max_lis_length(sequence_of_numbers)

if __name__ == '__main__':
    sequence_of_numbers = [ 1,0,3,6,2 ]
    for i in range(len(sequence_of_numbers)):
        length_longest.append(1)
    
    print(sequence_of_numbers)
    main(sequence_of_numbers)
    print(length_longest)
