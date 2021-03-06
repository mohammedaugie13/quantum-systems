import abc


class OneDimPotential(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, x):
        pass


class HOPotenial(OneDimPotential):
    def __init__(self, mass, omega):
        self.mass = mass
        self.omega = omega

    def __call__(self, x):
        return 0.5 * self.mass * self.omega ** 2 * x ** 2


class DWPotential(HOPotenial):
    def __init__(self, mass, omega, l):
        super().__init__(mass, omega)
        self.l = l

    def __call__(self, x):
        return super().__call__(x) + 0.5 * self.mass * self.omega ** 2 * (
            0.25 * self.l ** 2 - self.l * abs(x)
        )


class DWPotentialSmooth(OneDimPotential):
    """
    This is the double-well potential used by J. Kryvi and S. Bøe in theirs 
    thesis work. See Eq. [13.11] in Bøe: https://www.duo.uio.no/handle/10852/37170
    """

    def __init__(self, a=4):
        self.a = a

    def __call__(self, x):
        return (
            (1.0 / (2 * self.a ** 2))
            * (x + 0.5 * self.a) ** 2
            * (x - 0.5 * self.a) ** 2
        )


class GaussianPotential(OneDimPotential):
    def __init__(self, weight, center, deviation, np):
        self.weight = weight
        self.center = center
        self.deviation = deviation
        self.np = np

    def __call__(self, x):
        return -self.weight * self.np.exp(
            -(x - self.center) ** 2 / (2.0 * self.deviation ** 2)
        )
