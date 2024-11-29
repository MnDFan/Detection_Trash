from ultralytics import YOLO
import torch
import logging
torch.cuda.empty_cache()

# Configuration des logs
logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)

# Charger le modèle de détection YOLOv8
model = YOLO('yolo11m.pt')

# Vérifier CUDA
device = "cuda:0" if torch.cuda.is_available() else "cpu"
#device = "cpu"
logging.info(f"Utilisation de : {device}")
if torch.cuda.is_available():
    logging.info(f"GPU détectée : {torch.cuda.get_device_name(0)}")
    logging.info(f"CUDA version : {torch.version.cuda}")

# Lancer l'entraînement
if __name__ == '__main__':
    results = model.train(
        data='data.yaml',
        #amp=False,
        epochs=50,
        imgsz=640,
        batch=12,
        name='testv11',
        cache='disk',
        device=device  # Spécifier le device CUDA
    )