# load packages
import cv2
import numpy as np
import os
import torch
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#%matplotlib inline
def myDetector():
    i=-1
    if os.path.exists(img_dir):
        if os.listdir(img_dir) is []:
            print("No images!")
            exit(0)
        num_img = len(os.listdir(img_dir))
        for img in os.listdir(img_dir):
            if not img.endswith("jpg"):
                continue
            i+=1
            image_dir = os.path.join(img_dir, img)
            image = cv2.imread(image_dir)
            gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            sift = cv2.xfeatures2d.SIFT_create()
            kp = sift.detect(gray,None)
            img=cv2.drawKeypoints(gray,kp,image) 
            kp.sort(key=lambda kp:kp.response,reverse=True)
            for j in range(200):
             for c in range(1): 
                 keypoints[i,j,c]=kp[j].pt[c]         
            key_output_dir='output_detecor.pth'
            torch.save(keypoints,output_dir+key_output_dir)
            image_number=i
            print(i)
            patcher(gray,image_number)
        print(keypoints.shape)
    else:
        print("image folder not exists!")
        exit(0)

def patcher(gray,image_number):

    patch_size = 32
    patch5 = getPatches(keypoints[image_number], gray,size=patch_size, num=200)
    all_patches.append(patch5)
   # for idx,patch in enumerate(patch5):
    #    im = patch[0].numpy()
    #    plt.imshow(im)
    #    plt.show() 
    if (image_number==9):
        patches = torch.stack(all_patches) 
        dir_output = "patches.pt"
        torch.save(patches, output_dir+dir_output)
        print(patches.shape)

def getPatches(kps, img, size, num):
    res = torch.zeros(num, 1, size, size)
    if type(img) is np.ndarray:
        img = torch.from_numpy(img)

    h, w = img.shape      # note: for image, the x direction is the verticle, y-direction is the horizontal...
    source=torch.zeros(h+34,w+34)
    source[17:h+17,17:w+17]=img[:,:]
    img=source
    h, w = img.shape
    for i in range(num):
        cx, cy = kps[i]
        cx, cy = int(cx)+17, int(cy)+17
        dd = int(size/2)
        xmin, xmax = max(0, cx - dd), min(w, cx + dd ) 
        ymin, ymax = max(0, cy - dd), min(h, cy + dd ) 
        xmin_res, xmax_res = dd - min(dd,cx), dd + min(dd, w - cx)
        ymin_res, ymax_res = dd - min(dd,cy), dd + min(dd, h - cy)
        res[i, 0, xmin_res: xmax_res, ymin_res: ymax_res] = img[ymin: ymax, xmin: xmax] 
    return res
   
if __name__=="__main__":
    img_dir = "/media/roshan/Backup/CS537/HW1/dataset/input/images/"
    output_dir='/media/roshan/Backup/CS537/HW1/dataset/input/'
    keypoints=torch.empty(10,200,2)
    all_patches = []
    myDetector()

