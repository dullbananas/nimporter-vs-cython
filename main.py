import time


# Test Cython
import pyximport; pyximport.install(language_level=3)
import c_mod

start_time = time.time()
print(c_mod.primes(1000))
elapsed = time.time() - start_time
print(f'Cython took {elapsed} seconds to run')
