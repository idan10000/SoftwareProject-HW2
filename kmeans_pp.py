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

    obs = pd.read_csv(f'{args.filename}', header=None)
    initial, ind = k_means_pp(obs, N, K, d)
    print_ind(ind)
    mykmeanssp.kmeans(MAX_ITER, obs.values.tolist(), initial.tolist())


def print_ind(vec):
    str_lst = []
    for i in range(vec.size):
        str_lst.append(str(vec[i]))
    print(','.join(str_lst))


def calc_d(obs, cents, i):
    vec = obs[i, :]
    dist = np.linalg.norm(cents - vec, axis=1)
    return dist.min() ** 2


def update_dists(obs, D1, m, N):
    new_vec = obs[m, :]
    new_dists = np.zeros([N, 2])
    new_dists[:, 0] = (np.linalg.norm(obs - new_vec, axis=1))**2
    new_dists[:, 1] = D1
    return new_dists.min(axis=1)


def k_means_pp(obs, N, K, d):
    np.random.seed(0)  # Seed randomness
    mat = obs.to_numpy()
    initial = np.zeros([K, d])
    ind = np.zeros(K, dtype=int)
    i = np.random.choice(N, 1)
    ind[0] = i
    initial[0, :] = mat[i, :]
    cent = mat[i, :]
    D1 = (np.linalg.norm(mat - cent, axis=1))**2
    for j in range(1, K):
        s = sum(D1)
        P = D1 / s

        m = np.random.choice(N, 1, p=P)
        ind[j] = m
        initial[j, :] = mat[m, :]
        D1 = update_dists(mat, D1, m, N)
    return initial, ind


main()
