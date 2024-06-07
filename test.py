from pathlib import Path
from shutil import copyfile
import os
import random

# Função para criar diretórios 'val' e mover imagens e rótulos
def create_val_and_move_images(src_dir, dest_dir, val_ratio=0.2):
    os.makedirs(dest_dir, exist_ok=True)
    files = os.listdir(src_dir)
    random.shuffle(files)
    num_files_val = int(len(files) * val_ratio)
    val_files = files[:num_files_val]
    for file_name in val_files:
        # Mover imagens
        img_src = os.path.join(src_dir, file_name)
        img_dest = os.path.join(dest_dir, file_name)
        copyfile(img_src, img_dest)
        # Mover rótulos
        label_src = os.path.join(src_dir, file_name.replace(".jpg", ".txt"))
        label_dest = os.path.join(dest_dir, file_name.replace(".jpg", ".txt"))
        copyfile(label_src, label_dest)

# Função para ler e imprimir as classes nos arquivos de rótulos
def print_label_classes(label_file):
    with open(label_file, 'r') as f:
        for line in f:
            label_class = int(line.split()[0])  # Extrai a classe da primeira coluna
            print("Classe encontrada:", label_class)

# Diretórios das imagens e dos rótulos
train_dir_apaus = "C:\\Users\\Antonio Ferreira\\Downloads\\archive\\train\\ace of clubs"
val_dir = "C:\\Users\\Antonio Ferreira\\Desktop\\prova2\\var_dir\\"

# Criar diretórios 'val' e mover imagens
create_val_and_move_images(train_dir_apaus, os.path.join(val_dir, "a_paus"))

# Caminho para os arquivos de rótulos das imagens 113.jpg e 114.jpg
label_file_113 = os.path.join(train_dir_apaus, "113.txt")
label_file_114 = os.path.join(train_dir_apaus, "114.txt")


print("Arquivo de rótulos:", label_file_114)
# Imprimir classes nos arquivos de rótulos
print("Classes para a imagem 113.jpg:")
print_label_classes(label_file_113)

print("\nClasses para a imagem 114.jpg:")
print_label_classes(label_file_114)
