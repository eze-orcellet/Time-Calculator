def add_time(start, duration, day=""):

    # tupla de días
    Days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",
            "Saturday")

    [T, AmPm] = start.split(" ")
    [H, M] = T.split(":")

    [Hd, Md] = duration.split(":")

    # con esto tengo las horas en 24 horas, para poder despues calcular los días
    if AmPm == "PM":
        H = int(H) + 12

    NH = int(H) + int(Hd)
    NM = int(M) + int(Md)

    # si los minutos que se suman supera los 60, se suma eso a las horas calculadas
    if NM >= 60:

        addH = NM // 60
        NM = NM % 60
        NH = NH + addH

    # si las horas dejan resto menor que 12 cuando las divido por 24 es porque es AM
    if NH % 24 < 12:
        AmPm = "AM"
    else:
        AmPm = "PM"

    Ndias = NH // 24

    if Ndias == 1:
        aa = " (next day)"
    elif Ndias == 0:
        aa = ""
    else:
        aa = " " + f"({Ndias} days later)"

    # aca comienza el tema del dia opcional
    # bb = Days.index(day)
    # ND = ", " + str(Days[(bb + Ndias % 7)])

    d = day

    r = d.capitalize()

    # print(r)

    if r == "":
        day = ""

    if r == "Monday":
        day = ", " + Days[(1 + Ndias) % 7]

    elif r == "Tuesday":
        day = ", " + Days[(2 + Ndias) % 7]

    elif r == "Wednesday":
        day = ", " + Days[(3 + Ndias) % 7]

    elif r == "Thursday":
        day = ", " + Days[(4 + Ndias) % 7]

    elif r == "Friday":
        day = ", " + Days[(5 + Ndias) % 7]

    elif r == "Saturday":
        day = ", " + Days[(6 + Ndias) % 7]

    elif r == "Sunday":
        day = ", " + Days[(0 + Ndias) % 7]

    if AmPm == "Am":
        if NH % 12 == 0:
            NH = "12"
    else:
        pass

    if NH > 12:
        NH = NH % 12

    if NH == 0:
        NH = "12"

    # for i in range(0, 9):
    #     if NH == i:
    #         NH = "0" + f"{i}"

    for i in range(0, 9):
        if NM == i:
            NM = "0" + f"{i}"

    new_time = str(NH) + ":" + str(NM) + str(" " + AmPm) + str(day) + str(aa)

    # print(T, AmPm, H, M, NH, NM)
    return print(new_time)


add_time("11:43 PM", "24:20", "tueSday")
