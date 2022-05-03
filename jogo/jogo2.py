import pygame,random

def inicializa():
    pygame.init()
    w = pygame.display.set_mode((1080,600))
    pygame.key.set_repeat(50)

    state = {
        "merg_x" : 0,
        "merg_y" : 0,
        "tub_x" : 600,
        "tub_y" : 0
    }

    assets = {
        'player': pygame.image.load('mergulhador.png'),
        'fundo' : pygame.image.load('fundo2.png'),
        'tubarao': pygame.image.load('tubarao_mini.png'),
        'fundo_inicio': pygame.image.load('TELA_INICIAL_JOGO.jpg'),
        'fundo_final': pygame.image.load('TELA_FINAL_JOGO.jpg')
    }

    state['last_updated'] = 0


    return w, assets, state


def desenha(state, assets, window):
    window.blit(state['fundo_inicio'], (0,0))
    
 


def recebe_eventos(state):
    pass


def finaliza():
    pygame.quit()

def gameloop(window,assets,state):
    pass


if __name__ == '__main__':
    window, assets, state = inicializa()
    gameloop(window, assets, state)
    finaliza()