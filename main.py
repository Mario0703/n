import random
import pygame
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
pygame.display.init()
FPS = 30
Window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
food_width, food_height = 30,30
Snake_width,Snake_height = 30,30
food_x,food_y = 100,100

red = (255,255,0)
green = (0,128,0)
snake_x = 50
snake_y = 50
snake_List = []
snake_lenght = 1

class Snake():
    """Snake class that draws the snake on to the screen, controls the lenght of th snake
    and allows thge user to control the snake by the WASD keys"""
    def __init__(self,snake_x,snake_y,snake_width,snake_height):
        self.snake_height = snake_height
        self.snake_width = snake_width
        self.snake_x = snake_x
        self.snake_y = snake_y
        self.Snake_x = 500
        self.Snake_y = 500
        self.snake_speed_x = 0
        self.snake_speed_y = 0
        self.snake_speed = 1
        self.x1 = self.snake_width/2
        self.y1 = self.snake_width/2
        self.snake_List = []
        self.snake_lenght = 1
    def draw_snake(self):
        for snake_coordinate in self.snake_List:
            pygame.draw.rect(Window, red, [snake_coordinate[0], snake_coordinate[1], self.snake_width, self.snake_height])
    def Move_snake(self,keys):
        self.keys = keys
        if self.keys[pygame.K_a]:
            self.snake_speed_x = -self.snake_speed
            self.snake_speed_y = 0
        elif self.keys[pygame.K_d]:
            self.snake_speed_x = self.snake_speed
            self.snake_speed_y = 0
        elif self.keys[pygame.K_w]:
            self.snake_speed_x = 0
            self.snake_speed_y = -self.snake_speed
        elif self.keys[pygame.K_s]:
            self.snake_speed_x = 0
            self.snake_speed_y = self.snake_speed
    def Pop_snake_list(self):
        self.x1 += self.snake_speed_x
        self.y1 += self.snake_speed_y
        self.snake_Head = []
        self.snake_Head.append(self.x1)
        self.snake_Head.append(self.y1)
        self.snake_List.append(self.snake_Head)

        if len(self.snake_List) > self.snake_lenght:
            del self.snake_List[0]
class food():
    """Food class that defines the behavior of food consumed by the snake"""
    def __init__(self,food_x,food_y,food_width,food_height):
        self.food_x = food_x
        self.food_y = food_y
        self.food_width = food_width
        self.food_height = food_height
        self.food_hitbox = pygame.Rect(self.food_x,self.food_y,self.food_width,self.food_height)
    def Draw_food(self):
        pygame.draw.rect(Window,green,self.food_hitbox)
    def Collect_food(self,snake):
        self.snake = snake
        if self.food_hitbox.x == self.snake.x1 and self.food_hitbox.y == self.food_hitbox.y:
            self.food_hitbox.x = random.randint(0,500)
            self.food_hitbox.y = random.randint(0,500)
            self.snake.snake_lenght += 30
        print(self.snake.x1,self.food_hitbox.x)
snake = Snake(snake_x,snake_y, Snake_width,Snake_height)
Frugt = food(food_x,food_y,food_width,food_height)
def Draw_on_to_screen():
    Window.fill((0,0,0))
    snake.draw_snake()
    Frugt.Draw_food()
    pygame.display.update()

def main():
    global x1
    global y1
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        snake.Pop_snake_list()
        keys = pygame.key.get_pressed()
        snake.Move_snake(keys)
        Frugt.Collect_food(snake)
        Draw_on_to_screen()
if __name__ == '__main__':
    main()

