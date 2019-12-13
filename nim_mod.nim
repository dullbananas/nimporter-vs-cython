import nimpy

proc primes() {.exportpy.} =
    var n, i, len_p: int32
    var p: array[0..1000, int32]
    var uwu: bool
    
    len_p = 0
    n = 2
    while len_p < 1000:
        uwu = true
        for h in 0..len_p:
            i = p[h]
            # prevent 0 division
            if i == 0:
                break
            if n mod i == 0:
                uwu = false
                break
        
        if uwu:
            p[len_p] = n
            len_p += 1
        n += 1
