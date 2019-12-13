# Test Cython
import pyximport; pyximport.install()
import c_mod
print(c_mod.primes(1000))
