# Code to find the length of the longest increasing sequence

def lis(sn):
    length_longest = []
    for i in range(len(sequence_of_numbers)):
        length_longest.append(1)
    for i in range(0, len(sn)):
        for j in range(0, i ):
            print('sn[{}] : {} | sn[{}] : {} | ll[{}] : {} | ll[{}]:{}'.format(i,sn[i],j,sn[j],i,length_longest[i],j,length_longest[j] ))
            if sn[j] < sn[i] and length_longest[j] >= length_longest[i]:
                length_longest[i] = 1 + length_longest[j]

    return length_longest
    

def max_lis_length(sequence_of_numbers):
    return max(lis(sequence_of_numbers))

def main(sequence_of_numbers):
    print('Max length : {}'.format(max_lis_length(sequence_of_numbers))) 

if __name__ == '__main__':
    sequence_of_numbers = [ 3,4,5,1,3,4,9 ]
    print(sequence_of_numbers)
    main(sequence_of_numbers)
