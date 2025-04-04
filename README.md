# bullet_dodge_game
탄막 피하기 게임(Only Copilot)

이 코드는 pygame을 사용하여 탄막 피하기 게임을 구현한 것입니다. 주요 구성 요소는 다음과 같습니다:

1. 초기화 및 설정
pygame.init()로 pygame을 초기화합니다.
화면 크기(WIDTH, HEIGHT)를 설정하고, 게임 창을 생성합니다.
색상(흰색, 빨간색, 파란색 등)을 정의합니다.
2. 게임 객체 설정
탄막: bullet_size로 크기를 설정하고, bullet_list에 탄막 정보를 저장합니다. 탄막은 화면 바깥에서 랜덤한 위치에서 생성됩니다.
플레이어: 원형으로 그려지며, 크기는 bullet_size와 동일합니다. 초기 위치는 화면 정중앙입니다.
별: 타이틀 화면에서 배경으로 사용되며, 랜덤한 위치에 생성됩니다.
3. 주요 함수
detect_collision: 플레이어와 탄막 간의 충돌을 감지합니다. 두 원의 중심 간 거리를 계산하여 충돌 여부를 판단합니다.
spawn_bullet: 탄막을 화면 바깥에서 랜덤한 위치에 생성합니다.
move_bullets: 탄막을 이동시키며, 화면 가장자리에 닿으면 반사되도록 처리합니다.
draw_stars 및 move_stars: 타이틀 화면에서 별을 그리거나 이동시켜 우주 배경 효과를 만듭니다.
game_over_screen: 게임 오버 화면을 표시하고, 재시작 또는 종료를 처리합니다.
title_screen: 타이틀 화면을 표시하며, 사용자가 SPACE 키를 누르면 게임이 시작됩니다.
4. 게임 루프
플레이어 이동: 키 입력(LEFT, RIGHT, UP, DOWN)에 따라 플레이어를 이동시키며, 화면 바깥으로 나가지 않도록 제한합니다.
탄막 생성 및 이동: 일정 시간마다 탄막을 생성하고, 이동시킵니다.
충돌 감지: 플레이어와 탄막 간 충돌을 감지하여 게임 오버를 처리합니다.
점수 업데이트: 0.1초마다 점수를 증가시키며, 점수가 100단위일 때 점수 표시가 1초 동안 깜빡입니다.
화면 업데이트: 플레이어, 탄막, 점수 등을 화면에 그린 후, pygame.display.flip()으로 화면을 갱신합니다.
5. 종료 처리
pygame.quit()와 sys.exit()를 호출하여 게임을 종료합니다.
이 코드는 간단한 탄막 피하기 게임을 구현하며, 타이틀 화면, 게임 오버 화면, 점수 표시, 플레이어 이동 및 충돌 감지 등의 기능을 포함하고 있습니다.
