"""
File:VOC.py
"""

import sys
import os
import xml.etree.ElementTree as ET
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random
import shutil
import VOCOperationLibrary as vol

class VOC(object):
    def __init__(self, dataset_anno, dataset_img=None, num_class=None):
        if os.path.exists(dataset_anno) == False:
            raise  FileNotFoundError
        self.dataset_anno = dataset_anno
        self.dataset_img = dataset_img
        self.num_class = num_class
        self.dirname = os.path.dirname(self.dataset_anno)
        self.listanno = self._listanno()

    def _listanno(self, annodir=None):
        """return the list of all above of annotation file"""
        if annodir == None:
            annodir = self.dataset_anno
        return os.listdir(annodir)

    def _listimg(self):
        """return the list of all above of image file"""
        if self.dataset_img == None:
            print("you should give a image path of dataset in creating VOC class!")
            raise FileNotFoundError
        else:
            return os.listdir(self.dataset_img)

    def _ParseAnnos(self, annodir=None):
        """
        return the information of all above of annotation in this dataset_anno,
        format: a list of dictionary, include file name, annotation, size
        ([{file, annotation, size}])
        annotation is a list, [cls, xmin, ymin, xmax, ymax]
        size if a tuple, (weight, height)
        """
        annos = []
        if annodir == None:
            annodir = self.dataset_anno
            annolist = self.listanno
        else:
            annolist = self._listanno(annodir)
        for annofile in annolist:
            if annofile[-4:] != ".xml":
                continue
            annotation = vol._parseannotation(os.path.join(annodir, annofile))
            annos.append({'file': annofile, 'info': annotation[0], 'size': annotation[1]})
        return annos

    def _DelAnnotations(self, delclass, annodir=None):
        """
        Delete specific cls
        Precondition:delclass-a list of what's annotaion name you want to delete
        """
        if delclass == None:
            return
        if annodir== None:
            annodir = self.dataset_anno
        annolist = self._listanno(annodir) 
        for annofile in annolist:
            vol._deletesinglefile(os.path.join(annodir, annofile), delclass)



    def _ChangeAnnotation(self, oldcls, newcls, annodir=None):
        if annodir == None:
            annodir = self.dataset_anno
        annolist = self._listanno(annodir)
        for annofile in annolist:
            vol._changeone(os.path.join(annodir,annofile), oldcls, newcls)

    

    def _Crop(self, imgdir, cropdir, annos=None):
        """
        To crop all the box region of object in dataset
        """
        if annos == None:
            annos = self._ParseAnnos()
        total = len(annos)
        for num, annotation in enumerate(annos):
            annofile = annotation['file']
            if os.path.exists(imgdir+annofile[:-4]+'.jpg') == False:
                raise FileNotFoundError
            pil_im = Image.open(imgdir+annofile[:-4]+'.jpg') 
            for i, obj in enumerate(annotation['info']):
                obj_class = obj[0]
                obj_box = tuple(obj[1:5])
                if os.path.exists(cropdir+obj_class) == False:
                    os.mkdir(cropdir+obj_class)
                region = pil_im.crop(obj_box)
                pil_region = Image.fromarray(np.uint8(region))
                pil_region.save(os.path.join(cropdir+obj_class, 
                                annofile[:-4]+'_'+str(i)+'.jpg'))
            process = int(num*100 / total)
            s1 = "\r%d%%[%s%s]"%(process,"*"*process," "*(100-process))
            s2 = "\r%d%%[%s]"%(100,"*"*100)
            sys.stdout.write(s1)
            sys.stdout.flush()
        sys.stdout.write(s2)
        sys.stdout.flush()
        print('')
        print("crop is completed!")
    
    def _Countobject(self, annofile=None):
        """
        Count the label numbers of every class, and print it
        Precondition: annofile-the direction of xml file
        """
        if annofile == None:
            annofile = self.dataset_anno
        annoparse = self._ParseAnnos(annofile)
        count = {}
        for anno in annoparse:
            for obj in anno['info']:
                if obj[0] in count:
                    count[obj[0]] +=1
                else:
                    count[obj[0]] = 1
        for c in count.items():
            print("{}: {}".format(c[0], c[1]))
        return count

    def _DisplayDirectObjec(self):
        """
        To display what's box you want to display.
        """
        imglist = self._listimg()
        print("input what object you want display, space between numbers")
        parseannos = self._ParseAnnos()
        for i, annos in enumerate(parseannos):
            print("file name: {0}".format(annos['file'][:-4]))
            if annos['info'] == []:
                print("This image don't have annotation, so programme step it and go on!")
                continue
            for j, objs in enumerate(annos['info']):
                print('''({}): cls={}, \
                    box=[{:0>4d}, {:0>4d}, {:0>4d}, {:0>4d}]'''.format(
                    j, objs[0], objs[1], objs[2], objs[3], objs[4]
                ))
            inputstr = input()
            numbers = [int(x) for x in inputstr.split(' ')]
            self._displayone(annos['info'], annos['file'], numbers)
        
    def _displayone(self, objs, annofile, nums, score=[900, 1000], threshold=0.5):
        """
        display the annotation's box of one image
        Precondition: objs-the box information
                      annofile-annotation file name
                      nums-the object number of annotation which you want display
        """
        im = Image.open(self.dataset_img + annofile[:-4] + '.jpg')
        fig, ax = plt.subplots(figsize=(12, 12))
        ax.imshow(im, aspect='equal')
        for i, obj in enumerate(objs):
            if i in nums:
                s = random.randint(score[0], score[1]) / 1000.0
                bbox = obj[1:]
                ax.add_patch(
                        plt.Rectangle((bbox[0], bbox[1]),
                          bbox[2] - bbox[0],
                          bbox[3] - bbox[1], fill=False,
                          edgecolor='red', linewidth=3.5)
                        )
                ax.text(bbox[0], bbox[1] - 2,
                        '{:s} {:.3f}'.format(obj[0], s),
                        bbox=dict(facecolor='blue', alpha=0.5),
                        fontsize=14, color='white')

                ax.set_title(('detections with '
                        'p(box) >= {:.1f}').format(threshold),
                        fontsize=14)
        plt.axis('off')
        plt.tight_layout()
        plt.draw()
        plt.show()


    def _Mergeannotation(self, newdataset, olddataset=None):
        if olddataset == None:
            olddataset = self.dataset_anno
        annolist1 = os.listdir(olddataset)
        annolist2 = os.listdir(newdataset)
        for anno in annolist2:
            if anno in annolist1:
                print(anno)
                vol._mergeone(olddataset+anno, newdataset+anno)
            else:
                shutil.copy(newdataset+anno, olddataset+anno)

v = VOC('F:/数据集/优化后金具数据集/aaaa/')
print(v._ParseAnnos())
#v._Crop('F:/数据集/螺栓多标记数据集初建/JPEGImages/', 'F:/数据集/crops/')
#v._DelAnnotations(['123', '234'])
#v._DisplayDirectObjec()
#v._Mergeannotation('C:/Users/91279/Desktop/xml/', 'F:/xml/')
#v._DelAnnotations(['123'])