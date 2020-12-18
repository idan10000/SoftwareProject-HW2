import numpy as np
import pandas as pd

vec=np.array([1,1,1])
mat = np.array([[1,2,1],[0,1,0]])
mat2 = np.array([[1,1,1],[0,1,0]])
mat[1,:]=mat2[0,:]

# for i in range(N):
#     D[i] = calc_d(mat, cents, i)
#
#
#     def calc_d(obs, cents, i):
#         vec = obs[i, :]
#         dist = np.linalg.norm(cents - vec, axis=1)
#         return dist.min() ** 2

mat1 = np.array([[1,2,1],[0,1,0]])
mat2 = np.array([[2,2,1],[2,1,0],[0,1,0]])

# dists =

def calc_d(vec,mat):
    dist = np.linalg.norm(mat-vec,axis=1)
    return dist.min()**2

def calc_all_d(mat1,mat2):
    d = np.linalg.norm(mat1 - vec, axis=1)