# train-notebook

훈련 및 예측을 위한 리포지토리입니다. 모델 훈련은 [scratch.ipynb](scratch.ipynb)를 참고하시기 바랍니다. 예측은 아래 Getting started 에서 설명하고 있습니다.

## Getting started

1. 파이썬 가상환경 실행

2. 파이썬 패키지 설치

```s
$ pip install requirements.txt
```

3. 최상단 디렉토리에 분석하고자 하는 `text.txt` 를 놓기

```
I haven't tried it yet, but I'm saying the sales volume isn't it?
This Ottogi was launching Bibimmyeon to reduce the summer seasonality.
Fortunately, the market trend is... Flare is Nongshim Ottogi Samyang food.
```

4. `predict.py` 실행하기

```s
$ python3 predict.py
```

5. 결과는 `result.txt` 로 저장되며 왼쪽부터 `label`, `score`, `text`

```
1,0.9999964237213135,I haven't tried it yet, but I'm saying the sales volume isn't it?
2,0.9999943971633911,This Ottogi was launching Bibimmyeon to reduce the summer seasonality.
2,0.999994158744812,Fortunately, the market trend is... Flare is Nongshim Ottogi Samyang food.
```
