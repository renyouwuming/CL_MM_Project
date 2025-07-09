from torchvision.datasets import CIFAR100
from torchvision.transforms import ToPILImage
from tqdm import tqdm
import os

def convert_cifar100_to_images(root_dir, split='train'):
    dataset = CIFAR100(root=root_dir, train=(split=='train'), download=False)
    save_dir = os.path.join(root_dir, split)
    os.makedirs(save_dir, exist_ok=True)
    
    for idx, (img, label) in enumerate(tqdm(dataset)):
        class_name = dataset.classes[label]
        class_dir = os.path.join(save_dir, class_name)
        os.makedirs(class_dir, exist_ok=True)
        img = ToPILImage()(img)
        img.save(os.path.join(class_dir, f"{idx}.png"))

# 使用方法
convert_cifar100_to_images(r'/home/zqj/CL_project/cifar-100-python', split='train')
convert_cifar100_to_images(r'/home/zqj/CL_project/cifar-100-python', split='test')
