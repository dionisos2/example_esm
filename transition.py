from utils import *

class Transition:
    def __init__(self, transitions, productions):
        self.transitions = transitions
        self.productions = productions

    def __getitem__(self, key):
        return self.transitions[key]

    def __setitem__(self, key, value):
        self.transitions[key] = value

    def is_production(self, economic_activity):
        return (economic_activity in self.productions)

    def is_consumption(self, economic_activity):
        return not(is_production(economic_activit))


def create_transitions():
    # Du bois et des tartes
    transitions = {}
    def bois_ok(activities_sum):
        return approx_equal(activities_sum["Rbois"] * 10, activities_sum["Cbois"])

    def tarte_ok(activities_sum):
        return approx_equal(activities_sum["Rtarte"] * 7, activities_sum["Ctarte"])

    transitions["check"] = {}
    transitions["check"]["bois_ok"] = bois_ok
    transitions["check"]["tarte_ok"] = tarte_ok


    def induced_by_Rbois(Rbois):
        return ("Cbois", Rbois * 10)

    def induced_by_Cbois(Cbois):
        return ("Rbois", Cbois / 10)

    def induced_by_Rtarte(Rtarte):
        return ("Ctarte", Rtarte * 7)

    def induced_by_Ctarte(Ctarte):
        return ("Rtarte", Ctarte / 7)

    transitions["induced"] = {}
    transitions["induced"]["Rbois"] = induced_by_Rbois
    transitions["induced"]["Cbois"] = induced_by_Cbois
    transitions["induced"]["Rtarte"] = induced_by_Rtarte
    transitions["induced"]["Ctarte"] = induced_by_Ctarte

    transitions["economic_activities"] = {}
    transitions["economic_activities"] = ["Rbois", "Cbois", "Rtarte", "Ctarte"]

    transition = Transition(transitions, ["Rbois", "Rtarte"])
    return transition

def create_transitions_2():
    # des pommes et des poires
    transitions = {}
    def pomme_ok(activities_sum):
        return approx_equal(activities_sum["Rpomme"], activities_sum["Cpomme"])

    def poire_ok(activities_sum):
        return approx_equal(activities_sum["Rpoire"], activities_sum["Cpoire"])

    transitions["check"] = {}
    transitions["check"]["pomme_ok"] = pomme_ok
    transitions["check"]["poire_ok"] = poire_ok


    def induced_by_Rpomme(Rpomme):
        return ("Cpomme", Rpomme)

    def induced_by_Cpomme(Cpomme):
        return ("Rpomme", Cpomme)

    def induced_by_Rpoire(Rpoire):
        return ("Cpoire", Rpoire)

    def induced_by_Cpoire(Cpoire):
        return ("Rpoire", Cpoire)

    transitions["induced"] = {}
    transitions["induced"]["Rpomme"] = induced_by_Rpomme
    transitions["induced"]["Cpomme"] = induced_by_Cpomme
    transitions["induced"]["Rpoire"] = induced_by_Rpoire
    transitions["induced"]["Cpoire"] = induced_by_Cpoire

    transitions["economic_activities"] = {}
    transitions["economic_activities"] = ["Rpomme", "Cpomme", "Rpoire", "Cpoire"]

    transition = Transition(transitions, ["Rpomme", "Rpoire"])
    return transition
