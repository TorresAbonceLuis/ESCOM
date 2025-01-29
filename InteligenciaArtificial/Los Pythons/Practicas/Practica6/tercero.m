% Generar datos aleatorios
rng(1); % Fijar la semilla para reproducibilidad
data = [randn(100,2)*0.75+ones(100,2);
 randn(100,2)*0.5-ones(100,2)];
% Visualizar los datos
figure;
scatter(data(:,1), data(:,2));
title('Conjunto de Datos Aleatorios');
% Ajustar un modelo de mezcla gaussiana (GMM) a los datos
num_clusters = 2;
gmm_model = fitgmdist(data, num_clusters);
% Generar muestras del modelo ajustado
num_samples = 1000;
generated_data = random(gmm_model, num_samples);
% Visualizar los datos generados y los centroides de los clusters
figure;
scatter(generated_data(:,1), generated_data(:,2));
hold on;
plot(gmm_model.mu(:,1), gmm_model.mu(:,2), 'kx', 'MarkerSize', 15, 'LineWidth', 3);
title('Datos Generados por el Modelo de Mezcla Gaussiana');
legend('Datos Generados', 'Centroides');
hold off;