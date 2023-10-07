#!/usr/bin/env python3
"""Placeholders"""

import tensorflow as tf


def create_placeholders(nx, classes):
    """
    function returns 2 placeholders x & y
    nx: the number of feature columns in our data
    classes: the number of classes in our classifier
    """
    x = tf.placeholder(float, shape=(None, nx), name="x")
    y = tf.placeholder(float, shape=(None, classes), name="y")
    return x, y
