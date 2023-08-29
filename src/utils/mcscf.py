from math import comb

def n_csfs(n_orb: int, n_alpha: int, n_beta):
    return comb(n_orb, n_alpha) * comb(n_orb, n_beta) - comb(n_orb, n_alpha + 1) * comb(n_orb, n_beta - 1)