# **[*FINAL PJT* - 금융 상품 비교 애플리케이션]**

# 💵 <mark>더쓸라 (THESLA)</mark>

> ## 🧭 프로젝트 개요

- 이 프로젝트는 금융 상품 비교를 위한 웹 애플리케이션을 제작한 것입니다.

- 예금 및 적금 금리를 비교하고 데이터 분석을 통해 사용자에게 적합한 금융 상품을 추천할 뿐만 아니라, 그 외에도 사용자의 다른 금융 활동들의 편의를 위한 기능과 정보들을 제공합니다. 

---

> ## 👥 팀 소개

- 원종현
  
  - 백엔드(Django), 프론트엔드(Vue)

- 김민진
  
  - 프론트엔드(Vue), PPT 및 문서 작업

---

> ## ❗ 더쓸라 로고

![logo](https://github.com/www-jong/SSAFY-finance-pjt/assets/88592432/7c8c8f80-6558-43a7-a010-e88e39f9d6fd)

---

> ## 💎 메인 기능

- 예금 및 적금 금리 비교

- 환율 계산기

- 내 집 주변 은행 검색

- 나에게 맞는 상품 추천

---

> ## ✅ 프로젝트 요구 사항

- 메인 페이지
  
  - 서비스 소개 및 메인 페이지 구성

- 회원 커스터마이징
  
  - 회원 관리 기능 구성 (회원 가입, 로그인, 로그아웃 등)

- 예적금 금리 비교
  
  - 데이터 저장
    
    - 적절한 API를 활용하여 금융 상품 데이터를 DB에 저장
  
  - 전체 조회
    
    - 상품 목록을 조회할 수 있는 화면 구성
    
    - 은행을 선택하여 목록을 필터링할 수 있도록 추가 기능 구성
  
  - 상세 조회
    
    - 해당 금융 상품에 대한 자세한 정보를 출력할 수 있는 화면 구성
    
    - 관리자는 금리 정보를 수정할 수 있도록 구현
    
    - 상품의 금리 정보가 수정되면 가입한 유저의 이메일로 메일이 전송되도록 구현

- 환율 계산기
  
  - 적절한 API를 활용하여 현재 환율에 대한 정보 가져오기
  
  - 국가를 선택할 수 있도록 구성
  
  - 원화 입력 시, 선택한 국가의 통화로 변환된 값을 출력
  
  - 타국 통화 입력 시, 해당 통화를 원화로 변환한 값을 출력

- 근처 은행 검색
  
  - 적절한 API를 활용하여 지도를 표시
  
  - 위치와 은행을 선택할 수 있도록 구성

- 커뮤니티 (게시판)
  
  - 회원 간 소통할 수 있는 커뮤니티 기능(게시판)을 구현
  
  - 게시글 조회, 생성, 삭제, 수정 구현
  
  - 댓글 생성, 삭제 기능 구현
  
  - 회원의 권한에 따라 다른 동작을 하도록 구성

- 프로필 페이지
  
  - 회원의 기본 정보를 출력할 수 있도록 적절한 화면 구성
  
  - 회원의 정보를 수정하기 위한 적절한 화면 구성
  
  - 내가 가입한 금융 상품 리스트를 출력하는 화면 구성
  
  - 차트 라이브러리를 활용하여 가입한 상품 금리 정보를 그래프로 출력

- 금융 상품 추천 알고리즘
  
  - 사용자에게 적합한 금융 상품을 추천할 수 있는 알고리즘 구현

---

> ## 🔥 더쓸라의 추가 구현 기능

- 메인 페이지
  
  - 네이버 뉴스 검색 API를 통해 '오늘의 금융 뉴스' 화면 추가
  - 오늘의 운세 추가
  - 비트코인, 금, 은 시세 정보 추가
  - "작은 이스터에그가 있으니 찾아보세요!"

- 회원 커스터마이징
  
  - 프로필 편집 및 프로필 이미지 수정 기능

---

> ## 🖥️ 개발 환경

- **OS**
  
  - Windows (10, 11)

- **IDE**
  
  - Visual Studio Code (1.84.2)

- **Programming Language**
  
  - Python (3.9.13)
  - JavaScript (ES6+)

- **Front-end Framework**
  
  - Tailwind CSS (3.3.2)
  
  - Vue.js (3.3.4)

- **Back-end Framework**
  
  - Django (4.2.4)

- **Library**
  
  - Node.js (20.9.0)
  
  - Django REST framework (3.14.0)

- **DBMS**
  
  - SQLite (3.44.0)

---

> ## 📑 API

- 금융감독원 금융상품통합비교공시
  
  - 정기예금상품 API, 적금상품 API

- 한국수출입은행
  
  - 현재환율 API

- 카카오
  
  - 지도 API

- 네이버
  
  - 뉴스 검색 API

---

> ## 🏗️ 개체-관계 다이어그램 (ERD)

![이미지](https://github.com/www-jong/SSAFY-finance-pjt/assets/88592432/0ce14783-4848-42a6-b03c-ec1391844f6d)

---

> ## 📚 컴포넌트 다이어그램
![컴포넌트](https://github.com/www-jong/SSAFY-finance-pjt/assets/88592432/8c2c8e24-244a-4ab2-b32d-b9f1d528f194)

---

> ## ✨ 금융 상품 추천 알고리즘에 대한 기술적 설명

- 개념
  
  ![](https://github.com/www-jong/SSAFY-finance-pjt/assets/88592432/23b38572-8564-4f4b-b9cb-69fa2ffba2ba)
  
  - 많은 사람들의 나이, 소득, 자산 및 금융 상품 선호도를 통해 나와 유사한 사람들이 선호하는 금융 상품을 추천
  
  - 유사도의 초점에 따라 사용자 혹은 아이템 기반 측정 가능

- 사용자 기반 유사도 측정(코사인 유사도)
  
  ![](https://github.com/www-jong/SSAFY-finance-pjt/assets/88592432/8f828561-26d1-4782-ab2d-a8b6d96a6a4f)
  
  - 두 벡터의 코사인 각도를 계산해 유사성 측정
  
  - 즉, 구하고자 하는 사람의 금융 상품 선호도(추천)과 사람들을 1:1로 코사인 유사도를 구해 금융 상품 선호도 우선순위 설정

- 사용한 유저 데이터
  
  - 3만 명의 랜덤한 유저 더미 데이터를 이용
  
  - 더미 데이터는 20 ~ 80세의 랜덤한 나이, 0 ~ 1000만 원 사이의 랜덤한 월 소득, 0~10억 원 사이의 랜덤한 자산, 은행권 예금 상품중 랜덤한 1개 상품으로 구성

---

> ## 🍀 프로젝트 후기

- 원종현
  
  - SSAFY에서 처음 진행한 팀 프로젝트이며, 1학기의 마무리를 알리는 관통 프로젝트였습니다. 약 일주일의 길지도 않고 짧지도 않은 시간이었지만 지금까지 배워왔던 기술들을 한번씩 다 활용해볼 수 있는 좋은 기회였고, 부족한 팀 프로젝트 경험을 쌓을 수 있는 기회였습니다. 그리고 또 한 번, 기획의 중요성을 깨닫게 되는 프로젝트였습니다. 여러 어려움이 많았고, 답답함도 많았지만 이리저리 부딪히면서 최대한 구현해낼 수 있을만큼 구현을 해서 조금은 후련합니다. 그리고 뭐니뭐니 해도 디자인이 가장 어렵다는 것을 깨달았습니다. 기술 스택말고도, 디자인 스택(?)도 소홀히 하지 않아야겠습니다. 일주일 동안 같이 고생한 페어 민진이 형 정말 고생하셨습니다!

- 김민진
  
  - 기존에 프로젝트 경험이 여러 번 있던 종현이와 달리, 처음으로 프로젝트를 진행해보았습니다. 프로젝트 진행에 짐이 되지 않을까하는 걱정도 많이 했지만, 종현이가 이전의 프로젝트 경험들을 살려 리드를 잘해준 덕분에 마무리를 잘할 수 있었습니다. 첫 프로젝트인만큼 프로젝트의 전반적인 흐름을 배울 수 있는 경험이 된 것 같아 많은 것을 얻은 프로젝트였고, 특히 프로젝트 진행을 하며 종현이의 실력도 실력이지만 '개발에 대한 열정'을 보고 한 명의 SSAFY 교육생으로서 많은 귀감을 얻게 되었습니다. 프로젝트 기간 동안 함께 고생한 종현이에게 고생 많았다는 말을 전하고 싶습니다.
