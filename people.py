# Albert:vert Béatrice:rouge Claude:violet Denis:bleu Emilie:jaune

def create_people_2():
    people = {}
    people["Albert"] = {}
    people["Béatrice"] = {}
    people["Albert"]["Rpomme"] = {"coef": -1, "max": 10}
    people["Albert"]["Cpomme"] = {"coef": 1, "max": 10}
    people["Albert"]["Rpoire"] = {"coef": -2, "max": 10}
    people["Albert"]["Cpoire"] = {"coef": 2, "max": 20}

    people["Béatrice"]["Rpomme"] = {"coef": -2, "max": 10}
    people["Béatrice"]["Cpomme"] = {"coef": 2, "max": 15}
    people["Béatrice"]["Rpoire"] = {"coef": -1, "max": 10}
    people["Béatrice"]["Cpoire"] = {"coef": 1, "max": 10}

    return create_all_satisfaction_function(people)

def create_all_satisfaction_function(people):
    for citizen in people:
        for economic_activity in people[citizen]:
            satisfaction_coef = people[citizen][economic_activity]["coef"]
            extreme_satisfaction = people[citizen][economic_activity]["max"]

            people[citizen][economic_activity]["satisfaction_function"] = create_satisfaction_function(satisfaction_coef, extreme_satisfaction)

    return people

def create_people():
    people = {}
    people["Albert"] = {}
    people["Béatrice"] = {}
    people["Claude"] = {}
    people["Denis"] = {}
    people["Emilie"] = {}

    for citizen in people.keys():
        people[citizen]["Rbois"] = {"coef":0, "max":0}
        people[citizen]["Cbois"] = {"coef":0, "max":0}
        people[citizen]["Rtarte"] = {"coef":0, "max":0}
        people[citizen]["Ctarte"] = {"coef":0, "max":0}

    people["Albert"]["Rbois"]["coef"] = -1.6
    people["Albert"]["Rbois"]["max"] = -5
    people["Albert"]["Cbois"]["coef"] = 1.2
    people["Albert"]["Cbois"]["max"] = 12
    people["Albert"]["Rtarte"]["coef"] = -1
    people["Albert"]["Rtarte"]["max"] = -3
    people["Albert"]["Ctarte"]["coef"] = 0
    people["Albert"]["Ctarte"]["max"] = 0

    people["Béatrice"]["Rbois"]["coef"] = -2
    people["Béatrice"]["Rbois"]["max"] = -4
    people["Béatrice"]["Cbois"]["coef"] = 0.4
    people["Béatrice"]["Cbois"]["max"] = 10
    people["Béatrice"]["Rtarte"]["coef"] = -0.67
    people["Béatrice"]["Rtarte"]["max"] = -2
    people["Béatrice"]["Ctarte"]["coef"] = 0.5
    people["Béatrice"]["Ctarte"]["max"] = 1

    people["Claude"]["Rbois"]["coef"] = -5
    people["Claude"]["Rbois"]["max"] = -5
    people["Claude"]["Cbois"]["coef"] = 0.75
    people["Claude"]["Cbois"]["max"] = 30
    people["Claude"]["Rtarte"]["coef"] = -1.5
    people["Claude"]["Rtarte"]["max"] = -3
    people["Claude"]["Ctarte"]["coef"] = 1
    people["Claude"]["Ctarte"]["max"] = 5

    people["Denis"]["Rbois"]["coef"] = -1.5
    people["Denis"]["Rbois"]["max"] = -6
    people["Denis"]["Cbois"]["coef"] = 0.5
    people["Denis"]["Cbois"]["max"] = 10
    people["Denis"]["Rtarte"]["coef"] = -0.88
    people["Denis"]["Rtarte"]["max"] = -3.5
    people["Denis"]["Ctarte"]["coef"] = 1.5
    people["Denis"]["Ctarte"]["max"] = 3

    people["Emilie"]["Rbois"]["coef"] = -0.6
    people["Emilie"]["Rbois"]["max"] = -3
    people["Emilie"]["Cbois"]["coef"] = 0.75
    people["Emilie"]["Cbois"]["max"] = 15
    people["Emilie"]["Rtarte"]["coef"] = -0.4
    people["Emilie"]["Rtarte"]["max"] = -2
    people["Emilie"]["Ctarte"]["coef"] = 1
    people["Emilie"]["Ctarte"]["max"] = 4

    return create_all_satisfaction_function(people)

def create_satisfaction_function(satisfaction_coef, extreme_satisfaction):
    def satisfaction_function(x):
        if(x<0):
            return x * 100000

        satisfaction = x*satisfaction_coef
        if(extreme_satisfaction > 0):
            if(satisfaction > extreme_satisfaction):
                satisfaction = extreme_satisfaction
        else:
            if(satisfaction < extreme_satisfaction):
                satisfaction = -abs(x*1000)

        return satisfaction

    return satisfaction_function
