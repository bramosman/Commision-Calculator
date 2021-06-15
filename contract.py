class Contract:

    def __init__(self, associate, business, b, s):
        self.associate = associate
        self.business = business
        self.b = b
        self.s = s
        self.__fixed_fee = 2500
        self.__variable_fee_rate = 0
        self.__commission_rate = 0.05
    def F(self):
        return round (self.__fixed_fee +(0.15 * self.b))
    def TAR(self):
        return (self.s + (12 * self.F()))
    def C(self):
        return (self.TAR() * self.__commission_rate)
    def __str__(self):
        return "{0:20}{1:30}{2:<20.2f}{3:<20.2f}{4:<20.2f}{5:<20.2f}{6:<20.2f}".format(self.associate, self.business, self.b, self.s, self.F(), self.TAR(), self.C())
