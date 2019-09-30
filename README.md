# VOCtype-datasetOperation<br>
# 文件名：VOCOpertationLibrary.py<br>
# --VOC类<br>
  ## 初始化：dataset_anno-数据集存储标签的目录<br>
          dataset_img-数据集存储图像的目录，可为None<br>
          num_class-数据集类别数量，可为None(现在的实现均不需要)<br>
# --主要方法<br>
  ## _ParseAnnos(self, annodir=None):分析数据集标注信息，返回一个存储字典的列表<br>
                    每个字典存在一个图想内的全部标签信息，<br>
                   {'file':文件名, 'info': 标签类别和坐标, 'size': 图像尺寸}<br>
                    其中文件名为字符串，<br>
                    'info'为列表的列表，[[类名, xmin, ymin, xmax, ymax]]<br>
                    'size'为元组,(宽，高)<br>
                    输入：annodir-xml文件存储目录，可为空，空self.dataset_anno<br>
  ## _parseannotation(self, annofile):分析单个xml文件标注信息，<br>
                                   输入：xml文件地址<br>
                                   输出：列表[[类名, xmin, ymin, xmax, ymax]]<br>
  ## _DelAnnotations(self, delclass):删除数据集指定类别的全部标签信息<br>
                                  输入：delclass为列表，存储全部需要删除的标签<br>
  ## _deletesinglefile(self, filepath, delclass):删除单个xml文件的指定类别标签<br>
                                              输入：filepath-xml文件地址<br>
                                                    declass-删除的标签类别列表<br>
  ## _Crop(self, imgdir, cropdir, annos=None):将数据集中的全部标注框裁剪并保存<br>
                                           输入：imgdir-数据集图像目录；<br>
                                                 cropdir-裁剪图像保存目录；<br>
                                                 annos-标签信息<br>
  ## _DisplayDirectObjec(self):显示数据集每个图像的指定目标框<br>
                            对应每一个图像，显示图像内全部目标框标注信息<br>
                            选择想要显示的目标框，输入序号，例如：<br>
                            0 1 2#每个序号间用空格分隔，结束用回车<br>
                            
