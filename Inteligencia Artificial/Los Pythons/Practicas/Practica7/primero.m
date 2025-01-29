% Generar datos sintéticos
rng(0); % Para reproducibilidad
n = 100; % Número de muestras
X = [randn(n, 2) + 1; randn(n, 2) - 1]; % Características
y = [ones(n, 1); zeros(n, 1)]; % Etiquetas
% Visualizar los datos
figure;
gscatter(X(:,1), X(:,2), y, 'rb', 'xo');
xlabel('Característica 1');
ylabel('Característica 2');
title('Datos sintéticos para regresión logística');

% Convertir los datos a una tabla
data = array2table(X, 'VariableNames', {'Feature1', 'Feature2'});
data.Response = y;
% Ajustar el modelo de regresión logística
model = fitglm(data, 'Response ~ Feature1 + Feature2', 'Distribution', 'binomial');
% Mostrar el resumen del modelo
disp(model);
% Predecir las probabilidades
probabilidades = predict(model, data);
% Convertir probabilidades a etiquetas (0 o 1) con un umbral de 0.5
predicciones = round(probabilidades);
% Evaluar la precisión del modelo
precision = mean(predicciones == y);
fprintf('Precisión del modelo: %.2f%%\n', precision * 100);

% Visualizar las predicciones
figure;
gscatter(X(:,1), X(:,2), predicciones, 'rb', 'xo');
xlabel('Característica 1');
ylabel('Característica 2');
title('Predicciones del modelo de regresión logística');