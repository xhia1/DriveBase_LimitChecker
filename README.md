# DriveBase_LimitChecker




  
    settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)  
        straight_speed (Number, mm/s)・・・直進のスピード  
        straight_acceleration (Number, mm/s²)・・・直進の加速度  
        turn_rate (Number, deg/s)・・・回転のスピード  
        turn_acceleration (Number, deg/s²)・・・回転の加速度  

  

## このプログラムについて

ロボットのスピードの上限は、以下のような要素で変わります。

タイヤの直径
タイヤ同士の距離（axle_track）
ギアの組み方

そのため、ロボットごとに適切な値を探すのは大変です。

このプログラムを使えば、
DriveBase に設定した「タイヤ直径」と「タイヤ間距離」をもとに、
settings() に指定できる上限値の目安を自動で測定できます。

※モーターの種類は Pybricks が自動で認識するため、
特に設定する必要はありません。


## 使い方
wheel_diameter と axle_track を設定して DriveBase を作成
このプログラムを実行
表示された上限値を参考に settings() を調整


## ⚠注意

この結果はあくまで目安です。
実際のロボットの動きに合わせて微調整してください。
