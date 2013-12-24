def approx_equal(a, b):
    return abs(a-b) < 0.000001


def create_transitions():
    transitions = {}
    def bois_ok(activities_sum):
        return approx_equal(activities_sum["Rbois"] * 10, activities_sum["Cbois"])

    def tarte_ok(activities_sum):
        return approx_equal(activities_sum["Rtarte"] * 7, activities_sum["Ctarte"])

    transitions["bois_ok"] = bois_ok
    transitions["tarte_ok"] = tarte_ok

    return transitions
