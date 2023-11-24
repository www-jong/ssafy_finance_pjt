# **[*FINAL PJT* - 금융 상품 비교 애플리케이션]**

# 💵 <mark>더쓸라 (THESLA)</mark>

> ## 🧭 프로젝트 개요

- 이 프로젝트는 금융 상품 비교를 위한 웹 애플리케이션을 제작한 것입니다.

- 예금 및 적금 금리를 비교하고 데이터 분석을 통해 사용자에게 적합한 금융 상품을 추천할 뿐만 아니라, 그 외에도 사용자의 다른 금융 활동들의 편의를 위한 기능과 정보들을 제공합니다. 

---

> ## 👥 팀 소개

- 원종현
  
  - (역할 쓰기)

- 김민진
  
  - (역할 쓰기)

---

> ## ❗ 더쓸라 로고

(로고 이미지)

---

> ## 🪢 배포 URL

asfsaf

---

> ## 💎 메인 기능

- 예금 및 적금 금리 비교

- 환율 계산기

- 내 집 주변 은행 검색

- 나에게 맞는 상품 추천

- ~~~~완성본 보고 추가



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

- aaaa
  
  - bbb

---

> ## 🖥️ 개발 환경

- **OS**
  
  - Windows (10, 11)

- **IDE**
  
  - Visual Studio Code (1.84.2)

- **Programming Language**
  
  - Python (3.9.13)

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
 
- 나스닥
  - 금 시세 API
  - 은 시세 API

- 코인파프리카
  - 실시간 코인가격 API

---

> ## 📚 데이터 모델링 (ERD)

(ERD 이미지)

---

> ## ✨ 금융 상품 추천 알고리즘에 대한 기술적 설명
### 사용자 기반, 코사인 유사도를 이용한 협업 필터링 추천(Collaborative Filtering)
- 개념
  - 많은 사람들의들의 나이, 소득, 자산 및 금융상품 선호도를 통해 나와 유사한 사람들이 선호하는 금융상품을 추천
- 사용자 기반, 유사도 측정(코사인 유사도)
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mi>s</mi>
  <mi>i</mi>
  <mi>m</mi>
  <mo stretchy="false">(</mo>
  <mi>u</mi>
  <mo>,</mo>
  <msup>
    <mi>u</mi>
    <mo data-mjx-alternate="1">&#x2032;</mo>
  </msup>
  <mo stretchy="false">)</mo>
  <mo>=</mo>
  <mi>c</mi>
  <mi>o</mi>
  <mi>s</mi>
  <mo stretchy="false">(</mo>
  <mi>&#x3B8;</mi>
  <mo stretchy="false">)</mo>
  <mo>=</mo>
  <mfrac>
    <mrow>
      <msub>
        <mi>R</mi>
        <mrow data-mjx-texclass="ORD">
          <mi>u</mi>
        </mrow>
      </msub>
      <mo>&#x22C5;</mo>
      <msub>
        <mi>R</mi>
        <mrow data-mjx-texclass="ORD">
          <msup>
            <mi>u</mi>
            <mo data-mjx-alternate="1">&#x2032;</mo>
          </msup>
        </mrow>
      </msub>
    </mrow>
    <mrow>
      <mrow data-mjx-texclass="INNER">
        <mo data-mjx-texclass="OPEN" symmetric="true">&#x2016;</mo>
        <msub>
          <mi>R</mi>
          <mrow data-mjx-texclass="ORD">
            <mi>u</mi>
          </mrow>
        </msub>
        <mo data-mjx-texclass="CLOSE" symmetric="true">&#x2016;</mo>
      </mrow>
      <mrow data-mjx-texclass="INNER">
        <mo data-mjx-texclass="OPEN" symmetric="true">&#x2016;</mo>
        <msub>
          <mi>R</mi>
          <mrow data-mjx-texclass="ORD">
            <msup>
              <mi>u</mi>
              <mo data-mjx-alternate="1">&#x2032;</mo>
            </msup>
          </mrow>
        </msub>
        <mo data-mjx-texclass="CLOSE" symmetric="true">&#x2016;</mo>
      </mrow>
    </mrow>
  </mfrac>
  <mo>=</mo>
  <mfrac>
    <mrow>
      <munderover>
        <mo data-mjx-texclass="OP">&#x2211;</mo>
        <mrow data-mjx-texclass="ORD">
          <mi>i</mi>
          <mo>=</mo>
          <mn>1</mn>
        </mrow>
        <mrow data-mjx-texclass="ORD">
          <mi>n</mi>
        </mrow>
      </munderover>
      <msub>
        <mi>R</mi>
        <mrow data-mjx-texclass="ORD">
          <mi>u</mi>
          <mi>i</mi>
        </mrow>
      </msub>
      <mo>&#xD7;</mo>
      <msub>
        <mi>R</mi>
        <mrow data-mjx-texclass="ORD">
          <msup>
            <mi>u</mi>
            <mo data-mjx-alternate="1">&#x2032;</mo>
          </msup>
          <mi>i</mi>
        </mrow>
      </msub>
    </mrow>
    <mrow>
      <msqrt>
        <munderover>
          <mo data-mjx-texclass="OP">&#x2211;</mo>
          <mrow data-mjx-texclass="ORD">
            <mi>i</mi>
            <mo>=</mo>
            <mn>1</mn>
          </mrow>
          <mrow data-mjx-texclass="ORD">
            <mi>n</mi>
          </mrow>
        </munderover>
        <mo stretchy="false">(</mo>
        <msub>
          <mi>R</mi>
          <mrow data-mjx-texclass="ORD">
            <mi>u</mi>
            <mi>i</mi>
          </mrow>
        </msub>
        <msup>
          <mo stretchy="false">)</mo>
          <mrow data-mjx-texclass="ORD">
            <mn>2</mn>
          </mrow>
        </msup>
      </msqrt>
      <mo>&#xD7;</mo>
      <msqrt>
        <munderover>
          <mo data-mjx-texclass="OP">&#x2211;</mo>
          <mrow data-mjx-texclass="ORD">
            <mi>i</mi>
            <mo>=</mo>
            <mn>1</mn>
          </mrow>
          <mrow data-mjx-texclass="ORD">
            <mi>n</mi>
          </mrow>
        </munderover>
        <mo stretchy="false">(</mo>
        <msub>
          <mi>R</mi>
          <mrow data-mjx-texclass="ORD">
            <msup>
              <mi>u</mi>
              <mo data-mjx-alternate="1">&#x2032;</mo>
            </msup>
            <mi>i</mi>
          </mrow>
        </msub>
        <msup>
          <mo stretchy="false">)</mo>
          <mrow data-mjx-texclass="ORD">
            <mn>2</mn>
          </mrow>
        </msup>
      </msqrt>
    </mrow>
  </mfrac>
</math>
- 
---

> ## 🍀 프로젝트 후기

- 원종현
  
  - ㅁㄴㅇㄹ

- 김민진
  
  - ㅁㄴㅇㄹ
