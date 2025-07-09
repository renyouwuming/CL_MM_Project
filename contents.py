import os
import shutil
from tqdm import tqdm

def flatten_dataset(source_dir, target_dir):
    os.makedirs(target_dir, exist_ok=True)
    for superclass in os.listdir(source_dir):
        super_path = os.path.join(source_dir, superclass)
        if not os.path.isdir(super_path):
            continue
        for class_name in os.listdir(super_path):
            class_path = os.path.join(super_path, class_name)
            if not os.path.isdir(class_path):
                continue
            new_class_path = os.path.join(target_dir, class_name)
            os.makedirs(new_class_path, exist_ok=True)
            for img_name in os.listdir(class_path):
                src_img = os.path.join(class_path, img_name)
                dst_img = os.path.join(new_class_path, img_name)
                shutil.copy2(src_img, dst_img)

# 用法示例：
flatten_dataset(
    source_dir="/home/zqj/CL_project/cifar-100-python/cifar-100-python/train",
    target_dir="/home/zqj/CL_project/flat_cifar100/train"
)

flatten_dataset(
    source_dir="/home/zqj/CL_project/cifar-100-python/cifar-100-python/test",
    target_dir="/home/zqj/CL_project/flat_cifar100/test"
)
