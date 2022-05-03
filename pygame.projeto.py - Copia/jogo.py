import pygame, random, copy, time

def inicializa():
    pygame.init()
    pygame.mixer.init()
    w = pygame.display.set_mode((1080,600))
    pygame.key.set_repeat(50)
    logo = pygame.image.load('logo.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Diver Adventure')

    state = {
        "merg_x" : 100,
        "merg_y" : 300,
        "tubaroes" : [],
        'rect_tubarao' : []

    }

    assets = {
        'player': pygame.image.load('mergulhador.png'),
        'fundo' : pygame.image.load('fundo2.png'),
        'tubarao': pygame.image.load('tubarao.png'),
        'tela_inicial': pygame.image.load('TELA_INICIAL_JOGO.jpg'),
        'tela_final': pygame.image.load('TELA_FINAL_JOGO.jpg')
    }

    state['tela'] = 2
    state['last_updated'] = 0
    state['last_tubarao'] = 0
    state['t'] = True
    state['inicio'] = pygame.time.get_ticks()



    return w, assets, state




    



def finaliza():
    pygame.quit()


def desenha(window, assets, state):

    if state['tela'] == 2:
        window.blit(assets['tela_inicial'], (0,0))
    
    
    if state['tela'] == 0:

        window.blit(assets["fundo"], (0,0))
        window.blit(assets["player"], (state["merg_x"],state["merg_y"]))

        if state['last_updated'] % 30 == 0:
            state['tubaroes'].append([assets['tubarao'], 1080, random.randint(10, 530 )])
        
        for tubarao in state['tubaroes']:
            window.blit(pygame.image.load('tubarao.png'), (tubarao[1], tubarao[2]) )
            tubarao[1] -= 9

        default_font_name = pygame.font.get_default_font()
        def_font = pygame.font.Font(default_font_name, 20)
        text = def_font.render(str(state['last_updated']), True, (255, 255, 255))
        window.blit(text,(900, 10))





        
    pygame.display.update()


def atualiza_estado(state):

    # print(pygame.mouse.get_pos())
    pos = pygame.mouse.get_pos()
    valor = pygame.time.get_ticks() - state['inicio']

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_d:
                state["merg_x"] += 20
            if ev.key == pygame.K_w:
                state["merg_y"] -= 20
            if ev.key == pygame.K_a:
                state["merg_x"] -= 20
            if ev.key == pygame.K_s: 
                state["merg_y"] += 20
            if state["merg_y"] > 550:
                state["merg_y"] -= 20
            if state['merg_y'] < 0:
                state["merg_y"] += 20
            if state['merg_x'] > 990:
                state['merg_x'] -= 20
            if state['merg_x'] < 0:
                state['merg_x'] += 20

        if ev.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] >= 336 and pos[0] <= 781 and pos[1] >= 378 and pos[1] <= 470:
                state['merg_x'] = 100
                state['merg_y'] = 300
                state['inicio'] = pygame.time.get_ticks()
                state['t'] = True
                state['tela'] = 0
                pygame.mixer.music.load('som_ambiente.mp3')
                pygame.mixer.music.set_volume(0.2)
                pygame.mixer.music.play(-1)


            if pos[0] >= 445 and pos[0] <= 665 and pos[1] >= 476 and pos[1] <= 540 and state['tela'] != 0:
                return False


    if state['t']:
        state['last_updated'] = valor

    
    
    def colisao_tubarao (personagem, state):
    
        #print(state['tubaroes'])
        for tubarao1 in state['tubaroes']:
            
            tubarao_med = pygame.Rect(tubarao1[1], tubarao1[2] + 20, 30, 40)
            # print( tubarao_med)
            # print(personagem)
            
            if pygame.Rect.colliderect(personagem, tubarao_med):
                state['tubaroes'] = []
                
                
                return True
                
        
        return False
    personagem = pygame.Rect(state['merg_x'], state['merg_y'] + 25, 99, 25)
    #colisao

    if colisao_tubarao(personagem, state ):
        pygame.mixer.music.stop()
        fim = pygame.mixer.Sound('som_fim.mp3')
        pygame.mixer.Sound.play(fim)

        state['tela'] = 1
        state['t'] = False

        pontuaçãofinal = copy.deepcopy(state['last_updated'])
        window.blit(assets['tela_final'], (0,0))
        default_font_name = pygame.font.get_default_font()
        def_font = pygame.font.Font(default_font_name, 40)
        text = def_font.render(str(pontuaçãofinal), True, (255,255,255))
        window.blit(text,(562, 135))


        #pygame.quit()
        #transição de tela:
        pygame.display.update()
        
        
    
    
    
    
    for tubarao in state['tubaroes']:
        if tubarao[1] < -200:
            state['tubaroes'].remove(tubarao)








    return True

def gameloop(window, assets, state):
    while atualiza_estado(state):
        desenha(window, assets, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()