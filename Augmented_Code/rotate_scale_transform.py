import albumentations as A
import cv2
import os 

path = "D:/KALAPA_ByteBattles_2023_OCR_Set1/OCR/training_data/images"
path_save = "D:/KALAPA_ByteBattles_2023_OCR_Set1/Augmented_Data/Rotate_And_Scale_Transform"
count =0
for fold in os.listdir(path):
    folder_path = os.path.join(path,fold)
    for image in os.listdir(folder_path):
        image_path = os.path.join(folder_path,image)
        # Đọc ảnh
        img = cv2.imread(image_path)
        # Áp dụng các biện pháp augment
        transform = A.Compose([
        A.Rotate(limit=(-1.5,1.5), p=1),
        A.RandomScale(scale_limit=(-0.5,0), p=1),  # Change Scale to RandomScale
        ])
        # Áp dụng augmentations
        augmented = transform(image=img)
        augmented_image = augmented['image']
        image_name = "rotate_scale"+"_"+fold+"_"+image
        image_path_save = os.path.join(path_save,image_name)
        cv2.imwrite(image_path_save, augmented_image)
        count+=1
        print("Number of image save: {}".format(count))