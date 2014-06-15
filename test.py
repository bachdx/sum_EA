def num(i):
    try:
        return int(i)
    except:
        return -1

def _sumR(_array, _id, _count):
    ret = 0
    if(_count <=0):
        return 0;
    if(num(_array[_id]) < 0):
        ret += _sumR(_array, _id + 1, _count)
    else:
        try:
            _count -= 1
            ret += num(_array[_id]) * num(_array[_id])
            ret += _sumR(_array, _id + 1, _count)
        except:
            print "Please check your line format! [list index out of range]"
            return "-1"
    return ret

def _sumR_start(_array, _count):
    sum2 = _sumR(_array.split(), 0, _count)
    print sum2
    print >> f_out, sum2

def _calcul(_array, _min, _max):
    ret = 0;
    if(_min > _max):
        return ret;
    else:
        #try with a block of line
        try:
            _sumR_start(_array[_min * 2], num(_array[_min * 2 - 1]))    #array = lines[1*2], count = lines[1*2 - 1], ...
            _calcul(_array, _min + 1, _max)                             #try with other block
        except:
            print "Please check your file format! [list index out of range]"

N=0;
f_out = open("ret.txt", "a+")
with open('dat.txt') as f_in:
    lines = f_in.readlines()
    count = len(lines)
    
    N = num(lines[0])
    #print "N: ", N
    _calcul(lines, 1, N)
f_out.close()
