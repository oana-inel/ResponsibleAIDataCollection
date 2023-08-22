#Functions used to generate sets of workers per item
import pandas as pd
import itertools as it
import random
import os
import numpy as np


def get_uniq_unit_ids(df):
    unique_unit_ids = df["ItemIndex"].unique()
    return unique_unit_ids

def get_no_work_unit_id(df, unit_id):
    subset_unit_id = df[df["ItemIndex"] == unit_id]
    return (len(subset_unit_id), subset_unit_id)

def count_bits(number, n_bits):
    ret = 0
    bit_pos = []
    for i in range(0, n_bits):
        if (1 << i) & number != 0:
            ret += 1
            bit_pos.append(i)
    return (ret, bit_pos)

def gen_all_k_combinations(k, num_size):
    result = []
    for i in range(1, 2**num_size):
        bit_count, bit_pos = count_bits(i, num_size)
        if bit_count == k:
            result.append(bit_pos)
    return result

def gen_all_worker_combinations(subset_size, count, subset_unit_id):
    combinations = gen_all_k_combinations(subset_size, count)
    final_result = []
    for comb in combinations:
        crnt_workers = []
        for j in range(0, len(comb)):
            crnt_workers.append(subset_unit_id["Rater"].iloc[comb[j]])
        final_result.append(crnt_workers)
    return final_result

def get_all_unit_combinations(unit_dict):
    sorted_unit_dict = sorted(unit_dict)
    combinations = it.product(*(unit_dict[unit_id] for unit_id in sorted_unit_dict))
    #print(list(combinations))

def my_product(dicts):
    units, comb_of_workers = zip(*dicts.items())
    return [dict(zip(units, x)) for x in it.product(*comb_of_workers)]

def pick_random_worker_set(worker_sets):
    return random.choice(worker_sets)

