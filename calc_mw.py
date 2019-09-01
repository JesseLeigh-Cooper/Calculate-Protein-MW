"""
Author: Jesse Leigh-Cooper
Created: May 2019
"""

unformatted_sequence = "Insert Amino Acid Sequence Here" ##<--sequence


sequence = unformatted_sequence.upper()
residue_mw_dict = {
      "A": 89.10,
      "R": 174.20,
      "N": 132.12,
      "D": 133.11,
      "C": 121.16,
      "E": 147.13,
      "Q": 146.15,
      "G": 75.07,
      "H": 155.16,
      "I": 131.18,
      "L": 131.18,
      "K": 146.19,
      "M": 149.21,
      "F": 165.19,
      "P": 115.13,
      "S": 105.1,
      "T": 119.1,
      "W": 204.2,
      "Y": 181.2,
      "V": 117.1
      }

def calc_mw(sequence):
    accumulator = 0
    for character in sequence:
        accumulator+= residue_mw_dict[character]
        # 18 represents molecular weight lost by h20 formed from peptide bonds
        adjusted_mass = accumulator - (18*len(sequence))+18
        kda = round(adjusted_mass/1000, 1)
    return kda
mw = calc_mw(sequence)
print("Molecular weight of sequence = "+str(mw)+" kDa")