import pygame,random
print()

def inicializa():
    pygame.init()
    w = pygame.display.set_mode((1080,600))
    pygame.key.set_repeat(50)

    state = {
        "merg_x" : 0,
        "merg_y" : 0,
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
    print(assets['player'].get_size())
    


    return w, assets, state




    



def finaliza():
    pygame.quit()


def desenha(window, assets, state):
    if state['tela'] == 2:
        window.blit(assets['tela_inicial'], (0,0))
    if state['tela'] == 0:
        window.blit(assets["fundo"], (0,0))
        window.blit(assets["player"], (state["merg_x"],state["merg_y"]))
        if state['last_updated'] % 50 == 0:
            state['tubaroes'].append([assets['tubarao'], 920, random.randint(10, 500)])
        
        for tubarao in state['tubaroes']:
            window.blit(pygame.image.load('tubarao.png'), (tubarao[1], tubarao[2]) )
            tubarao[1] -= 7

        
    pygame.display.update()


def atualiza_estado(state):
    print(pygame.mouse.get_pos())
    pos = pygame.mouse.get_pos()
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
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if pos[0] >= 336 and pos[0] <= 781 and pos[1] >= 378 and pos[1] <= 431:
                state['tela'] = 0


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

    
    
    def colisao_tubarao (personagem, state):
    
        #print(state['tubaroes'])
        for tubarao1 in state['tubaroes']:
            
            tubarao_med = pygame.Rect(tubarao1[1], tubarao1[2] + 20, 30, 40)
            # print( tubarao_med)
            # print(personagem)
            
            if pygame.Rect.colliderect(personagem, tubarao_med):
                
                
                
                return True
                
        
        return False
    personagem = pygame.Rect(state['merg_x'], state['merg_y'] + 25, 99, 25)
    #colisao

    if colisao_tubarao(personagem, state ):
        state['tela'] = 1
        window.blit(assets['tela_final'], (0,0))
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