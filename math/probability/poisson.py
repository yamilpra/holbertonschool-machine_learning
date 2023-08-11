#!/usr/bin/env python3
""" Represents a poisson distribution: """


class Poisson:
    """ Class constructor """

    def __init__(self, data=None, lambtha=1.):
        """ Attributes
        data:  is a list of the data to be used to estimate the distribution
        lambtha: is the expected number of occurences in a given time frame
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) <= 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """ Calculates the value of the PMF for a given number of “successes”
        k = number of successes
        """
        if k < 0:
            return 0
        k = int(k)
        event = 1
        for i in range(1, k + 1):
            event *= i
        return (self.lambtha ** k * 2.7183 ** (-self.lambtha)) / event

    def cdf(self, k):
        """ Calculates the value of the CDF for a given number of “successes”
        """
        if k < 0:
            return 0
        k = int(k)
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
