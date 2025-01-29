% Generar datos sintéticos
rng(1); % Para reproducibilidad
n = 100; % Número de muestras por clase
X = [randn(n, 2) + 1; randn(n, 2) - 1]; % Características
y = [ones(n, 1); zeros(n, 1)]; % Etiquetas: 1 y 0

% Visualizar los datos
figure;
gscatter(X(:,1), X(:,2), y, 'rb', 'xo');
xlabel('Característica 1');
ylabel('Característica 2');
title('Datos sintéticos para Naive Bayes');
legend('Clase 1', 'Clase 0');

% Entrenar el modelo Naive Bayes
naiveBayesModel = fitcnb(X, y);

% Mostrar el modelo entrenado
disp(naiveBayesModel);

% Predecir las etiquetas
predicciones = predict(naiveBayesModel, X);

% Evaluar la precisión del modelo
precision = mean(predicciones == y);
fprintf('Precisión del modelo: %.2f%%\n', precision * 100);

% Visualizar las predicciones
d = 0.02; % Densidad de la malla
[x1Grid, x2Grid] = meshgrid(min(X(:,1)):d:max(X(:,1)), min(X(:,2)):d:max(X(:,2)));
xGrid = [x1Grid(:), x2Grid(:)];
prediccionesGrid = predict(naiveBayesModel, xGrid);

% Visualizar la frontera de decisión
figure;
gscatter(X(:,1), X(:,2), y, 'rb', 'xo');
hold on;
% Dibuja las predicciones de la malla con scatter
scatter(xGrid(:,1), xGrid(:,2), 10, prediccionesGrid, 'filled', 'MarkerFaceAlpha', 0.1);
xlabel('Característica 1');
ylabel('Característica 2');
title('Naive Bayes con frontera de decisión');
legend('Clase 1', 'Clase 0', 'Ubicaciones predichas');
hold off;