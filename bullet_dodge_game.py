import pygame
import random
import sys
import math

# 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("탄막 피하기 게임")

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (255, 255, 0)  # 플레이어 색상을 밝은 노란색으로 변경

# 탄막 설정
bullet_size = 10  # 탄막 크기를 절반으로 줄임
bullet_list = []
bullet_speed = 7

# 플레이어 설정
player_size = bullet_size  # 플레이어 크기를 탄막 크기와 동일하게 설정
player_pos = [WIDTH // 2, HEIGHT // 2]  # 플레이어 시작 위치를 정중앙으로 설정
player_speed = 10

# 점수 설정
score = 0
score_font = pygame.font.SysFont("Arial", 30)
score_timer = 0
is_blinking = False  # 점수 깜빡임 상태
last_blink_time = 0  # 마지막 깜빡임 시간

# 탄막 생성 타이머 설정
bullet_spawn_timer = 0
bullet_spawn_interval = 1000  # 1000ms (1초)마다 탄막 생성

# 별 설정
star_list = [[random.randint(0, WIDTH), random.randint(0, HEIGHT)] for _ in range(100)]  # 100개의 별 생성

# 게임 시계
clock = pygame.time.Clock()

# 충돌 감지 함수
def detect_collision(player_pos, bullet_pos):
    px, py = player_pos
    bx, by = bullet_pos
    distance = math.sqrt((px - bx)**2 + (py - by)**2)  # 두 점 사이의 거리 계산
    return distance < (player_size // 2 + bullet_size // 2)  # 반지름의 합보다 거리가 짧으면 충돌

# 탄막 생성 함수
def spawn_bullet():
    angle = random.uniform(0, 2 * math.pi)  # 0에서 360도 사이의 랜덤 각도
    speed_x = math.cos(angle) * bullet_speed
    speed_y = math.sin(angle) * bullet_speed

    # 탄막 시작 위치를 화면 바깥에서 랜덤하게 설정
    edge = random.choice(["top", "bottom", "left", "right"])
    if edge == "top":
        x_pos = random.randint(-bullet_size, WIDTH + bullet_size)
        y_pos = -bullet_size
    elif edge == "bottom":
        x_pos = random.randint(-bullet_size, WIDTH + bullet_size)
        y_pos = HEIGHT + bullet_size
    elif edge == "left":
        x_pos = -bullet_size
        y_pos = random.randint(-bullet_size, HEIGHT + bullet_size)
    elif edge == "right":
        x_pos = WIDTH + bullet_size
        y_pos = random.randint(-bullet_size, HEIGHT + bullet_size)

    bullet_list.append([x_pos, y_pos, speed_x, speed_y])

# 탄막 이동 함수
def move_bullets():
    for bullet in bullet_list:
        bullet[0] += bullet[2]  # x 방향 이동
        bullet[1] += bullet[3]  # y 방향 이동

        # 화면 가장자리에 닿으면 방향 반전 및 위치 조정
        if bullet[0] <= 0:
            bullet[0] = 0  # 화면 내부로 이동
            bullet[2] = -bullet[2]  # x 방향 반전
        elif bullet[0] >= WIDTH - bullet_size:
            bullet[0] = WIDTH - bullet_size  # 화면 내부로 이동
            bullet[2] = -bullet[2]  # x 방향 반전

        if bullet[1] <= 0:
            bullet[1] = 0  # 화면 내부로 이동
            bullet[3] = -bullet[3]  # y 방향 반전
        elif bullet[1] >= HEIGHT - bullet_size:
            bullet[1] = HEIGHT - bullet_size  # 화면 내부로 이동
            bullet[3] = -bullet[3]  # y 방향 반전

# 별 그리기 함수
def draw_stars():
    for star in star_list:
        pygame.draw.circle(screen, WHITE, star, 2)  # 작은 원으로 별을 그림

# 별 이동 함수
def move_stars():
    for star in star_list:
        star[1] += 1  # 별을 아래로 이동
        if star[1] > HEIGHT:  # 화면을 벗어나면 위로 다시 생성
            star[0] = random.randint(0, WIDTH)
            star[1] = 0

# 게임 오버 화면 함수
def game_over_screen():
    screen.fill((0, 0, 0))  # 배경을 검은색으로 설정
    game_over_font = pygame.font.SysFont("Arial", 50)
    game_over_text = game_over_font.render("Game Over", True, WHITE)  # 폰트 색상을 하얀색으로 변경
    score_text = score_font.render(f"Your Score: {score}", True, WHITE)  # 폰트 색상을 하얀색으로 변경
    restart_text = score_font.render("Press SPACE to Restart or ESC to Quit", True, WHITE)  # 폰트 색상을 하얀색으로 변경
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 30))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + 30))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # SPACE 키를 눌러 재시작
                    return True
                if event.key == pygame.K_ESCAPE:  # ESC 키를 눌러 종료
                    pygame.quit()
                    sys.exit()

# 타이틀 화면 함수
def title_screen():
    while True:
        screen.fill((0, 0, 0))  # 배경을 검은색으로 설정
        move_stars()  # 별 이동
        draw_stars()  # 별 그리기
        title_font = pygame.font.SysFont("Arial", 50)
        title_text = title_font.render("Bullet Dodge Game", True, WHITE)  # 폰트 색상을 하얀색으로 변경
        start_text = score_font.render("Press SPACE to Start", True, WHITE)  # 폰트 색상을 하얀색으로 변경
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # SPACE 키를 눌러 시작
                    return

        pygame.time.delay(30)  # 별 이동 속도를 조정

# 게임 루프
title_screen()  # 타이틀 화면 호출

running = True
while running:
    screen.fill((0, 0, 0))  # 배경을 검은색으로 설정
    delta_time = clock.get_time()  # 프레임 간 시간(ms)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 플레이어 이동
    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT] and player_pos[0] > player_size // 2:
        dx -= 1
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size // 2:
        dx += 1
    if keys[pygame.K_UP] and player_pos[1] > player_size // 2:
        dy -= 1
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size // 2:
        dy += 1

    # 대각선 이동 속도 조정
    if dx != 0 or dy != 0:
        length = (dx**2 + dy**2)**0.5
        dx /= length
        dy /= length

    player_pos[0] += dx * player_speed
    player_pos[1] += dy * player_speed

    # 화면 바깥으로 넘어가지 않도록 제한
    player_pos[0] = max(player_size // 2, min(WIDTH - player_size // 2, player_pos[0]))
    player_pos[1] = max(player_size // 2, min(HEIGHT - player_size // 2, player_pos[1]))

    # 탄막 생성 및 이동
    bullet_spawn_timer += delta_time
    if bullet_spawn_timer >= bullet_spawn_interval:  # 일정 시간마다 탄막 생성
        spawn_bullet()
        bullet_spawn_timer = 0
    move_bullets()

    # 충돌 감지
    for bullet in bullet_list:
        if detect_collision(player_pos, bullet[:2]):
            if not game_over_screen():
                running = False
            else:
                # 게임 재시작 초기화
                player_pos = [WIDTH // 2, HEIGHT // 2]  # 정중앙으로 위치 초기화
                bullet_list.clear()
                score = 0
                score_timer = 0
                is_blinking = False
                last_blink_time = 0

    # 점수 업데이트 및 점수 표시
    score_timer += clock.get_time()
    if score_timer >= 100:  # 0.1초마다 점수 증가
        score += 1
        score_timer = 0

        # 점수가 100단위일 때 깜빡임 시작
        if score % 100 == 0:
            is_blinking = True
            last_blink_time = pygame.time.get_ticks()

    # 점수 표시
    if is_blinking:
        current_time = pygame.time.get_ticks()
        if (current_time - last_blink_time) // 200 % 2 == 0:  # 200ms 간격으로 깜빡임
            score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))  # 검은색으로 숨김
        else:
            score_text = score_font.render(f"Score: {score}", True, WHITE)  # 하얀색으로 표시

        # 깜빡임 종료 조건 (1초 동안 깜빡임)
        if current_time - last_blink_time > 1000:
            is_blinking = False
    else:
        score_text = score_font.render(f"Score: {score}", True, WHITE)  # 기본 하얀색 표시

    screen.blit(score_text, (10, 10))

    # 플레이어 그리기
    pygame.draw.circle(screen, BLUE, (int(player_pos[0]), int(player_pos[1])), player_size // 2)

    # 탄막 그리기
    for bullet in bullet_list:
        pygame.draw.circle(screen, RED, (int(bullet[0] + bullet_size // 2), int(bullet[1] + bullet_size // 2)), bullet_size // 2)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
