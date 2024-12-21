import math
import random
import time

import config

import pygame
from pygame.locals import Rect, K_LEFT, K_RIGHT


class Basic:
    def __init__(self, color: tuple, speed: int = 0, pos: tuple = (0, 0), size: tuple = (0, 0)):
        self.color = color
        self.rect = Rect(pos[0], pos[1], size[0], size[1])
        self.center = (self.rect.centerx, self.rect.centery)
        self.speed = speed
        self.start_time = time.time()
        self.dir = 270

    def move(self):
        dx = math.cos(math.radians(self.dir)) * self.speed
        dy = -math.sin(math.radians(self.dir)) * self.speed
        self.rect.move_ip(dx, dy)
        self.center = (self.rect.centerx, self.rect.centery)


class Block(Basic):
    def __init__(self, color: tuple, pos: tuple = (0,0), alive = True):
        super().__init__(color, 0, pos, config.block_size)
        self.pos = pos
        self.alive = alive
        self.hit_count = 0  # 블록이 부딪힌 횟수

    def draw(self, surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)
    
    def collide(self):
        """블록이 공에 부딪혔을 때 색상 변경 및 블록 상태 갱신"""
        if self.color == (169, 169, 169):  # 회색 블록
            self.color = (255, 0, 0)  # 빨간색으로 변경
        elif self.color == (255, 0, 0): # 빨간색 블록
            self.color = (255, 165, 0)  # 주황색 블록으로 변경
        elif self.color == (255, 165, 0):  # 주황색 블록
            self.color = (255, 255, 0)  # 노란색으로 변경
        elif self.color == (255, 255, 0):  # 노란색 블록
            self.alive = False  # 노란색에서 부딪히면 사라짐

class Paddle(Basic):
    def __init__(self):
        super().__init__(config.paddle_color, 0, config.paddle_pos, config.paddle_size)
        self.start_pos = config.paddle_pos
        self.speed = config.paddle_speed
        self.cur_size = config.paddle_size

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move_paddle(self, event: pygame.event.Event):
        if event.key == K_LEFT and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        elif event.key == K_RIGHT and self.rect.right < config.display_dimension[0]:
            self.rect.move_ip(self.speed, 0)


class Ball(Basic):
    def __init__(self, pos: tuple = config.ball_pos):
        super().__init__(config.ball_color, config.ball_speed, pos, config.ball_size)
        self.power = 1
        self.life = 3
        self.dir = 90 + random.randint(0, 45)

    def reflect(self, block):
        if self.rect.top < block.rect.bottom and self.rect.bottom > block.rect.top:
            if self.rect.left < block.rect.right and self.rect.right > block.rect.left:
                self.dir = 180 - self.dir + random.randint(-5, 5)  # 수평 반사
        if self.rect.left < block.rect.right and self.rect.right > block.rect.left:
            if self.rect.top < block.rect.bottom and self.rect.bottom > block.rect.top:
                self.dir = 360 - self.dir + random.randint(-5, 5)  # 수직 반사
                
    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)

    def collide_block(self, blocks: list):   
        for block in blocks:
            if self.rect.colliderect(block.rect):  # 공과 블록의 충돌 확인
                block.collide()  # 충돌 시 블록 상태 변경
                self.reflect(block)  # 공 반사
                if not block.alive:  # 블록이 사라지면 리스트에서 제거
                    blocks.remove(block)
                    # 아이템 떨어뜨리기
                    self.drop_item(block)

                break

    def collide_paddle(self, paddle: Paddle) -> None:
        if self.rect.colliderect(paddle.rect):
            self.dir = 360 - self.dir + random.randint(-10, 10)

    def hit_wall(self):
        if self.rect.left <= 0:     # 좌측 벽 충돌
            self.rect.left = 0
            self.dir = 180 - self.dir + random.randint(-10, 10)

        if self.rect.right >= 600:      # 우측 벽 충돌
            self.rect.right = 600
            self.dir = 180 - self.dir + random.randint(-10, 10)  

        if self.rect.top <= 0:      # 상단 벽 충돌
            self.dir = 360 - self.dir + random.randint(-10, 10)  
        pass
    
    def alive(self): 
        if self.rect.bottom >= 800:  
            if self.life > 1:
                self.life -= 1  
                ball_pos = (300, 385)
                return True  
            else:
                return False  
        return True  
        pass

    def drop_item(self, block: Block):
        """블록을 부술 때 20% 확률로 빨간 공 또는 파란 공 아이템을 떨어뜨리기"""
        if random.random() < 0.2:  # 20% 확률로 아이템 떨어짐
            item_color = random.choice([(255, 0, 0), (0, 0, 255)])  # 빨간 공 (255, 0, 0) 또는 파란 공 (0, 0, 255)
            item = Item(item_color, (block.rect.centerx, block.rect.centery))
            config.ITEMS.append(item)  # 아이템을 config.ITEMS에 추가

class Item(Basic):
    def __init__(self, color: tuple, pos: tuple = (0, 0)):
        # 아이템 클래스, 공이 떨어지는 효과를 구현
        super().__init__(color, 0, pos, config.item_size)

    def draw(self, surface):
        # 아이템을 화면에 그리기
        pygame.draw.ellipse(surface, self.color, self.rect)

    def move(self):
        # 아이템이 아래로 떨어지게
        self.rect.move_ip(0, 5)

    def collision_with_paddle(self, paddle: Paddle):
        """아이템이 paddle에 닿았을 때 처리하는 함수"""
        if self.rect.colliderect(paddle.rect):
            if self.color == (255, 0, 0):  # 빨간 공 아이템
                # 새로운 공을 발사
                new_ball = Ball((paddle.rect.centerx, paddle.rect.top - 20))  # paddle 위에서 새로운 공을 발사
                config.BALLS.append(new_ball)  # BALLS 리스트에 새로운 공 추가
            config.ITEMS.remove(self)  # 아이템이 먹혔으므로 삭제
