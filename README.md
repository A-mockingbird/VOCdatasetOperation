# VOCtype-datasetOperation
文件名：VOCOpertationLibrary.py
--VOC类
  初始化：dataset_anno-数据集存储标签的目录
          dataset_img-数据集存储图像的目录，可为None
          num_class-数据集类别数量，可为None(现在的实现均不需要)
--主要方法
  _ParseAnnos(self, annodir=None):分析数据集标注信息，返回一个存储字典的列表
                    每个字典存在一个图想内的全部标签信息，
                   {'file':文件名, 'info': 标签类别和坐标, 'size': 图像尺寸}
                    其中文件名为字符串，
                    'info'为列表的列表，[[类名, xmin, ymin, xmax, ymax]]
                    'size'为元组,(宽，高)
                    输入：annodir-xml文件存储目录，可为空，空self.dataset_anno
  _parseannotation(self, annofile):分析单个xml文件标注信息，
                                   输入：xml文件地址
                                   输出：列表[[类名, xmin, ymin, xmax, ymax]]
  _DelAnnotations(self, delclass):删除数据集指定类别的全部标签信息
                                  输入：delclass为列表，存储全部需要删除的标签
  _deletesinglefile(self, filepath, delclass):删除单个xml文件的指定类别标签
                                              输入：filepath-xml文件地址
                                                    declass-删除的标签类别列表
  _Crop(self, imgdir, cropdir, annos=None):将数据集中的全部标注框裁剪并保存
                                           输入：imgdir-数据集图像目录；
                                                 cropdir-裁剪图像保存目录；
                                                 annos-标签信息
  _DisplayDirectObjec(self):显示数据集每个图像的指定目标框
                            对应每一个图像，显示图像内全部目标框标注信息
                            选择想要显示的目标框，输入序号，例如：
                            0 1 2#每个序号间用空格分隔，结束用回车
                            
