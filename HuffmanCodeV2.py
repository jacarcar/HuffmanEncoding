#finds the huffman code, entropy, average length of the codewords & efficiency
import math
def main():
    # I couldn't do it without the 2 dicts because I want to destroy 1 of them
    # but it does work for numbers that end up being the same
    huffman={}
    frequencies={}
    counter=0
    freq={'A':20,'B':50,'C':220,'D':120,'E':200,'F':300}
    while len(freq) > 1:
        tiny=0
        smol=0
        # find the 2 smallest values
        for a in freq:
            if tiny==0:
                tiny=a
            elif smol==0:
                smol=a
            elif freq[a] < freq[tiny]:
                tiny=a
            elif freq[a] < freq[smol]:
                smol=a
            # make the secondary dict
            if counter==0:
                frequencies[a]=freq[a]
        counter+=1
        # assign 0 and 1
        huffman[tiny]='0'+huffman.get(tiny,'')
        huffman[smol]='1'+huffman.get(smol,'')
        # put in combination of the 2 smallest
        freq[tiny+smol]=freq[tiny]+freq[smol]
        # remove the used ones
        del freq[tiny]
        del freq[smol]
    for f in freq:
        num=freq[f]
    # translate to huffman code
    code={}
    for c in huffman:
        for i in c:
            code[i]=huffman[c]+code.get(i,'')
    # find the average length of the codewords
    total=0
    for e in code:
        print(e+':'+code[e],'\n')
        total+=len(code[e])*frequencies[e]
    # find the entropy of the info
    entropy=0
    for g in frequencies:
        entropy+=frequencies[g]/num*math.log2(num/frequencies[g])
    # print it out
    print('Entropy: '+str(entropy))
    print('Average length of codewords: '+str(total/num))
    print('Efficiency: '+str(entropy/(total/num)))
main()
