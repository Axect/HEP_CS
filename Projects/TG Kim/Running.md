<h1 style="text-align:center"> Running Gauge Couplings </h1>

<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

## 0. Process

일단, 현대물리학에 이르러서는 절대적인 상수는 거의 없다는 것을 발견하였습니다. (빛의 속도나 플랑크상수가 거의 유일한 상수값입니다.) Gauge Coupling 상수들 역시 절대적인 상수가 아니라 Energy Scale에 dependent하는 상수입니다. 따라서 Energy를 높여가며 Gauge 상수들을 보는 것이 목표입니다. 이때, 기본 Base Model을 Higgs Inflation 모델로 잡을 것이기에 Mt(Top quark mass)와 xi(Non-minimal coupling constant)가 Free parameter 가 됩니다. Mt의 범위는 대략 170 ~ 172 GeV 정도로 잡고 있고 xi는 0.1 ~ 40000 정도로 추정하고 있습니다. 따라서 Mt와 xi값을 지정하고 에너지를 높여가며 보는 것이 결국 목표입니다. (Mt, xi를 바꿔가며 여러 그래프를 그려보는 것도 좋을 겁니다.)

## 1. Constants

상수들은 첨부한 PBH_CHI(~).html 파일을 보면 init에 나와있으니 참고하면 됩니다. 우주론에서는 기본 Planck mass(Mp)를 사용하지 않고 Reduced Planck mass(MpR)을 사용하니 이에 유의하여 하시면 됩니다.

## 2. Initialize

이제 Running할 Gauge 상수들의 초기값을 줘야 합니다. 일단 Running에 참가하는 상수는 5가지입니다.
$$\lambda, y_t, g_1, g_2, g_3$$
각각의 초기값은 첨부한 draft를 보면 3페이지 정도에 식으로 나와있으니 참고하시길 바랍니다.

## 3. Running

기본적으로 Beta function이 주어졌을때, 게이지 상수는 다음과 같은 식을 얻습니다.
$$\frac{dg_i}{dt} = \frac{\beta_{g_i}(t)}{1+\gamma(t)}$$
이때, $\beta,\, \gamma$는 draft의 마지막에서 두번째 페이지에서 $\frac{1}{16\pi^2}$이 붙어있는 식 - 1-loop - 만 이용하시면 됩니다. (그외의 식에는 오류가 포함되어있으니 사용하지마세요) 따라서 결국 Running의 메커니즘은 t를 조금씩 움직이면서 $g_i$ 들을 바꿔가는 것입니다.

## 4. Graph

결과가 나왔다면 그래프를 예쁘게 그리시면 됩니다. $\lambda$ 같은 경우는 $Mt, \xi$에 민감하기에 $\xi$를 고정하고 $Mt$를 바꿔가며 같이 그려보면 우아한 곡선들이 여러개 나오는 것을 감상할 수 있습니다.

하다가 질문 있으면 언제든 하세요~