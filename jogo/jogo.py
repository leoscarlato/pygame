import pygame,random


def inicializa():
    pygame.init()
    w = pygame.display.set_mode((1080,600))
    pygame.key.set_repeat(50)

    assets = {
        'player': pygame.image.load('mergulhador.png'),
        'fundo' : pygame.image.load('fundo2.png'),
        'tubarao': pygame.image.load('tubarao_mini.png'),
        'fundo_inicio': pygame.image.load('TELA_INICIAL_JOGO.jpg'),
        'fundo_final': pygame.image.load('TELA_FINAL_JOGO.jpg')
    }

    state = {
        "merg_x" : 0,
        "merg_y" : 0,
        "tub_x" : 600,
        "tub_y" : 0,
        "fundo_inicio2": assets['fundo_inicio'],
        "fundo_final2": assets['fundo_final']
    }


    state['last_updated'] = 0


    return w, assets, state



def finaliza():
    pygame.quit()



def recebe_eventos(state):
    pos = pygame.mouse.get_pos()
    print(pos)
    valor = pygame.time.get_ticks()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RIGHT:
                state["merg_x"] += 12
            if ev.key == pygame.K_UP:
                state["merg_y"] -= 12
            if ev.key == pygame.K_LEFT:
                state["merg_x"] -= 12
            if ev.key == pygame.K_DOWN:
                state["merg_y"] += 12
            if state["merg_y"] > 550:
                state["merg_y"] -= 12
            if state['merg_y'] < 0:
                state["merg_y"] += 12
            if state['merg_x'] > 990:
                state['merg_x'] -= 12
            if state['merg_x'] < 0:
                state['merg_x'] += 12
        if ev.type == pygame.MOUSEBUTTONUP: 
            if pos[0] >= 336 and pos[0] <= 781 and pos[1] >= 378 and pos[1] <= 431:
                assets['fundo_inicio'] == False
                assets['fundo'] == True
                pygame.display.update()
    state['last_updated'] = valor




    return True


def desenha(window, assets, state):
    window.fill((255,255,0))
    window.blit(assets['fundo_inicio'], (0,0))
    window.blit(assets["fundo"], (0,0))
    window.blit(assets["player"], (state["merg_x"],state["merg_y"]))
    window.blit(assets["tubarao"], (state["tub_x"],state["tub_y"]))
    state["tub_x"] -= 10
    if state['tub_x'] == -500:
                state['tub_y'] = random.randint(80,250)
                state['tub_x'] = 920
                state['tub_x'] -= 10
                return False
    pygame.display.update()



def gameloop(window, assets, state):
    while recebe_eventos(state):
        desenha(window, assets, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()