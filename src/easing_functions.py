import math

class EasingFunction:
    def __init__(self, weight=1.0):
        self.weight = weight

    def out(self, t):
        raise NotImplementedError

    def in_(self, t):
        raise NotImplementedError

    def in_out(self, t):
        raise NotImplementedError

    def out_in(self, t):
        raise NotImplementedError

    def apply_weight(self, value):
        return value * self.weight

class Exponential(EasingFunction):
    def in_(self, t):
        return self.apply_weight(0 if t == 0 else 2 ** (10 * (t - 1)))

    def out(self, t):
        return self.apply_weight(1 if t == 1 else 1 - 2 ** (-10 * t))

    def in_out(self, t):
        if t == 0 or t == 1:
            return self.apply_weight(t)
        t *= 2
        return self.apply_weight(0.5 * (2 ** (10 * (t - 1)) if t < 1 else 2 - 2 ** (-10 * (t - 1))))

    def out_in(self, t):
        return self.apply_weight(0.5 * self.out(t * 2) if t < 0.5 else 0.5 * self.in_(t * 2 - 1) + 0.5)

class Quad(EasingFunction):
    def in_(self, t):
        return self.apply_weight(t * t)

    def out(self, t):
        return self.apply_weight(1 - (1 - t) * (1 - t))

    def in_out(self, t):
        return self.apply_weight(2 * t * t if t < 0.5 else 1 - (2 * (1 - t)) * (2 * (1 - t)))

    def out_in(self, t):
        return self.apply_weight(0.5 * self.out(t * 2) if t < 0.5 else 0.5 * self.in_(t * 2 - 1) + 0.5)

class Back(EasingFunction):
    def __init__(self, weight=1.0, c1=1.70158, c2=None):
        super().__init__(weight)
        self.c1 = c1
        self.c2 = c2 if c2 is not None else self.c1 * 1.525

    def in_(self, t):
        return self.apply_weight((t ** 2) * ((self.c2 + 1) * t - self.c2))

    def out(self, t):
        t -= 1
        return self.apply_weight((t ** 2) * ((self.c2 + 1) * t + self.c2) + 1)

    def in_out(self, t):
        t *= 2
        if t < 1:
            return self.apply_weight(0.5 * (t ** 2) * ((self.c2 + 1) * t - self.c2))
        t -= 2
        return self.apply_weight(0.5 * ((t ** 2) * ((self.c2 + 1) * t + self.c2) + 2))

    def out_in(self, t):
        return self.apply_weight(0.5 * self.out(t * 2) if t < 0.5 else 0.5 * self.in_(t * 2 - 1) + 0.5)

class Bounce(EasingFunction):
    def out(self, t):
        n1, d1 = 7.5625, 2.75
        if t < 1 / d1:
            return self.apply_weight(n1 * t * t)
        elif t < 2 / d1:
            t -= 1.5 / d1
            return self.apply_weight(n1 * (t * t + 0.75))
        elif t < 2.5 / d1:
            t -= 2.25 / d1
            return self.apply_weight(n1 * (t * t + 0.9375))
        else:
            t -= 2.625 / d1
            return self.apply_weight(n1 * (t * t + 0.984375))

    def in_(self, t):
        return self.apply_weight(1 - self.out(1 - t))

    def in_out(self, t):
        return self.apply_weight(0.5 * self.in_(t * 2) if t < 0.5 else 0.5 * self.out(t * 2 - 1) + 0.5)

    def out_in(self, t):
        return self.apply_weight(0.5 * self.out(t * 2) if t < 0.5 else 0.5 * self.in_(t * 2 - 1) + 0.5)

class Elastic(EasingFunction):
    def in_(self, t):
        if t == 0 or t == 1:
            return self.apply_weight(t)
        p, s = 0.3, 0.3 / 4
        return self.apply_weight(-(2 ** (10 * (t - 1))) * math.sin((t - s) * (2 * math.pi) / p))

    def out(self, t):
        if t == 0 or t == 1:
            return self.apply_weight(t)
        p, s = 0.3, 0.3 / 4
        return self.apply_weight((2 ** (-10 * t)) * math.sin((t - s) * (2 * math.pi) / p) + 1)

    def in_out(self, t):
        if t == 0 or t == 1:
            return self.apply_weight(t)
        t *= 2
        p, s = 0.45, 0.45 / 4
        return self.apply_weight(-0.5 * (2 ** (10 * (t - 1))) * math.sin((t - s) * (2 * math.pi) / p) if t < 1 else (2 ** (-10 * (t - 1))) * math.sin((t - s) * (2 * math.pi) / p) * 0.5 + 1)

    def out_in(self, t):
        return self.apply_weight(0.5 * self.out(t * 2) if t < 0.5 else 0.5 * self.in_(t * 2 - 1) + 0.5)

class Sine(EasingFunction):
    def in_(self, t):
        return self.apply_weight(1 - math.cos((t * math.pi) / 2))

    def out(self, t):
        return self.apply_weight(math.sin((t * math.pi) / 2))

    def in_out(self, t):
        return self.apply_weight(0.5 * (1 - math.cos(math.pi * t)))

    def out_in(self, t):
        return self.apply_weight(0.5 * self.out(t * 2) if t < 0.5 else 0.5 * self.in_(t * 2 - 1) + 0.5)

class Circ(EasingFunction):
    def in_(self, t):
        return self.apply_weight(1 - math.sqrt(1 - t ** 2))

    def out(self, t):
        t -= 1
        return self.apply_weight(math.sqrt(1 - t ** 2))

    def in_out(self, t):
        t *= 2
        return self.apply_weight(0.5 * (1 - math.sqrt(1 - t ** 2))) if t < 1 else self.apply_weight(0.5 * (math.sqrt(1 - (t - 2) ** 2) + 1))

    def out_in(self, t):
        return self.apply_weight(0.5 * self.out(t * 2) if t < 0.5 else 0.5 * self.in_(t * 2 - 1) + 0.5)

class Cubic(EasingFunction):
    def in_(self, t):
        return self.apply_weight(t ** 3)

    def out(self, t):
        t -= 1
        return self.apply_weight((t ** 3) + 1)

    def in_out(self, t):
        t *= 2
        return self.apply_weight(0.5 * (t ** 3)) if t < 1 else self.apply_weight(0.5 * ((t - 2) ** 3 + 2))

    def out_in(self, t):
        return self.apply_weight(0.5 * self.out(t * 2) if t < 0.5 else 0.5 * self.in_(t * 2 - 1) + 0.5)

class Quart(EasingFunction):
    def in_(self, t):
        return self.apply_weight(t ** 4)

    def out(self, t):
        t -= 1
        return self.apply_weight((t ** 4) + 1)

    def in_out(self, t):
        t *= 2
        return self.apply_weight(0.5 * (t ** 4)) if t < 1 else self.apply_weight(0.5 * ((t - 2) ** 4 + 2))

    def out_in(self, t):
        return self.apply_weight(0.5 * self.out(t * 2) if t < 0.5 else 0.5 * self.in_(t * 2 - 1) + 0.5)

class Quint(EasingFunction):
    def in_(self, t):
        return self.apply_weight(t ** 5)

    def out(self, t):
        t -= 1
        return self.apply_weight((t ** 5) + 1)

    def in_out(self, t):
        t *= 2
        return self.apply_weight(0.5 * (t ** 5)) if t < 1 else self.apply_weight(0.5 * ((t - 2) ** 5 + 2))

    def out_in(self, t):
        return self.apply_weight(0.5 * self.out(t * 2) if t < 0.5 else 0.5 * self.in_(t * 2 - 1) + 0.5)

def get_easing_class(easing_type):
    easing_classes = {
        'Exponential': Exponential,
        'Quad': Quad,
        'Back': Back,
        'Bounce': Bounce,
        'Elastic': Elastic,
        'Sine': Sine,
        'Circ': Circ,
        'Cubic': Cubic,
        'Quart': Quart,
        'Quint': Quint,
    }
    return easing_classes.get(easing_type, lambda: EasingFunction())