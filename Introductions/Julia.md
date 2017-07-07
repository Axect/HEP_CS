<h1 style="text-align:center">Julia</h1>
<p style="text-align:right">Provided by <b>Tae Geun Kim</b></p>

## 1. What is Julia?
> 프로그래밍 언어의 일종. MIT에서 개발한 언어이다. 동적 프로그래밍 언어로, 주로 과학, 공학 분야에서 빠른 계산 성능을 내기 위해 개발되었다. 2012년에 처음 발표된 신생 언어이다. 병렬 컴퓨팅을 지원할 뿐만 아니라 이것으로 작성한 코드의 실행 속도는 C보다는 약간 느리지만 Python이나 MATLAB보다 훨씬 빠르다. 
>
> -출처: 나무위키

* 핵심 언어는 최소한으로 꾸린다; 정수를 다루는 프리미티브 연산자(+ – * 같은)를 비롯해 기본 라이브러리는 줄리아 자체로 작성됐다.
* 객체를 구성하고 서술하는 데 쓸 타입을 언어에서 풍부히 지원하며, 타입 선언을 할 때도 선택적으로 사용할 수 있다.
* 인자 타입을 조합함으로써 함수의 작동 행위를 정의하는 ‘멀티플 디스패치’
* 인자 타입에 따라 효율적이고 특화된 코드를 자동으로 생성한다.
* C처럼 정적으로 컴파일되는 언어에 근접하는 훌륭한 성능
* 사용자가 정의한 타입 또한 내장한 타입처럼 빠르고 간결하다.
* 성능을 위해 코드를 벡터화할 필요가 없다; 벡터화하지 않은 코드도 빠르다.
* 병렬과 분산 처리를 위해 고안됐다.
* 가벼운 그린 쓰레딩(코루틴)
* 리스프와 비슷한 매크로, 메타프로그래밍을 위한 장치들
* (이하 하략)
* (출처 : 줄리아 소개글 by 깃허브 줄리아 한국 커뮤니티)

> * 줄리아 이름은 어떻게 지은건가?  
    : 많이 듣는 질문인데, 이유는 정말 없다. 그냥 줄리아 이름이 귀여웠다.

## 2. Why do we use Julia?

1. Speed
<img src="https://cdn.namuwikiusercontent.com/a5/a5804a3c94f7bc5cd974ecfb965bd7d851e8d94db84dba21b760179668b56d9b.png?e=1507190584&k=KetO2_I5al-aL7RrM2mFzQ" align="center">

2. Between Python & Matlab
>```Julia
>for animal in ["dog", "cat", "mouse"]
>    println("$animal is a mammal")
>end
>```