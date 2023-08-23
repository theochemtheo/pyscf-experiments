import numpy as np
from pyscf import gto

def ozone_geom(mol: gto.Mole) -> np.ndarray:
    coords = mol.atom_coords(unit="ANG")
    o1_o2 = np.linalg.norm(coords[0, :] - coords[1, :])
    o1_o3 = np.linalg.norm(coords[0, :] - coords[2, :])
    o2_o3 = np.linalg.norm(coords[1, :] - coords[2, :])
    ooo = np.arctan2(coords[2, 1] - coords[0, 1], coords[2, 0] - coords [0, 0]) - np.arctan2(coords[1, 1] - coords[0, 1], coords[1, 0] - coords [0, 0])
    blengths = [o1_o2, o1_o3, o2_o3]
    return [np.mean(blengths), np.std(blengths), *blengths, ooo / (2 * np.pi) * 360]

def ozgeom_print(array: np.ndarray) -> None:
    print(f"{array[2]:.3f} {array[3]:.3f} {array[5]:.2f}˚")