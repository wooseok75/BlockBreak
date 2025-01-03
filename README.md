# BlockBreak


이 프로젝트는 Pygame 라이브러리를 사용하여 만든 간단한 블럭깨기 게임입니다. 사용자는 패들을 좌우로 움직여 공을 튕기고, 블럭을 부수어 점수를 얻습니다. 게임에서 모든 블럭을 제거하거나, 공이 화면 아래로 떨어지지 않도록 생명을 관리하는 것이 목표입니다.

## 기능
* 공과 패들, 블럭, 아이템의 상호작용
* 블럭 부수기 및 색상 변화
* 아이템 드롭 (새로운 공 추가, 패들 크기 변경 등)
* 점수 및 생명 관리
* 게임 종료 및 클리어 메시지


## 프로젝트 구조
* config.py: 게임의 설정 파일로, 블럭 크기, 화면 크기, 패들 속도 등 다양한 게임 설정을 포함하고 있습니다.
* implements.py: 게임에서 사용하는 주요 객체들(블럭, 패들, 공, 아이템)을 정의한 파일입니다. 각 객체의 이동, 충돌 처리 등을 구현합니다.
* run.py: 게임의 메인 실행 코드로, 게임을 초기화하고 게임 루프를 실행합니다. 화면에 각 객체를 그려주고, 사용자 입력을 처리합니다.


## 사용법
* 게임 시작: SPACE 키를 눌러 게임을 시작합니다.
* 패들 조작: 왼쪽, 오른쪽 화살표 키를 눌러 패들을 좌우로 이동시킵니다.
* 게임 종료: ESC 키를 눌러 게임을 종료할 수 있습니다.
* 게임 목표: 공을 튕겨서 블럭을 모두 부수고, 점수를 얻으세요. 생명이 다하면 게임 오버가 됩니다.


## 주요 게임 동작
* 블럭: 블럭은 여러 색상으로 설정되어 있으며, 공과 충돌할 때 색상이 변경됩니다. 색상이 모두 변경되면 블럭이 사라집니다.
* 아이템: 일부 블럭을 부술 때, 20% 확률로 아이템이 떨어집니다. 아이템은 패들과 충돌 시 효과를 발동합니다. 예를 들어, 새로운 공을 추가하거나 패들의 크기를 늘리는 등의 효과가 있습니다.
* 공: 공은 패들과 충돌하며 반사됩니다. 벽에 부딪힐 때도 반사되며, 화면 아래로 떨어지면 생명이 차감됩니다.


## 게임 종료 및 승리
* 게임 오버: 공이 화면 아래로 떨어지면 생명이 차감되며, 생명이 0이 되면 게임 오버 메시지가 표시됩니다.
* 게임 클리어: 모든 블럭을 부수면 "Cleared!" 메시지가 표시됩니다.


## 라이센스
이 프로젝트는 MIT 라이센스 하에 배포됩니다. 더 자세한 내용은 LICENSE 파일을 참고해주세요.

## 개발자 주소
wseok1824@naver.com

![ABC](https://github.com/user-attachments/assets/76bfd153-756b-4d80-b18c-916d1ac9d156)
