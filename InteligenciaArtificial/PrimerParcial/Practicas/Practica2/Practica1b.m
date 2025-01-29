function main()
    m = mobiledev;
    m.Logging = 1;
    webmap('OpenStreetMap');% abrir el mapa
    grafo = [
        1 , 2      % inicio - a
        1 , 2      % inicio - b
        2 , 3;     % a - b
        2 , 4;     % a - c
        3 , 2;     % b - a 
        3 , 5;     % b - d
        4 , 2;     % c - a
        4 , 5;     % c - d
        4 , 7;     % c - f
        5 , 3;     % d - b
        5 , 4;     % d - c
        5 , 6;     % d - e
        5 , 8;     % d - g
        6 , 5;     % e - d
        6 , 11;    % e - j
        7 , 4;     % f - c
        7 , 8;     % f - g
        7 , 9;     % f - h
        8 , 5;     % g - d
        8 , 7;     % g - f
        8 , 10;    % g - i
        9 , 7;     % h - f
        9 , 10;    % h - i
        10 , 8;    % i - g
        10 , 9;    % i - h
        10 , 11;   % i - j
        11 , 6;    % j - e
        11 , 10;    % j - i
        11 , 12;   % j - destino
    ];
    while true
        latitud = m.Latitude;
        longitud = m.Longitude;
        %latitud = 19.504097;
        %longitud = -99.146262;
        coordenadas = [
            19.504112, -99.146289 % nodo inicio
            19.504201, -99.146386; % nodo a
            19.504061, -99.146128; % nodo b
            19.504434, -99.146257; % nodo c
            19.504299, -99.145984; % nodo d
            19.504232, -99.145817; % nodo e
            19.504682, -99.146143; % nodo f
            19.504555, -99.145863; % nodo g
            19.504940, -99.146000; % nodo h
            19.504810, -99.145729; % nodo i
            19.504744, -99.145563; % nodo j
            19.505379, -99.145240; % Destino
        ];
        wmremove;%quitar la ruta marcada
        nodo_inicio = encontrarNodoMasCercano(latitud, longitud, coordenadas);
        ruta = aEstrella(grafo, coordenadas, nodo_inicio);
        for i = 1:length(ruta) - 1%graficar la ruta
            latitudes = [coordenadas(ruta(i), 1), coordenadas(ruta(i+1), 1)];
            longitudes = [coordenadas(ruta(i), 2), coordenadas(ruta(i+1), 2)];
            wmline(latitudes, longitudes, 'Color', 'magenta');
        end
        wmcenter(latitud, longitud,18)%centrar el mapa
        pause(5);
    end
end

function nodo_mas_cercano = encontrarNodoMasCercano(latitud, longitud, coordenadas)
    distancias = sqrt((coordenadas(:, 1) - latitud).^2 + (coordenadas(:, 2) - longitud).^2);%distancia entre nodo actual y c/nodo
    [~, nodo_mas_cercano] = min(distancias);
end

function camino = aEstrella(mapa, ubicaciones, inicio)
    meta = size(ubicaciones, 1);
    estimacion = @(punto) calcularDistancia(ubicaciones(punto, 1), ubicaciones(punto, 2), ubicaciones(meta, 1), ubicaciones(meta, 2));
    porExplorar = inicio;
    explorados = [];
    costoReal = zeros(size(ubicaciones, 1), 1);
    costoTotal = zeros(size(ubicaciones, 1), 1);
    antecesores = zeros(size(ubicaciones, 1), 1);
    while ~isempty(porExplorar)
        [~, indiceActual] = min(costoTotal(porExplorar));
        puntoActual = porExplorar(indiceActual);
        if puntoActual == meta
            camino = trazarCamino(antecesores, meta);
            return;
        end
        porExplorar(indiceActual) = [];
        explorados(end+1) = puntoActual;
        adyacentes = mapa(mapa(:, 1) == puntoActual, 2);
        for adyacente = adyacentes'
            if ismember(adyacente, explorados)
                continue;
            end
            nuevoCostoReal = costoReal(puntoActual) + calcularDistancia(ubicaciones(puntoActual, 1), ubicaciones(puntoActual, 2), ubicaciones(adyacente, 1), ubicaciones(adyacente, 2));
            if ~ismember(adyacente, porExplorar)
                porExplorar(end+1) = adyacente;
            elseif nuevoCostoReal >= costoReal(adyacente)
                continue;
            end
            costoReal(adyacente) = nuevoCostoReal;
            costoTotal(adyacente) = costoReal(adyacente) + estimacion(adyacente);
            antecesores(adyacente) = puntoActual;
        end
    end
    error('No se encontró un camino');
end

function camino = trazarCamino(antecesores, meta)
    camino = meta;
    while antecesores(camino(1)) ~= 0
        camino = [antecesores(camino(1)); camino];
    end
end

function distancia = calcularDistancia(lat1, lon1, lat2, lon2)
    elipsoide = referenceEllipsoid('WGS84');
    distancia = distance(lat1, lon1, lat2, lon2, elipsoide) * 1000; % Convertir a metros
end