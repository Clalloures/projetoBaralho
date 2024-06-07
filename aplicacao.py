from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2

# Load the model
model = YOLO("C:\\Users\\Antonio Ferreira\\Desktop\\prova2\\yolo\\train9\\weights\\best.pt")

# Define a mapping for card classes to numeric values
card_values = {
    'a_ouros': 1,
    'a_copas': 1,
    'a_paus': 1,
    'cinco_ouros': 5,
    'oito_copas': 8
}

def load_and_predict(image_path):
    # Predict with the model
    results = model(image_path)  # predict on an image

    # Extract the predicted class (assuming the class represents the rank of the card)
    predicted_class = results[0].names[int(results[0].boxes[0].cls)]

    # Convert BGR to RGB for displaying with matplotlib
    predicted_image = results[0].plot()
    predicted_image_rgb = cv2.cvtColor(predicted_image, cv2.COLOR_BGR2RGB)
    
    # Read the original image and convert to RGB
    original_image = cv2.imread(image_path)
    original_image_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    
    return original_image_rgb, predicted_image_rgb, predicted_class

def main():
    # Get image paths from the user
    image_path_player1 = input("Digite o caminho da imagem da carta do Jogador 1: ")
    image_path_player2 = input("Digite o caminho da imagem da carta do Jogador 2: ")

    # Load and predict for both players
    original_image1, predicted_image1, predicted_class1 = load_and_predict(image_path_player1)
    original_image2, predicted_image2, predicted_class2 = load_and_predict(image_path_player2)

    # Get the numeric values of the predicted classes
    value1 = card_values[predicted_class1]
    value2 = card_values[predicted_class2]

    # Compare the predicted classes to determine the winner
    if value1 > value2:
        winner = "Jogador 1 venceu!"
    elif value1 < value2:
        winner = "Jogador 2 venceu!"
    else:
        winner = "Empate!"

    # Display the original and predicted images with the result
    plt.figure(figsize=(15, 7))

    plt.subplot(2, 2, 1)
    plt.title("Original Image - Jogador 1")
    plt.imshow(original_image1)
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.title("Predicted Image - Jogador 1")
    plt.imshow(predicted_image1)
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.title("Original Image - Jogador 2")
    plt.imshow(original_image2)
    plt.axis('off')

    plt.subplot(2, 2, 4)
    plt.title("Predicted Image - Jogador 2")
    plt.imshow(predicted_image2)
    plt.axis('off')

    plt.suptitle(winner, fontsize=16)
    plt.show()

if __name__ == "__main__":
    main()
