variable = 78685486
match variable:
    case 5:
        print("Vale 5")
    case 10:
        print("Nuestra variable vale 10")
    case "hola":
        print("Hola a ti también")
    case _:
        print("Entró al caso por default")