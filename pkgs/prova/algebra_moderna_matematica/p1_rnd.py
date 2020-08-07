#!/usr/bin/env python3

import random


def rnd():
    rnd = {}
    rnd[0] = random.randint(99, 999)
    rnd[1] = random.uniform(0, 1)
    return rnd
