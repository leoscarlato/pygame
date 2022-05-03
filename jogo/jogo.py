import pygame,random


def inicializa():
    pygame.init()
    w = pygame.display.set_mode((1080,600))
    pygame.key.set_repeat(50)

    state = {
        "merg_x" : 0,
        "merg_y" : 0,
        "tub_x" : 600,
        "tub_y" : random.randint(100,550)
    }

    assets = {
        'player': pygame.image.load('mergulhador.png'),
        'fundo' : pygame.image.load('fundo2.png'),
        'tubarao': pygame.image.load('tubarao_mini.png')
    }

    state['last_updated'] = 0


    return w, assets, state



def finaliza():
    pygame.quit()


def desenha(window, assets, state):
    window.fill((255,255,0))
    window.blit(assets["fundo"], (0,0))
    window.blit(assets["player"], (state["merg_x"],state["merg_y"]))
    print(state['last_updated'])
    if state['last_updated'] % 1 == 0:
        window.blit(assets["tubarao"], (state["tub_x"],state["tub_y"]))
        state["tub_x"] -= 5
    pygame.display.update()


def recebe_eventos(state):
    valor = pygame.time.get_ticks()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RIGHT:
                state["merg_x"] += 20
            if ev.key == pygame.K_UP:
                state["merg_y"] -= 20
            if ev.key == pygame.K_LEFT:
                state["merg_x"] -= 20
            if ev.key == pygame.K_DOWN:
                state["merg_y"] += 20
            if state["merg_y"] > 550:
                state["merg_y"] -= 20
            if state['merg_y'] < 0:
                state["merg_y"] += 20
            if state['merg_x'] > 990:
                state['merg_x'] -= 20
            if state['merg_x'] < 0:
                state['merg_x'] += 20
    state['last_updated'] = valor

        # state['merg_x'] = (pygame.mouse.get_pos()[0] - 40)
        # state['merg_y'] = (pygame.mouse.get_pos()[1] - 20)
        # if state["merg_y"] > 410:
        #         state["merg_y"] -= 20
        # if state['merg_y'] < 20:
        #         state["merg_y"] += 20
        # if state['merg_x'] > 550:
        #         state['merg_x'] -= 20
        # if state['merg_x'] < 0:
        #         state['merg_x'] += 20



    return True

def gameloop(window, assets, state):
    while recebe_eventos(state):
        desenha(window, assets, state)


if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()