# finds the huffman code, entropy, average length of the codewords & efficiency 
import math
def main():
    # I couldn't find out how to do it without both of these dicts
    # only works if the numbers never end up being the same
    # number=key, letter=value
    freq={}
    # letter=key, number=value
    frequencies={'A':20,'B':50,'C':220,'D':120,'E':200,'F':300}
    # only need one of the dicts at start
    if freq == {}:
        try:
            for c in frequencies:
                freq[frequencies[c]]=c
        except KeyError:
            print("I can't do that")
            return
    if frequencies=={}:
        for d in freq:
            frequencies[freq[d]]=d
    huffman={}
    my_list=[]
    # get the values to compare them
    for e in frequencies:
        my_list.append(frequencies[e])
    my_list.sort()
    # the core of it
    while len(my_list) > 1:
        try:
            tiny = my_list[0]
            big = my_list[1]
            my_list.append(tiny+big)
            huffman[freq[tiny]]='0'+huffman.get(freq[tiny],'')
            huffman[freq[big]]='1'+huffman.get(freq[big],'')
            freq[tiny+big]=freq[tiny]+freq[big]
            del freq[tiny]
            del freq[big]
        # if the numbers end up being the same at some point
        except KeyError:
            print("I can't do that")
            return
        # make the list smaller
        my_list.remove(my_list[0])
        my_list.remove(my_list[0])
        my_list.sort()
    for f in freq:
        num=f
    # translate to huffman code
    code={}
    for a in huffman:
        for i in a:
            code[i]=huffman[a]+code.get(i,'')
    total=0
    # find the average length of the codewords
    for b in code:
        print(b+':'+code[b],'\n')
        total+=len(code[b])*frequencies[b]
    entropy=0
    # find the entropy of the info
    for g in frequencies:
        entropy+=frequencies[g]/num*math.log2((num)/frequencies[g])
    print("Entropy: "+str(entropy))
    print("Average length of codewords: "+str(total/num))
    print("Efficiency: "+str(entropy/(total/num)))
main()
