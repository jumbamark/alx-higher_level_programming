#!/usr/bin/python3
"""
Module containing a function that multiples 2 matrices by using
the module Numpy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiples m_a and m_b using Numpy

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multiplication

    """
    return (np.matmul(m_a, m_b))
