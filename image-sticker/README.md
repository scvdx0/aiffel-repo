### 파일 설명

- [sticker.ipynb](sticker.ipynb)
  - 얼굴 감지를 한 뒤에 고양이 수염 스티커를 붙이는 예제 notebook

- [sticker_webcam.ipynb](sticker_webcam.ipynb)
  - 웹캠을 통해 얼굴에 고양이 수염 스티커를 붙이는 예제
  - 이미지를 바꿔가며 테스트하는 것이 불편하여 웹캠을 통해 여러 각도의 얼굴을 테스트할 수 있도록 하였습니다.

- 이미지 출처: [Kaggle Datasets - Human Faces](https://www.kaggle.com/datasets/ashwingupta3012/human-faces)

### 회고

- 머신러닝 기술을 사용하여 애플리케이션을 만드는 것은 재미있었다.

- 하지만 웹캠을 통해서 다양하게 테스트해보니 여러 문제를 발견 할 수 있었다.
  1. 고개가 회전하면 스티커도 회전해야할 텐데 그렇지 못했다.
    👉 얼굴 랜드마크를 검출하여 고개의 각도를 계산하면 개선 가능할 것 같다.
  2. 얼굴이 보이지만 고개를 앞,뒤,좌,우로 젖히면 얼굴 감지가 되지 않았다.
    👉 각도에 따라 얼굴을 더 잘 인식할 수 있는 모델을 사용하여 개선 가능할 것 같다.
  3. 사진을 찍는 환경이 너무 밝거나 어두운 경우에는 얼굴 감지가 되지 않았다.
    👉 이미지의 밝기를 확인하여 얼굴 감지 시 사용되는 이미지는 밝기 조절을 해야할 것 같다.
  4. 몇몇 이미지는 얼굴 검출이 되지 않았는데 그 기준을 찾기 힘들었다.
    - 주변이 어두워서 검출을 못하는 것 같아 밝이를 높였는데도 얼굴을 검출을 하지 못하였다.
    - 더 다양한 샘플을 사용하여 원인을 찾을 필요가 있을 것 같다.
  5. 반면 사람의 거리는 크게 문제가 되지 않았다. (가까이서도 멀리서도 잘 동작하였다)

### 리뷰

🔑 **PRT(Peer Review Template)**

- [x]  **1. 주어진 문제를 해결하는 완성된 코드가 제출되었나요? (완성도)**
    - 문제에서 요구하는 최종 결과물이 첨부되었는지 확인
    - 문제를 해결하는 완성된 코드란 프로젝트 루브릭 3개 중 2개, 
    퀘스트 문제 요구조건 등을 지칭
        - 해당 조건을 만족하는 부분의 코드 및 결과물을 캡쳐하여 사진으로 첨부


> 다양한 방법을 사용해서 문제를 해결하였습니다.

#### [x] 정면 이미지로 테스트

<img width="249" alt="Screenshot 2024-06-04 at 5 25 00 PM" src="https://github.com/minkj1992/aiffel-repo/assets/37536298/5c31bf43-8528-419e-8981-e3d6743615ec">

#### [x] 단체 이미지로 테스트

<img width="469" alt="Screenshot 2024-06-04 at 5 25 39 PM" src="https://github.com/minkj1992/aiffel-repo/assets/37536298/f0f4a7b7-f46e-423e-bca6-3917090fd7f0">

#### [x] 얼굴 각도 비교
<img width="474" alt="Screenshot 2024-06-04 at 5 25 59 PM" src="https://github.com/minkj1992/aiffel-repo/assets/37536298/f9f7b115-82b5-4d84-b26e-44e8098d41a4">

#### [x] Rotate 비교
<img width="408" alt="Screenshot 2024-06-04 at 5 26 44 PM" src="https://github.com/minkj1992/aiffel-repo/assets/37536298/bde36b08-7dd3-4232-b945-af65cdb432d6">

#### [x] 밝기 조절  비교
<img width="474" alt="Screenshot 2024-06-04 at 5 27 15 PM" src="https://github.com/minkj1992/aiffel-repo/assets/37536298/fdbe9c86-fabb-4727-982e-e538a2f370d3">


- 또한 [webcam](https://github.com/minkj1992/aiffel-repo/blob/main/image-sticker/sticker_webcam.py)을 구현하여 simulation을 하였습니다.

- [x]  **2. 프로젝트에서 핵심적인 부분에 대한 설명이 주석(닥스트링) 및 마크다운 형태로 잘 기록되어있나요? (설명)**
    - [ ]  모델 선정 이유
    - [ ]  Metrics 선정 이유
    - [ ]  Loss 선정 이유

- [x]  **3. 체크리스트에 해당하는 항목들을 모두 수행하였나요? (문제 해결)**
    - [ ]  데이터를 분할하여 프로젝트를 진행했나요? (train, validation, test 데이터로 구분)
    - [ ]  하이퍼파라미터를 변경해가며 여러 시도를 했나요? (learning rate, dropout rate, unit, batch size, epoch 등)
    - [x]  각 실험을 시각화하여 비교하였나요? rotate, 밝기 조절,각도에 따른 비교를 모두 시각화하여 비교하였습니다. (위 첨부)
    - [x]  모든 실험 결과가 기록되었나요? 위와 동일

- [x]  **4. 프로젝트에 대한 회고가 상세히 기록 되어 있나요? (회고, 정리)**
    - [x]  배운 점
    - [x]  아쉬운 점
    - [x]  느낀 점
    - [x]  어려웠던 점
