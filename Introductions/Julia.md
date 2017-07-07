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

1. Speed (C=1)

| Test | 포트란 | 줄리아 | 파이썬 | R | 매트랩 | 옥타브 | 매스매티카 | 자바스크립트 | Go | 자바 |
|-----| ----|-----|-----|---|-----|-----|-------|--------|----|---|
||gcc 5.1.1 | 0.4.0 | 3.4.3 | 3.2.2 | R2015b | 4.0.0 | 10.2.0 | V8 3.28.71.19 | go1.5 | 1.8.0_45
| fib | 0.70 | 2.11 | 77.76 | 533.52 | 26.89 | 9324.35 | 118.53 | 3.36 | 1.86 | 1.21 |
| parse_int | 5.05 | 1.45 | 17.02 | 45.73 | 802.52 | 9581.44 | 15.02 | 6.06 | 1.20 | 3.35 |
| quicksort | 1.31 | 1.15 | 32.89 | 264.54 | 4.92 | 1866.01 | 43.23 | 2.70 | 1.29 | 2.60 |
| mandel | 0.81 | 0.79 | 15.32 | 53.16 | 7.58 | 451.81 | 5.13 | 0.66 | 1.11 |  1.35 |
| pi_sum | 1.00 | 1.00 | 21.99 | 9.56 | 1.00 | 299.31 | 1.69 | 1.01 | 1.00 |  1.00 |
| rand_mat_stat | 1.45 | 1.66 | 17.93 | 14.56 | 14.52 | 30.93 | 5.95 | 2.30 | 2.96 |  3.92 |
| rand_mat_mul | 3.48 | 1.02 | 1.14 | 1.57 | 1.12 | 1.12 | 1.30 | 15.07 | 1.42 |  2.36 |


2. Between Python & Matlab
>```Julia
>for animal in ["dog", "cat", "mouse"]
>    println("$animal is a mammal")
>end
>```
>``` Julia
># function to calculate the volume of a sphere
> function sphere_vol(r)
>    # julia allows Unicode names (in UTF-8 encoding)
>    # so either "pi" or the symbol π can be used
>    return 4/3*pi*r^3
>end
>```

3. Best language for Data Science
> <a href="https://www.slant.co/topics/4001/~programming-languages-for-data-science" target="_blank">- What are the best languages for Data Science</a>  

## 3. Advantages

1. Pythonic  
 : Easy to learn & Beautiful Code

2. Dynamic  
 : Need not declare variables. Just use it


## 4. Disadvantages

1. Few Documents & Books  
 : There is only 1 book written by korean

2. No physics library  
 : You should make numerical calculations

3. Interpret (No compile)  
 : You can see errors at run time.

## 5. How to learn Julia?

> <a href="https://juliabyexample.helpmanual.io" target="_blank">- Julia Examples </a>  
> <a href="https://julialang.org/learning/" target="_blank">- Julia Books </a>

## 6. Conclusion

Julia is fast and simple language for Data Science.
It becomes main language in Data Science soon. So, let's challenge!