import time


# Test Cython
import pyximport; pyximport.install(language_level=3)
import c_mod

start_time = time.time()
c_mod.primes(1000)
elapsed = time.time() - start_time
print(f'Cython took {elapsed} seconds to run')


# Test Nimporter
import nimporter
import nim_mod

start_time = time.time()
nim_mod.primes(1000)
elapsed = time.time() - start_time
print(f'Nimporter took {elapsed} seconds to run')
