from distribution import Distribution, Distribution_factory
import copy

class Distribution_finder:
    def __init__(self, distribution_factory):
        self.distribution_factory = distribution_factory
        self.create_exemples()

    


    def create_exemples(self):
        distribution_dict_1 = {"Albert":{"Rbois":0.5, "Cbois":5, "Rtarte":0, "Ctarte":0},
                               "Béatrice":{"Rbois":0.5, "Cbois":5, "Rtarte":0, "Ctarte":0},
                               "Claude":{"Rbois":0.5, "Cbois":5, "Rtarte":0, "Ctarte":0},
                               "Denis":{"Rbois":0.5, "Cbois":5, "Rtarte":0, "Ctarte":0},
                               "Emilie":{"Rbois":0.5, "Cbois":5, "Rtarte":0, "Ctarte":0}}

        distribution_dict_2 = {"Albert":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Béatrice":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Claude":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Denis":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Emilie":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0}}

        distribution_dict_3 = {"Albert":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Béatrice":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Claude":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Denis":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0},
                               "Emilie":{"Rbois":1, "Cbois":10, "Rtarte":0, "Ctarte":0}}


        self.distribution_1 = self.distribution_factory.create_distribution(distribution_dict_1)
        self.distribution_2 = self.distribution_factory.create_distribution(distribution_dict_2)
        self.distribution_3 = self.distribution_factory.create_distribution(distribution_dict_3)


