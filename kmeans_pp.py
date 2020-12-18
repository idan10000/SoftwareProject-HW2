import argparse
import numpy as np
import pandas as pd
import mykmeanssp

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("K", type=int)
    parser.add_argument("N", type=int)
    parser.add_argument("d", type=int)
    parser.add_argument("MAX_ITER", type=int)
    parser.add_argument("filename", type=str)

    args = parser.parse_args()

    K = args.K
    N = args.N
    d = args.d
    MAX_ITER = args.MAX_ITER

    if K >= N or K <= 0 or N <= 0 or d <= 0 or MAX_ITER <= 0:
        print("Error in arguments")
        exit()

    obs = pd.read_csv(f'{args.filename}',header=None)
    initial=k_means_pp(obs, N, K, d)
    print(initial.dtype)
    print(initial)
    #mat = obs.to_numpy()
    #print(mat)
    #print('a')
    mykmeanssp.kmeans(MAX_ITER,obs,initial)


def calc_d(obs,cents, i):
    vec = obs[i,:]
    dist = np.linalg.norm(cents-vec,axis=1)
    return dist.min()**2

#delete this after
def calc_test(vec,mat):
    dist = np.linalg.norm(mat-vec,axis=1)
    print(dist)



def k_means_pp(obs, N , K , d):
    np.random.seed(0) #Seed randomness
    mat = obs.to_numpy()
    initial = np.zeros([K,d])
    i = np.random.choice(N,1)
    initial[0,:]=mat[i,:]
    for j in range(1,K):
        cents = initial[:j,:]
        D = np.zeros(N)
        for i in range(N):
            D[i] = calc_d(mat, cents, i)
            # D = [calc_d(mat,cents,i) for i in range(N)]
        s = sum(D)
        P = D/s
        #
        # P = np.zeros(N)
        # for i in range(N):
        #     P[i] = D[i]/s
        # P = [D[i]/s for i in range(N)]
        m = np.random.choice(N,1,p=P)
        initial[j, :] = mat[m, :]
    return initial


# vec=np.array([1,1,1])
# mat = np.array([[1,2,1],[0,1,0]])
# mat2 = np.array([[1,1,1],[0,1,0]])
# mat[1,:]=mat2[0,:]
#print(mat)

#calc_test(vec,mat)


main()