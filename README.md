### Assignment I : 單層神經網路的圖片解碼器實作  

### 環境與套件:
1. PIL
2. NUMPY

### Pipeline:
1. 用PIL將圖片讀入
2. 將圖片轉存到NUMPY ARRAY
3. 利用LMS(Least Mean Error)來實作 Gradient descent 的部分 尋找權重
4. 將Eprime替換I,輸出結果圖片

### 細節與參數:
* 關於MaxIterlimit : 控制epoch，也就是迭代的次數，我預設為10

* 關於α : lerningrate，預設為0.00001

* 關於ε : 因為資料很少大概第一個epoch結束就觸底了，所以我沒有設這個參數，之後若有機會會加上去

* 關於weights : 初始化用了numpy的random，給予0~1間的任意值 
 
* learningrate為0.00001時基本上第一個epoch就收斂了所以幾乎後面權重都沒什麼變動 

  ![lr=1e-05](https://github.com/jt851113/ML2018_410421233/raw/master/photo/1e-05.JPG)
  
* learningrate為0.000000001時，一開始算差了一點，但大概到第3個epoch跟第4個epoch也開始收斂了

  ![lr=1e-08](https://github.com/jt851113/ML2018_410421233/raw/master/photo/1e-08.JPG)
  
* 解答是老師的帥臉
  
  ![ans](https://github.com/jt851113/ML2018_410421233/raw/master/photo/Iprime.jpg)

### 雜談:
這次算是花了不少時間，主要是因為一開始走了不少冤枉路 ~~(因為想偷吃步所以都在keras跟sklearn上面)~~  
不過後面理解後就寫很快了  
之後最主要的困難是會搞混很多參數的型態不知道要用哪個型態  
算是紮紮實實的上了一課，也對ML有更深的理解 ~~(因為很多時候看不懂就要翻書了)~~

### Assignment II : 手寫辨識

### 環境與套件:
1. Scikit-Learn
2. NUMPY

### Pipeline:
1. 讀入sklearn手寫資料組
2. 將圖片轉為灰階
3. 利用PCA來降維
4. 送入SVM來訓練MODEL

###  細節與參數:
* 轉灰階其實就是將原始圖片讀入後將每個圖片中每個PIXEL除以255 讓值介於0~1之間
* 最難的部分是調整PCA的參數，太大要跑非常久尤其是SKLEARN不支援GPU加速 太小根本學不到東西
* 有試過把PCA的N_COMPONENT參數調為1，明顯沒用，完全沒學習到
  ![FAIL](https://github.com/jt851113/ML2018_410421233/blob/master/photo/FAIL.png)
* 訓練過程
  ![Process](https://github.com/jt851113/ML2018_410421233/blob/master/photo/PROCESS.JPG)
  
### 雜談:
這次不算太難，主要是調整pca降維那邊很難調整，若狀況允許，當然直接扁平化是最好，這樣能夠保留完整的特徵值
但在跟速度的妥協下，還是讓他減少維度，因為之前有練習過用keras的手寫辨識，跟那次不同，那次是用神經網路來實作
跟這次用分類器做的感覺不太一樣，當然這也是個很好的學習機會，讓我能夠更加熟悉python的套件以及複習之前上課所學到的
