"""
#자료구조의 정의

## 자료(Data) 
현실 세계로부터 수집한 사실(= 측정한 값 =measurement)
or 개념의 값(성격-내성적, 외향적 등) 
or 이들의 집합. 
특정 용도로 사용하기 위해 처리 / 가공한 것을 정보(=information = 평균, 분산 등)이라 한다.

## 자료구조의 특징
+ 효율성(Efficiency)
    자료구조를 사용함으로써 무언가 더 좋아지는 게 있어야 한다.

+ 추상화(Abstraction)
    Tree에서 노드를 삭제한다 에는
    노드를 삭제할 때, 그 자식이 있따면 그 자식을 자기 자식으로 swap 해야한다
    를 내포하고 있다.
    이렇게 추상화된 표현으로 사용하는 특징을 추상화라고 한다.
    자료 구조를 사용하면 이렇게 내용이 추상화되기 때문에
    대화를 할 때 더 편하다.

+ 재사용성(Reusability)
    자료구조를 하나 정의하면 
    여기도 쓰일 수 있고, 저기도 쓰일 수 있는 
    범용성을 가져야한다.
    너무 특정한 상황에서만 쓰일 수 있으면 자료구조로 인정받기 어렵다.
    너무 구체적인 상황을 가정하는 것이 아닌,
    조금 효율이 부족해질지라도 재사용성을 높이는 방향으로 간다.

+ 위 세가지의 균형을 잘 맞춰야 좋은 자료구조라고 할 수 있다.

## 자료구조의 종류

+ 선형(Linear)
    여러 갈래로 나누어지지 않는다. = 일자로 되어 있다.
    - 배열 리스트
    - 연결 리스트(배열 리스트의 단점을 보완)
    - 스택
    - 큐
    (스택, 큐는
    연결리스트를 단순화하여 
    효율성을 극대화한
    특별한 자료구조로
    컴퓨터 내부에서 많이 활용한다.)
+ 비선형(NonLinear)
    여러 갈래로 나누어진다. = 일자로 되어 있지 않다. 
    = 선형구조와 반대 = 방향성이 존재한다.
    - 트리
        (= root Node와 child Node 들로 구성)
    - 그래프
        (그래프는 가장 일반적으로 표현하는 자료구조,
        모든 자료의 구조를 표현할 수 있다. 
        = 모든 관계를 표현할 수 있다.
        = 코딩테스트에 항상 나온다.)

## 자료구조의 필요성
프로그램에서는 다양한 자료를 
임시(메모리-RAM) / 영구적(파일 시스템, 데이터베이스)에 
저장하여 사용한다.
= 데이터를 다룬다. 
= 자료구조를 사용한다.

- 만능인 자료구조는 없다. 그래서 여러가지 자료구조를 배우는 것.
  그때 그때 상황에 맞는 좋은 것이 있을 뿐, 항상 좋은 것은 없다.
  각각의 자료구조는 각 상황에서 최적인 것들이다.
- 어떤 자료구조를 선택하는 지에 따라 = 자료를 어떻게 저장하는 지에 따라
  프로그램에 중대한 영향을 끼친다.
  1) 필요한 자료에 효율적으로 빠르게 접근할 수 있게 한다.
  2) 자료의 중복을 최소화하여 저장장치를 효율적으로 사용할 수 있게 한다.
  3) 자료구조 별로 적절한 알고리즘을 기계적으로 사용할 수 있다.
  4) 동료들과 협업하는 데에 큰 도움이 된다.(잘못된 창의성을 발휘하지 않게 도와준다.)

  ## Python과 자료구조
  + Python 에는 대부분의 자료구조가 구현되어 있다.



"""
