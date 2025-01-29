% Leer la imagen
img = imread('imagen.png');
% Convertir la imagen a una matriz de doble precisión
img_double = double(img);
% Obtener las dimensiones de la imagen
[rows, cols, ~] = size(img_double);
% Convertir la imagen a una matriz de píxeles (cada fila representa un píxel)
pixels = reshape(img_double, rows * cols, 3);
% Definir el número de clusters
num_clusters = 5;
% Aplicar K-means a los píxeles de la imagen
[cluster_indices, centroids] = kmeans(pixels, num_clusters);
% Asignar a cada píxel el color del centroide más cercano
for i = 1:size(pixels, 1)
 pixels(i, :) = centroids(cluster_indices(i), :);
end
% Restaurar la estructura de la imagen
img_reconstructed = reshape(uint8(pixels), rows, cols, 3);
% Mostrar la imagen original y la imagen procesada
figure;
subplot(1, 2, 1);
imshow(img);
title('Imagen Original');
subplot(1, 2, 2);
imshow(img_reconstructed);
title('Imagen Procesada con K-means');