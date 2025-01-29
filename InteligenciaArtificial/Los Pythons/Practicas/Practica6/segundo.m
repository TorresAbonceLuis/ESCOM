% Generar datos aleatorios
rng(1); % Fijar la semilla para reproducibilidad
data = [randn(100,2)*0.75+ones(100,2);
 randn(100,2)*0.5-ones(100,2)];
% Visualizar los datos
figure;
scatter(data(:,1), data(:,2));
title('Conjunto de Datos Aleatorios');
% Aplicar Mean Shift
bandwidth = 1.0; % Parámetro de ancho de banda
[cluster_centers, assignments] = MeanShiftCluster(data, bandwidth);
% Visualizar los clusters
figure;
gscatter(data(:,1), data(:,2), assignments);
hold on;
plot(cluster_centers(:,1), cluster_centers(:,2), 'kx', 'MarkerSize', 15, 'LineWidth', 3);
title('Resultados de Mean Shift');
legend('Cluster 1', 'Cluster 2', 'Centroides');
hold off;
% Función para Mean Shift
function [cluster_centers, assignments] = MeanShiftCluster(data, bandwidth)
 [n, m] = size(data);
 cluster_centers = zeros(0, m);
 assignments = zeros(n, 1);

 % Loop sobre los puntos de datos
 for i = 1:n
 x = data(i, :);
 while true
 % Calcular la distancia euclidiana
 distances = sqrt(sum((data - x).^2, 2)); 
 % Encontrar puntos dentro del ancho de banda
 within_bandwidth = distances <= bandwidth;
 num_within_bandwidth = sum(within_bandwidth);

 % Calcular el nuevo centro como la media de los puntos dentro del ancho de banda
 new_center = sum(data(within_bandwidth, :), 1) / num_within_bandwidth;

 % Si el nuevo centro es igual al centro anterior, detener el bucle
 if norm(new_center - x) < 1e-5
 break;
 end

 x = new_center;
 end

 % Asignar el punto al centro correspondiente
 if isempty(cluster_centers) || ~ismember(x, cluster_centers, 'rows')
 cluster_centers = [cluster_centers; x];
 end
 [~, cluster_index] = ismember(x, cluster_centers, 'rows');
 assignments(i) = cluster_index;
 end
end 
