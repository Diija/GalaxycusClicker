import pygame
import shelve
pygame.init()
pygame.font.init()
save = shelve.open('save')
screen = pygame.display.set_mode((1280,720))

#Iniciando imagens, sons e fontes e arquivos

title = pygame.image.load('Title.png')
backgroundmenu = pygame.image.load('Menu.png')
backgroundlab = pygame.image.load('lab.png')

botaojogar = pygame.image.load('JogarButton.png')
botaojogarap = pygame.image.load('JogarButtonAp.png')

botaoinstrucoes = pygame.image.load('InstrucoesButton.png')
botaoinstrucoesap = pygame.image.load('InstrucoesButtonAp.png')

botaohistoria = pygame.image.load('HistoriaButton.png')
botaohistoriaap = pygame.image.load('HistoriaButtonAp.png')

botaosobre = pygame.image.load('SobreButton.png')
botaosobreap = pygame.image.load('SobreButtonAp.png')

instrucoestela = pygame.image.load('Instrucoestela.png')
sobretela = pygame.image.load('Sobretela.png')
historiatela = pygame.image.load('Historiatela.png')
popupstart = pygame.image.load('popupstart.png')

botaofarm = pygame.image.load('Livro.png')
botaofarmap = pygame.image.load('Livro2.png')

botaocarregar = pygame.image.load('CarregarButton.png')
botaocarregarap = pygame.image.load('CarregarButtonap.png')
#botãoupgrades = pygame.image.load('.png')
#dar load nas imagens dos upgrades
#upgrade1_URSS = pygame.image.load('.png')

sound = pygame.image.load('Sound.png')
fonte = pygame.font.Font('Comicoro.ttf', 30)

##salvar = pygame.image.load('Salvar.png')

def menu():

    #Coloca as imagens
    screen.blit(backgroundmenu, (0,0))
    screen.blit(botaojogar, (490,260))
    screen.blit(botaocarregar,(490,340))
    screen.blit(botaoinstrucoes, (490,420))
    screen.blit(botaohistoria, (490,500))
    screen.blit(botaosobre, (490,580))
    screen.blit(title, (390,100))
    screen.blit(sound, (1180,50))
    pygame.display.flip()

    #Eventos clicáveis do Menu

    contador=0
    while(pygame.event.wait() or pygame.event.get()):
        
        #Pega a posição do mouse e
        #(Posição hitbox direita) > Posição X do mouse > (Posição hitbox esquerda) and (Posição hitbox baixo) > Posição Y do mouse > (Posição hitbox cima) então:
        
        mouse=pygame.mouse.get_pos()
        #Jogar
        if 490+300 > mouse[0] > 490 and 260+62 > mouse[1] > 260:
            screen.blit(botaojogarap, (490,260))
            if pygame.mouse.get_pressed()[0]:
                print("Inicio jogo")
                gameinit()
        else:
            screen.blit(botaojogar, (490,260))
        #Carregar
        if 490+300 > mouse[0] > 490 and 340+62 > mouse[1] > 340:
            screen.blit(botaocarregarap, (490,340))
            if pygame.mouse.get_pressed()[0]:
                print("Ainda em construção")
##                save = shelve.open('save')
##                pesquisa = save['pesquisa']
##                primeiravez = save['primeiravez']
##                shelfFile.close()
##                gameinit()
        else:
            screen.blit(botaocarregar, (490,340))
        #Instruções
        if 490+300 > mouse[0] > 490 and 420+62 > mouse[1] > 420:
            screen.blit(botaoinstrucoesap, (490,420))
            if pygame.mouse.get_pressed()[0]:
                while(True):
                    screen.blit(instrucoestela, (340,200))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                menu()             
        else:
            screen.blit(botaoinstrucoes, (490,420))
        #História
        if 490+300 > mouse[0] > 490 and 500+62 > mouse[1] > 500:
            screen.blit(botaohistoriaap, (490,500))
            if pygame.mouse.get_pressed()[0]:
                while(True):
                    screen.blit(historiatela, (340,200))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                menu()
        else:
            screen.blit(botaohistoria, (490,500))
        #Sobre
        if 490+300 > mouse[0] > 490 and 580+62 > mouse[1] > 580:
            screen.blit(botaosobreap, (490,580))
            if pygame.mouse.get_pressed()[0]:
                while(True):
                    screen.blit(botaosobre, (490,580))
                    screen.blit(sobretela, (340,200))
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                menu()
        else:
            screen.blit(botaosobre, (490,580))
        #Musica
        if 1180+50 > mouse[0] > 1180 and 50+50 > mouse[1] > 50:
            if pygame.mouse.get_pressed()[0]:
                if contador==0:
                    pygame.mixer.music.stop()
                    contador=1
                elif contador==1:
                    pygame.mixer.music.play(-1,0)
                    contador=0
        pygame.display.flip()

def gameinit():
    contador=0
    pesquisa=0
    modificador=0
    primeiravez=0
    while (pygame.event.wait() or pygame.event.get()):

        mouse=pygame.mouse.get_pos()
        screen.blit(backgroundlab, (0,0))
        screen.blit(botaofarm, (40,360))
        screen.blit(sound, (1180,50))
        #screen.blit(botaoupgrade,(1180,70))
##        screen.blit(salvar, (1100,50))
        pesquisatexto = fonte.render(('Pesquisa: %s' % pesquisa), False, (0,0,0))
        screen.blit(pesquisatexto, (300,100))
        while primeiravez==0:
            screen.blit(backgroundlab, (0,0))
            screen.blit(popupstart, (340,200))
            pygame.display.flip()
            for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                primeiravez=1
        pygame.display.flip()
##        screen.blit(backgroundlab2, (0,0))
##        screen.blit(botaofarm, (40,360))
##        pygame.display.flip()
##        pygame.time.wait(1000)
        
        #Farm
        if 40+200 > mouse[0] > 40 and 360+150 > mouse[1] > 360:
            screen.blit(backgroundlab,(0,0))
            screen.blit(botaofarmap, (40,360))
            screen.blit(sound, (1180,50))
##            screen.blit(salvar, (1100,50))
            if pygame.mouse.get_pressed()[0]:
                pesquisa=pesquisa+1+modificador
            screen.blit(pesquisatexto, (300,100))
            pygame.display.flip()
        else:
            screen.blit(botaofarm, (40,360))
##        #Salvar
##        if 1100+50 > mouse[0] > 1100 and 50+50 > mouse[1] > 50:
##            if pygame.mouse.get_pressed()[0]:
##                save = shelve.open('save')
##                save[pesquisa] = shelfFile['pesquisa']
##                save[primeiravez] = shelfFile['primeiravez']
##                shelfFile.close()
##                print('Salvou')
        #Botão upgrades
        if 1180+70 > mouse[0] > 1180 and 70+70 > mouse[1] > 70:
            if pygame.mouse.get_pressed()[0]:
                while(True):
                    screen.blit(menu_upgrades, (340,200))
                     #dar blit nas imagens do upgrades
                    pygame.display.flip()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pygame.display.flip()               
        
        #Musica
        if 1180+50 > mouse[0] > 1180 and 50+50 > mouse[1] > 50:
            if pygame.mouse.get_pressed()[0]:
                if contador==0:
                    pygame.mixer.music.stop()
                    contador=1
                elif contador==1:
                    pygame.mixer.music.play(-1,0)
                    contador=0
        #BençãodoADM, free pesquisa
        if 1270+10 > mouse[0] > 1270 and 710+10 > mouse[1] > 710:
            if pygame.mouse.get_pressed()[0]:
                pesquisa=pesquisa+100000

contador=0
pesquisa=0
modificador=0
primeiravez=0
music1 = pygame.mixer.music.load('Space.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1,0)
menu()
