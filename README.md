### ��h���g�������Ϥ��ѽX����@  

### Pipeline:
1. ��PIL�N�Ϥ�Ū�J
2. �N�Ϥ���s��NUMPY ARRAY
3. �Q��LMS(Least Mean Error)�ӹ�@ Gradient descent ������ �M���v��
4. �NEprime����I,��X���G�Ϥ�

### �Ӹ`�P�Ѽ�:
* ����MaxIterlimit : ����epoch�A�]�N�O���N�����ơA�ڹw�]��10

* ����\ : lerningrate�A�w�]��0.00001

* ����` : �]����ƫܤ֤j���Ĥ@��epoch�����NĲ���F�A�ҥH�ڨS���]�o�ӰѼơA����Y�����|�|�[�W�h

* ����weights : ��l�ƥΤFnumpy��random�A����0~1�������N�� 
 
* learningrate��0.00001�ɰ򥻤W�Ĥ@��epoch�N���ĤF�ҥH�X�G�᭱�v�����S�����ܰ� 

  ![lr=1e-05](https://github.com/jt851113/ML2018_410421233/raw/master/photo/1e-05.JPG)
  
* learningrate��0.000000001�ɡA�@�}�l��t�F�@�I�A���j�����3��epoch���4��epoch�]�}�l���ĤF

  ![lr=1e-08](https://github.com/jt851113/ML2018_410421233/raw/master/photo/1e-08.JPG)
  
* �ѵ��O�Ѯv�����y
  
  ![ans](https://github.com/jt851113/ML2018_410421233/raw/master/photo/Iprime.jpg)

### ����:
�o����O��F���֮ɶ��A�D�n�O�]���@�}�l���F���֭ުP��~~(�]���Q���Y�B�ҥH���bkeras��sklearn�W��)~~
���L�᭱�z�ѫ�N�g�ܧ֤F  
����̥D�n���x���O�|�d�V�ܦh�Ѽƪ����A�����D�n�έ��ӫ��A  
��O�ϲϹ�ꪺ�W�F�@�ҡA�]��ML����`���z��~~(�]���ܦh�ɭԬݤ����N�n½�ѤF)~~