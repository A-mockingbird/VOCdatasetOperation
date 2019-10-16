# VOCtype-datasetOperation<br>
  包含解析VOC数据集、删除指定类别标签，修改指定类别标签名称、批量合并不同标签文件、<br>
  剪裁目标图像、画出图中标注框、统计数据集各类别标签数目，resize数据集<br>
  Parse VOC dataset, Delete or Correct direction class label, Merge different label file, <br>
  Crop object in image, Draw the box of object in image, Statistic the number of label,<br>
  resize all image in dataset and correct the annotation information(reszie dataset).<br>
  说明文档由中文写作，代码中为英文注释<br>
  The documentation is written in Chinese and the code comment is in English.
# 文件名：
  VOCOpertationLibrary.py: VOC数据集中单个xml文件操作函数库<br>
  VOC.py：VOC数据集类，操作整个数据集<br>
# --VOC类<br>
  ## 初始化：
  dataset_anno-数据集存储标签的目录<br>
  dataset_img-数据集存储图像的目录，可为None<br>
  num_class-数据集类别数量，可为None(现在的实现均不需要)<br>
## 主要方法<br>
  ## _ParseAnnos(self, annodir=None):
  分析数据集标注信息，返回一个存储字典的列表,每个字典存在一个图想内的全部标签信息，<br>
  {'file':文件名, 'info': 标签类别和坐标, 'size': 图像尺寸}<br>
  其中文件名为字符串，<br>
  'info'为列表的列表，[[类名, xmin, ymin, xmax, ymax]]<br>
  'size'为元组,(宽，高)<br>
  输入：annodir-xml文件存储目录，可为空，空self.dataset_anno<br>
  输出：列表[[类名, xmin, ymin, xmax, ymax], ...]<br>
  ## _DelAnnotations(self, delclass, annodir=None):
  删除数据集指定类别的全部标签信息<br>
  输入：delclass-列表，存储全部需要删除的类别名称，['1', '2', ...]<br>
        annofile-xml文件目录，若为空，=self.dataset_anno<br>
  ## _Countobject(self, annofile=None):
  统计数据集中全部类别标签的数目
  输入：annofile-xml文件目录，若为空，=self.dataset_anno
  返回：字典，{'类别名称': 统计数目, ...}
  ## _ChangeAnnotation(self, oldcls, newcls, annodir=None):
  修改指定类别标签的名称<br>
  输入：oldcls-需修改的类别名称<br>
        newcls-修改后的类别名称<br>
        annofile-xml文件目录，若为空，=self.dataset_anno<br>
  ## _Crop(self, imgdir, cropdir, annos=None):
  将数据集中的全部标注框裁剪并保存<br>
  输入：imgdir-数据集图像目录；<br>
  cropdir-裁剪图像保存目录；<br>
  annos-标签信息<br>
  ## _DisplayDirectObjec(self):
  显示数据集每个图像的指定目标框,对应每一个图像，显示图像内全部目标框标注信息<br>
  选择想要显示的目标框，输入序号，例如：<br>
  0 1 2#每个序号间用空格分隔，结束用回车<br>
  ## _Mergeannotation(self, newdataset, olddataset=None):
  将俩个数据集(俩个数据集中存在相同的图片)的全部标签合并,合并后存储在olddataset数据集中<br>
  此方法的意义：多人分工标注时，将不同人标注的数据合并(例如没人标一类的情况下)
  输入:newdataset-需要合并的新数据集<br>
       olddataset-需要合并的旧数据集，合并后数据存放在此数据集中<br>
  ## _Resize(self, newsize, annodir=None, imgdir=None):
  resize数据集中全部图像，并修改标注信息<br>
  输入:newsize-rezise的尺寸，元组，(宽, 高)<br>
       annodir-标注xml文件目录<br>
       imgdir-图像文件目录<br>
 # --VOC数据集xml文件操作函数库
  ## _parseannotation(annofile):
  分析单个xml文件标注信息，<br>
  输入：xml文件地址<br>
  返回：列表，[[类名, xmin, ymin, xmax, ymax], ...]<br>
  ## _deletesinglefile(annofile, delclass):
  删除单个xml文件的指定类别标签<br>
  输入：annofile-xml文件地址<br>
        declass-删除的标签类别名称列表<br>
  ## _changeone(annofile, oldcls, newcls, newsize=None):
  修改单个xml文件标注信息，当oldcls!=newcls时，可修改指定类别名称<br>
  当newsize!=None时，可修改resize图像后的标注信息<br>
  输入：annofile-xml文件路径<br>
        oldcls-需修改的类别名称<br>
        newcls-修改后的类别名称<br>
  ## appendobj(root, annotation):
  增加标签信息<br>
  输入：root-xml根节点(import xml.etree.ElementTree as ET)<br>
        annotation-标签信息，列表，[[类名, xmin, ymin, xmax, ymax], ...]<br>
  ## _mergeone(anno1, anno2):
  合并俩个标签xml文件<br>
  输入:anno1-标签文件，合并后存储在anno1中<br>
       anno2-标签文件<br>
