#!/usr/bin/env python3
"""task 0 concolutional forward prop"""

import numpy as np


def conv_forward(A_prev, W, b, activation, padding='same', stride=(1, 1)):
    """write a function that performs forward propagation over cnn"""
    # retrieving dimensions from A_prev shape
    (m, h_prev, w_prev, c_prev) = A_prev.shape

    # retrieving dimesions from W's shape
    (kh, kw, c_prev, c_new) = W.shape

    # retrieving information from 'stride'
    sh, sw = stride

    # Padding
    if padding == 'same':
        ph = int(((h_prev - 1) * sh + kh - h_prev) / 2) + 1
        pw = int(((w_prev - 1) * sw + kw - w_prev) / 2) + 1
    elif padding == 'valid':
        ph, pw = 0, 0

    # applying padding to the previous layer
    A_prev_pad = np.pad(A_prev, ((0, 0), (ph, ph), (pw, pw), (0, 0)),
                        'constant', constant_values=0)

    # Computing the dimensions of the CONV output volume
    h_new = int((h_prev + 2 * ph - kh) / sh) + 1
    w_new = int((w_prev + 2 * pw - kw) / sw) + 1

    # Initializing the output volume Z with 0
    Z = np.zeros((m, h_new, w_new, c_new))

    # Looping over the vertical(h) and horizontal(w) axis of the output vol
    for i in range(h_new):
        for j in range(w_new):
            # looping over the channels(c_new)
            for k in range(c_new):
                # creating slices
                v_start = i * sh
                v_end = v_start + kh
                h_start = j * sw
                h_end = h_start + kw

                # computing convolution
                Z[:, i, j, k] = np.sum(np.multiply(
                    A_prev_pad[:, v_start:v_end, h_start:h_end, :],
                    W[:, :, :, k]), axis=(1, 2, 3))

                # adding bias
                Z[:, i, j, k] = Z[:, i, j, k] + b[:, :, :, k].reshape(1, 1, 1)

    # aplying activation
    A = activation(Z)

    return A
