在使用yolo检测目标，进行数据集裁剪，之后拿裁剪后的图像进行训练。

`可以将此操作用作业务以及比赛等前处理。`

使用labelimg进行数据标注，训练数据后根据检测box裁剪img，mask。

- train_mydata：训练自己的数据集,部分参考[(2条消息) YOLOv5训练自己的数据集（超详细完整版）_深度学习菜鸟的博客-CSDN博客_yolov5训练自己数据集](https://blog.csdn.net/qq_36756866/article/details/109111065)
- 训练代码:train.py
- 检测裁剪数据集代码:detect.py
