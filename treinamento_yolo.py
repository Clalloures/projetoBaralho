from pathlib import Path
from shutil import copyfile
from ultralytics import YOLO
import os
import random

# Diretórios das imagens e dos rótulos
train_dir_apaus = "C:\\Users\\Antonio Ferreira\\Desktop\\prova2\\train\\ace of clubs"
train_dir_aouros = "C:\\Users\\Antonio Ferreira\\Desktop\\prova2\\train\\ace of diamonds"
train_dir_acopas = "C:\\Users\\Antonio Ferreira\\Desktop\\prova2\\train\\ace of hearts"
train_dir_oito_copas = "C:\\Users\\Antonio Ferreira\\Desktop\\prova2\\train\\eight of hearts"
train_dir_cinco_ouros = "C:\\Users\\Antonio Ferreira\\Desktop\\prova2\\train\\five of diamonds"
val_dir = "C:\\Users\\Antonio Ferreira\\Desktop\\prova2\\var_dir\\"

# Função para criar diretórios 'val' e mover imagens e rótulos
def create_val_and_move_images(src_dir, dest_dir, val_ratio=0.2):
    os.makedirs(dest_dir, exist_ok=True)
    files = os.listdir(src_dir)
    random.shuffle(files)
    num_files_val = int(len(files) * val_ratio)
    val_files = files[:num_files_val]
    for file_name in val_files:
        # Verificar se existe um arquivo de rótulo correspondente
        label_file = file_name.replace(".jpg", ".txt")
        if label_file not in files:
            continue  # Ignorar a imagem se não houver arquivo de rótulo
        # Mover imagens
        img_src = os.path.join(src_dir, file_name)
        img_dest = os.path.join(dest_dir, file_name)
        copyfile(img_src, img_dest)
        # Mover rótulos
        label_src = os.path.join(src_dir, label_file)
        label_dest = os.path.join(dest_dir, label_file)
        copyfile(label_src, label_dest)

# Criar diretórios 'val' e mover imagens
# Criar diretórios 'val' e mover imagens e rótulos
create_val_and_move_images(train_dir_apaus, os.path.join(val_dir, "a_paus"))
create_val_and_move_images(train_dir_aouros, os.path.join(val_dir, "a_ouros"))
create_val_and_move_images(train_dir_acopas, os.path.join(val_dir, "a_copas"))
create_val_and_move_images(train_dir_oito_copas, os.path.join(val_dir, "oito_copas"))
create_val_and_move_images(train_dir_cinco_ouros, os.path.join(val_dir, "cinco_ouros"))


# Criar arquivo data_custom.yaml
data_custom_yaml = """
train: 
  - {}
  - {}
  - {}
  - {}
  - {}
val: {}
nc: 5
names: ["a_paus", "a_ouros", "a_copas", "oito_copas", "cinco_ouros"]
""".format(train_dir_apaus, train_dir_aouros, train_dir_acopas, train_dir_oito_copas, train_dir_cinco_ouros, val_dir)

with open("data_custom.yaml", "w") as f:
    f.write(data_custom_yaml)

model = YOLO("yolov8n.pt")

# Train the model
results = model.train(data="data_custom.yaml", epochs=30, imgsz=640, batch=8)

# Save the trained model
model.save("yolov8n_trained.pt") # não usar esse e sim o que está escrito na saida do treinamento do yolo