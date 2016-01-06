def TowersofHanoi(n, frompeg, topeg, auxpeg):
    # if only one disc is there, simply move it from 'from' peg to 'to' peg
    if n == 1:
        print("Move disc 1 from %c peg to %c peg" %(frompeg, topeg))
        return
    # move the top (n-1) discs from 'from' peg to 'aux' peg using 'to' peg
    TowersofHanoi(n-1, frompeg, auxpeg, topeg)
    #  move the nth disc from 'from' peg to 'to' peg
    print("Move disc %d from %c peg to %c peg" %(n, frompeg, topeg))
    # move the top (n-1) discs from 'aux' peg to 'to' peg using 'from' peg
    TowersofHanoi(n-1, auxpeg, topeg, frompeg)

TowersofHanoi(4, 'A', 'C', 'B')
