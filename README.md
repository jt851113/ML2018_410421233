### 單層神經網路的圖片解碼器實作  

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
