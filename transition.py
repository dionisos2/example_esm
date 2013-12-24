def approx_equal(a, b):
    return abs(a-b) < 0.000001


def create_transitions():
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

    return transitions
