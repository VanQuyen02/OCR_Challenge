import albumentations as A
import cv2
import os 

path = "D:/KALAPA_ByteBattles_2023_OCR_Set1/OCR/training_data/images"
path_save = "D:/KALAPA_ByteBattles_2023_OCR_Set1/Augmented_Data/Elastic_Transform"
count =0
for fold in os.listdir(path):
    folder_path = os.path.join(path,fold)
    for image in os.listdir(folder_path):
        image_path = os.path.join(folder_path,image)
        # Đọc ảnh
        img = cv2.imread(image_path)
        idx =1
        for i in range(40,60,5):
            for j in range(5,8,1):
                # Áp dụng các biện pháp augment
                transform = A.Compose([
                    A.ElasticTransform(alpha=i, sigma=j,alpha_affine=0.01, p=1),       
                ])
                # Áp dụng augmentations
                augmented = transform(image=img)
                augmented_image = augmented['image']
                image_name = image.split(".jpg")[0]+"_"+str(idx)+".jpg"
                image_name_save = "elas"+"_"+fold+"_"+image_name
                idx+=1
                image_path_save = os.path.join(path_save,image_name_save)
                cv2.imwrite(image_path_save, augmented_image)
                count+=1
                print("Number of image save: {}".format(count))