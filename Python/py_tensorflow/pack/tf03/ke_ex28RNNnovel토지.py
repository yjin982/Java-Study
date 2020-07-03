# 기존 소설을 읽어 학습한 후 새로운 글을 작성하기
# 주의 : 아래 실습은 시스템의 성능이 우수해야 함.
import numpy as np
import random, sys
import tensorflow as tf

#from google.colab import files
#files.upload()
f = open("rnn_test_toji.txt", 'r', encoding="utf-8")
text = f.read()
#print(text)
f.close();

print('텍스트 행 수: ', len(text))  # 306967
print(set(text))  # set 집합형 함수를 이용해 중복 제거{'얻', '턴', '옮', '쩐', '제', '평',...
chars = sorted(list(set(text)))     # 중복이 제거된 문자를 하나하나 읽어 들여 정렬 
print(chars)                        # ['\n', ' ', '!', ... , '0', '1', ... 'a', 'c', 'f', '...
print('사용되고 있는 문자 수:', len(chars))   # 1469

char_indices = dict((c, i) for i, c in enumerate(chars)) # 문자와 ID
indices_char = dict((i, c) for i, c in enumerate(chars)) # ID와 문자
print(char_indices)            # ... '것': 106, '겄': 107, '겅': 108,...
print(indices_char)            # ... 106: '것', 107: '겄', 108: '겅',...

# 텍스트를 maxlen개의 문자로 자르고 다음에 오는 문자 등록하기
maxlen = 20
step = 3
sentences = []
next_chars = []

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])

print('학습할 구문 수:', len(sentences))        # 102316
print('텍스트를 ID 벡터로 변환')

X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
#print(X)
    # [[[False False False ... False False False]
    #   [False False False ... False False False]
    #   ...

print()
#print(y)
    # [[False False False ... False False False]
    #   [False False False ... False False False]
    #   ...

for i, sent in enumerate(sentences):
    for t, char in enumerate(sent):
        X[i, t, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1

print(X[:5])
print(y[:5])

# 모델 구축하기(LSTM(RNN의 개량종)) -------------
# 하나의 LSTM 층과 그 뒤에 Dense 분류층 추가
model = tf.keras.Sequential()
model.add(tf.keras.layers.LSTM(128, input_shape=(maxlen, len(chars))))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dense(128))
model.add(tf.keras.layers.Activation('relu'))
model.add(tf.keras.layers.Dense(len(chars)))
model.add(tf.keras.layers.Activation('softmax'))

opti = tf.keras.optimizers.Adam(lr=0.001)
model.compile(loss='categorical_crossentropy', optimizer=opti, metrics=['acc'])

from tensorflow.keras.callbacks import EarlyStopping
es = EarlyStopping(patience = 5, monitor='loss')
model.fit(X, y, epochs=500, batch_size=64, verbose=2, callbacks=[es])
print(model.evaluate(X, y))
#print(model.eval‎uate(X, y))

# 확률적 샘플링 처리 함수(무작위적으로 샘플링하기 위함)
# 모델의 예측이 주어졌을 때 새로운 글자를 샘플링 
def sample_func(preds, variety=1.0):    # 후보를 배열에서 꺼내기
    # array():복사본, asarray():참조본 생성 - 원본 변경시 복사본은 변경X 참조본은 변경O
    preds = np.asarray(preds).astype('float64') 
    preds = np.log(preds) / variety     # 로그확률 벡터식을 코딩
    exp_preds = np.exp(preds)   # 자연상수 얻기
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)  # 다항식분포로 샘플 얻기
    return np.argmax(probas)

for num in range(1, 2):   # 학습시키고 텍스트 생성하기 반복    1, 60
    print()
    print('--' * 30)
    print('반복 =', num)

    # 데이터에서 한 번만 반복해서 모델 학습
    model.fit(X, y, batch_size=128, epochs=1, verbose=0) 

    # 임의의 시작 텍스트 선택하기
    start_index = random.randint(0, len(text) - maxlen - 1)

    for variety in [0.2, 0.5, 1.0, 1.2]:     # 다양한 문장 생성
        print('\n--- 다양성 = ', variety)    # 다양성 = 0.2 -> 다양성 =  0.5 -> ...
        generated = ''
        sentence = text[start_index: start_index + maxlen]
        generated += sentence
        print('--- 시드 = "' + sentence + '"')  # --- 시드 = "께 간뎅이가 부어서, 시부릴기력 있거"...
        sys.stdout.write(generated)


        # 시드를 기반으로 텍스트 자동 생성. 시드 텍스트에서 시작해서 500개의 글자를 생성
        for i in range(500):
            x = np.zeros((1, maxlen, len(chars))) # 지금까지 생성된 글자를 원핫인코딩 처리
            for t, char in enumerate(sentence):
                x[0, t, char_indices[char]] = 1.
                

            # 다음에 올 문자를 예측하기(다음 글자를 샘플링)
            preds = model.predict(x, verbose=0)[0]
            next_index = sample_func(preds, variety)    # 다양한 문장 생성을 위함
            next_char = indices_char[next_index]

            # 출력하기
            generated += next_char
            sentence = sentence[1:] + next_char
            sys.stdout.write(next_char)
            sys.stdout.flush()
        print()