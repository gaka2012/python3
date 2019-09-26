# python3

1.runmul.py会读取gcap目录下的所有事件，并读取地震目录中的地震震级作为参数，最终调用run_gcap.pl进行批量反演。
2.rundraw_err.py会读取gcap目录下的所有地震事件，读取他们反演后得到的out文件，据此生成gmt文件，并画出误差随深度变化的图，生成的图会复制到每个地震事件中。并删除中间产生的各种临时文档。
3.rungcap_mul.py是一个多线程用来跑朱教授的cap.pl程序的。
4.changetoFM.py将FM转换成msatsi反演所需要的数据格式:1分区 2将走向转换成dip direction
