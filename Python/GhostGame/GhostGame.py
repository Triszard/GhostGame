import pygame

(width, height) = (1000, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

font = pygame.font.SysFont("Comic Sans MS", 20)

def textObjekt(text, font):
    textFlaeche = font.render(text, True, (0,0,0))
    return textFlaeche,textFlaeche.get_rect()

def button(bx,by,laenge,hoehe,randDicke,randFarbe,farbe_normal,farbe_aktiv,nachricht):
    global aktiv
    global build
    global eingelogteFeldposition
    if maus[0] > bx and maus[0] < bx+laenge and maus[1] > by and maus[1] < by+hoehe:
        pygame.draw.rect(screen, farbe_aktiv, (bx,by,laenge,hoehe))
        if klick[0] == 1 and aktiv == False:
            aktiv = True
            if nachricht == "Tür 1":
                    pygame.time.wait(50)
                    print("Tür geklickt")
        if klick[0] == 0:
            aktiv = False
    else:
        pygame.draw.rect(screen, farbe_normal, (bx,by,laenge,hoehe))
    pygame.draw.rect(screen, randFarbe, (bx,by,laenge,hoehe),randDicke)
    textGrund,textKasten = textObjekt(nachricht,font)
    textKasten.center = ((bx+(laenge/2)),(by+(hoehe/2)))
    screen.blit(textGrund, textKasten)