import sys #Para usar exit
import pygame
import time

width, height = 640, 480
background_color = (0,64,0) #Color RGB
font_color = (255,255,255)

#Elementos principales
class Scene:
    def __init__(self):
        "Inicilizando"
        self.nextScene = False
        self.playing = False
        self.menu = True
    
    def read_events(self, event):
        "Lectura de los eventos"
        pass
    
    def update(self):
        "Calculos y lógica"
        pass
    
    def draw(self, screen):
        "Dibuja los objetos en pantalla"
        pass

    def change_scene(self, scene):
        "Selecciona la nueva escena"
        self.nextScene = scene

class Director:
    def __init__(self,title="",res = (width, height)):
        pygame.init()
        #Inicializamos pantalla
        self.screen = pygame.display.set_mode(res)
        #Título de pantalla
        pygame.display.set_caption(title)
        #Creamos reloj
        self.clock = pygame.time.Clock()
        self.scene = None
        self.scenes = {}
     
    def execute(self, init_scene, fps = 60):
        self.scene = self.scenes[init_scene]
        playing = True

        while playing:
            self.clock.tick(fps)
            events = pygame.event.get()
            #Revisar eventos
            for event in events:
                if event.type == pygame.QUIT: #Presionames X en la venta
                    playing = False  #Se cierra el juego
            self.scene.read_events(events)
            self.scene.update()
            self.scene.draw(self.screen)
            self.choose_scene(self.scene.nextScene)

            if playing:
                playing = self.scene.playing
            
            pygame.display.flip()

        time.sleep(3)

    def choose_scene(self, nextScene):
        if nextScene:
            if nextScene not in self.scenes:
                self.addScene(nextScene)
            self.scene = self.scenes[nextScene]
    
    def addScene(self, scene):
        sceneClass = 'Scene'+scene
        sceneObject = globals()[sceneClass]
        self.scenes[scene] = sceneObject()

#Generación de escenas
class SceneLevel1(Scene):
    def __init__(self):
        Scene.__init__(self)

        self.balon = Ball()
        self.plataforma = Platform()
        self.muro = Wall(100)
        
        self.puntuacion = 0
        self.vidas = 3
        self.sacar = False

        #Repetición de evento
        pygame.key.set_repeat(30) #Restraso en milisegundos
    
    def read_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.plataforma.update(event)
                if self.sacar == False and event.key == pygame.K_SPACE:
                    self.sacar = True
                    if self.balon.rect.centerx < width/2:
                        self.balon.speed = [3,-3]
                    else:
                        self.balon.speed = [-3,-3]
    
    def update(self):
    #Actualizamos la posición del balón
        if self.sacar == True:
            self.balon.update()
        else:
            self.balon.rect.midbottom = self.plataforma.rect.midtop

        #Colisiones
        if pygame.sprite.collide_rect(self.balon,self.plataforma): #balon vs plataforma
            self.balon.speed[1] = -self.balon.speed[-1]

        list = pygame.sprite.spritecollide(self.balon,self.muro,False)
        if list:
            ladrillo = list[0]
            cx_balon = self.balon.rect.centerx

            if cx_balon <= ladrillo.rect.left or cx_balon > ladrillo.rect.right:
                self.balon.speed[0] = -self.balon.speed[0]
            else:
                self.balon.speed[1] = -self.balon.speed[1]
            self.muro.remove(ladrillo)
            self.puntuacion += 1

        #El balon sale de la pantalla
        if self.balon.rect.top > height:
            self.vidas -= 1
            self.sacar = False
        
        #Terminar juego
        if self.vidas <= 0:
            self.change_scene('EndGame')

    def draw(self,screen):
        #Rellenamos pantala
        screen.fill(background_color)
        #Mostrar puntuacion
        self.Score(screen)
        #Mostar vida
        self.Health(screen)
        #dibujar objeto
        screen.blit(self.balon.image, self.balon.rect) #Balon
        screen.blit(self.plataforma.image, self.plataforma.rect) #Plataforma
        self.muro.draw(screen)

    def Health(self, screen):
        font = pygame.font.SysFont('Consolas',20)
        self.health = "Vidas: " + str(self.vidas).zfill(2)
        text = font.render(self.health,True,font_color)
        text_rect = text.get_rect()
        text_rect.topright = [width,0]
        screen.blit(text,text_rect)
        
    def Score(self, screen):
        font = pygame.font.SysFont('Consolas',20)
        self.score = "Score: "+ str(self.puntuacion).zfill(3)
        text = font.render(self.score,True,font_color)
        text_rect = text.get_rect()
        text_rect.topleft = [0,0]
        screen.blit(text,text_rect)

class SceneEndGame(Scene):
    def update(self):
        self.playing = False
    
    def draw(self, screen):
        font = pygame.font.SysFont('Arial',72)
        text = font.render('END GAME',True,font_color)
        text_rect = text.get_rect()
        text_rect.center = [width / 2, height / 2]
        screen.blit(text,text_rect)



    
#Creación de objetos
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #garcar imagen
        self.image=pygame.image.load('images/balon.png')
        self.rect = self.image.get_rect()
        #configurar posicion inical
        self.rect.centerx = width / 2
        self.rect.centery = height / 2 
        #configuramos velocidad inicial
        self.speed = [3,3]
    
    def update(self):
        #Evitamos que salga el objeto
        if self.rect.top <= 0: #Por debajo o arriba
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= width or self.rect.left <= 0: #Por derecha o izquierda 
            self.speed[0] = -self.speed[0]

        #Movemos en base a la posición actual y la velocidad
        self.rect.move_ip(self.speed)
    
class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #garcar imagen
        self.image=pygame.image.load('images/plataforma.png')
        self.rect = self.image.get_rect()
        #configurar posicion inical
        self.rect.midbottom = (width/2, height - 20)
        #configuramos velocidad inicial
        self.speed = [0,0]
    
    def update(self, event):
        if event.key == pygame.K_LEFT and self.rect.left > 0:      #Presionas flecha izquiera
            self.speed = [-8,0]
        elif event.key == pygame.K_RIGHT and self.rect.right < width:   #Presionar flecha derecha
            self.speed = [8,0]
        else:                               #No presionamos              
            self.speed= [0,0]
        #Movemos en base a la posición actual y la velocidad
        self.rect.move_ip(self.speed)

class Brick(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        #garcar imagen
        self.image=pygame.image.load('images/muro.png')
        self.rect = self.image.get_rect()
        #configurar posicion inical
        self.rect.topleft = position

class Wall(pygame.sprite.Group):
    def __init__(self, cantBrick):
        pygame.sprite.Group.__init__(self)

        pos_x,pos_y = 0,20 
        for i in range(cantBrick):
            ladrillo = Brick((pos_x,pos_y))
            self.add(ladrillo)
            pos_x +=ladrillo.rect.width
            
            if pos_x > width:
                pos_x = 0
                pos_y += ladrillo.rect.height

director = Director('Primer Juego',(width, height))
director.addScene('Level1')
director.execute('Level1')