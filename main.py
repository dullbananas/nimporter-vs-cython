# Test Cython
import pyximport; pyximport.install(language_level=3)
import c_mod
print(c_mod.primes(1000))
