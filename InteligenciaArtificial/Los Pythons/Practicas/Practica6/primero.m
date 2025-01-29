% Generar datos aleatorios
rng(1); % Fijar la semilla para reproducibilidad
data = [randn(100,2)*0.75+ones(100,2);
 randn(100,2)*0.5-ones(100,2)];
% Visualizar los datos
figure;
scatter(data(:,1), data(:,2));
title('Conjunto de Datos Aleatorios');
% Definir el número de clusters (k)
k = 2;
% Aplicar K-means
[idx, centroids] = kmeans(data, k);
% Visualizar los clusters
figure;
gscatter(data(:,1), data(:,2), idx);
hold on;
plot(centroids(:,1), centroids(:,2), 'kx', 'MarkerSize', 15, 'LineWidth', 3);
title('Resultados de K-means');
legend('Cluster 1', 'Cluster 2', 'Centroides');
hold off; 