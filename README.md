# VOCtype-datasetOperation
�ļ�����VOCOpertationLibrary.py
--VOC��
  ��ʼ����dataset_anno-���ݼ��洢��ǩ��Ŀ¼
          dataset_img-���ݼ��洢ͼ���Ŀ¼����ΪNone
          num_class-���ݼ������������ΪNone(���ڵ�ʵ�־�����Ҫ)
--��Ҫ����
  _ParseAnnos(self, annodir=None):�������ݼ���ע��Ϣ������һ���洢�ֵ���б�
                    ÿ���ֵ����һ��ͼ���ڵ�ȫ����ǩ��Ϣ��
                   {'file':�ļ���, 'info': ��ǩ��������, 'size': ͼ��ߴ�}
                    �����ļ���Ϊ�ַ�����
                    'info'Ϊ�б���б�[[����, xmin, ymin, xmax, ymax]]
                    'size'ΪԪ��,(����)
                    ���룺annodir-xml�ļ��洢Ŀ¼����Ϊ�գ���self.dataset_anno
  _parseannotation(self, annofile):��������xml�ļ���ע��Ϣ��
                                   ���룺xml�ļ���ַ
                                   ������б�[[����, xmin, ymin, xmax, ymax]]
  _DelAnnotations(self, delclass):ɾ�����ݼ�ָ������ȫ����ǩ��Ϣ
                                  ���룺delclassΪ�б��洢ȫ����Ҫɾ���ı�ǩ
  _deletesinglefile(self, filepath, delclass):ɾ������xml�ļ���ָ������ǩ
                                              ���룺filepath-xml�ļ���ַ
                                                    declass-ɾ���ı�ǩ����б�
  _Crop(self, imgdir, cropdir, annos=None):�����ݼ��е�ȫ����ע��ü�������
                                           ���룺imgdir-���ݼ�ͼ��Ŀ¼��
                                                 cropdir-�ü�ͼ�񱣴�Ŀ¼��
                                                 annos-��ǩ��Ϣ
  _DisplayDirectObjec(self):��ʾ���ݼ�ÿ��ͼ���ָ��Ŀ���
                            ��Ӧÿһ��ͼ����ʾͼ����ȫ��Ŀ����ע��Ϣ
                            ѡ����Ҫ��ʾ��Ŀ���������ţ����磺
                            0 1 2#ÿ����ż��ÿո�ָ��������ûس�