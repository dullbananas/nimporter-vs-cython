import time


# Test Cython
import pyximport; pyximport.install(language_level=3)
import c_mod

start_time = time.time()
for _ in range(1000):
    c_mod.primes(1000)
elapsed = time.time() - start_time
print(f'Cython took {elapsed} seconds to run')


# Test Nimporter
import nimporter
import nim_mod

start_time = time.time()
for _ in range(1000):
    nim_mod.primes()
elapsed = time.time() - start_time
print(f'Nimporter took {elapsed} seconds to run')
