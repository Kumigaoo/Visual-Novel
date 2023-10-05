# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("bakemono")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

    e "Colgado? Creo que está muy visto, ni siquiera sé hacer nudos."
    e "Tirarse a las vías del tren? Retrasaría a los trenes y molestaría a mucha gente."
    e "Seguro que eso haría que me odien."
    e "Me gusta la idea de que me odien, lo merezco."
    
    default menuset= set()

    menu:
        "Has pensado en saltar de un hospital? A lo mejor matas a alguien y haces que más gente te odie.":
            e "Buena idea pero le tengo un poco de panico a las alturas, pero no lo descarto."

        "Porque te querrías matar?":
            $ No_Suicidio1 = True
            e "Porque no querría hacerlo?"   
        
        "Es bastante triste que te guste la idea de que te odien, debes ser muy patético.":
            e "No te equivocas."
    
    label after_menu:
        e "*suspiro*
        Porqué tiene que ser tan complicado conseguir una pistola."
    
    menu:
        "No vuelvas a hacer eso del suspiro de los asteriscos, se ve muy raro.":
            $ Romper= True

            e "De qué hablas?"
        "Menos mal, me sentiría inseguro si gente como tu pudiera tener un arma.":
            $ Romper = False
            e "Oye que yo solo la usaría conmigo mismo, nunca dispararía a nadie que no lo mereza pues muy bestía que sea."

        "Sigo insistiendo en que no deberias pensar en suicidarte.":
            $ Romper = False
            $ No_Suicidio2 = True
            e "Deja de insistir en ello, no sirves para eso."

    menu paranoia:
        "Ya sabes de lo que estoy hablando, los asteriscos del suspiro en la caja de texto." if Romper:
            e "No, no sé de lo que hablas, no otra vez."
    menu :
        "A que te refieres con otra vez?" if Romper:
            e "Otra vez, ahora te ibas a poner a hablar sobre una pantalla, una novela visual y cosas así para que me vuelva loco."
    menu :
        "bueno vale" if Romper:
            e "perfecto"

    label FIRE_chapter:
        e "Bueno, después de haberlo pensado ya lo he decidido, pienso ser la cosa más bella de la humanidad, fuego, voy a arder hasta la muerte"
        


    ""

    # This ends the game.

    return
