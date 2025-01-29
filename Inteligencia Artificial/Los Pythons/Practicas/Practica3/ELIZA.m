% Define startFig como una variable global
global startFig;

% Crea una nueva figura para la pantalla de inicio
startFig = uifigure('Name', 'Inicio', 'Position', [300 100 800 600]);

% Agrega la imagen de fondo
ax = axes(startFig, 'Position', [0 0 0.25 .5]); % Ajusta el color de fondo a blanco
img = imread('messi.png');
imshow(img, 'Parent', ax);

% Agrega la segunda imagen de fondo
ax2 = axes(startFig, 'Position', [0.5 0 0.5 0.5]); % Ajusta el tamaño y la posición de los ejes
img2 = imread('mbappe.png');
imshow(img2, 'Parent', ax2);

% Agrega las imágenes
logo1_width = 200; % Nuevo ancho para logo1
logo1_height = 160; % Nuevo altura para logo1
logo1 = uiimage(startFig, 'Position', [10 460 logo1_width logo1_height]);
logo1.ImageSource = 'logo1.png'; % Cambia 'logo1.png' a la ruta de tu imagen

logo2 = uiimage(startFig, 'Position', [640 480 150 120]);
logo2.ImageSource = 'logo2.png'; % Cambia 'logo2.png' a la ruta de tu imagen

% Calcula la posición x para centrar logo3
logo3_width = 200; % Ancho para logo3
logo3_height = 160; % Altura para logo3
logo3_x_position = (startFig.Position(3) - logo3_width) / 2;

logo3 = uiimage(startFig, 'Position', [logo3_x_position 460 logo3_width logo3_height]);
logo3.ImageSource = 'logo3.png'; % Cambia 'logo3.png' a la ruta de tu imagen

% Resto del código...

% Agregar la información
info = uilabel(startFig, 'Position', [200 300 400 300]);
info.Text = sprintf('\n\n\nInstituto Politecnico Nacional (IPN)\nEscuela Superior de Computo (ESCOM)\nPlayer Prophet\nTorres Abonce Luis Miguel\nRyan Nathanael Cruz Barragan\nJoshua Levi Rodriguez Vazquez');
info.HorizontalAlignment = 'center';
info.FontSize = 18; % Aumenta el tamaño de la fuente

% Crea un botón para continuar a la figura original
continueButton = uibutton(startFig, 'push', 'Position', [350 200 100 50]);
continueButton.Text = 'Continuar';
continueButton.BackgroundColor = [0 0 1]; % Establece el color de fondo a azul
continueButton.FontColor = [1 1 1]; % Establece el color de la fuente a blanco
continueButton.ButtonPushedFcn = @(btn,event) switchToOriginalFig();

% Crea un botón para la ayuda en la figura principal
helpButton = uibutton(startFig, 'push', 'Position', [350 100 100 50]);
helpButton.Text = 'Ayuda';
helpButton.ButtonPushedFcn = @(btn,event) showHelp();

% Función para mostrar la ayuda
function showHelp()
    % Crea una nueva figura para la ayuda
    helpFig = uifigure('Name', 'Ayuda', 'Position', [300 100 800 600]);
    
    % Agrega el texto de ayuda
    helpText = uilabel(helpFig, 'Position', [50 400 700 150]);
    helpText.Text = sprintf(['Este programa es una implementación de ELIZA, un chatbot diseñado para simular una conversación con una \npersona, que intentara decirte sobre que jugador estas preguntando.\n\n-Para empezar el programa deberas de presionar el boton de "Continuar".\n-Posteriormente se te mostrara otro boton con el texto "Empezar", presionalo para empezar.\n-Contestar a todas las preguntas dentro del cuadro de texto y presionar el boton "Enviar".\n-Cuando contestes la ultima pregunta se te mostrara el jugador en el que penaste.\n Esta es una tabla sobre cuales son los datos de ejemplo con los que puedes contestar a las preguntas:']);
    helpText.HorizontalAlignment = 'center';
    helpText.FontSize = 14; % Ajusta el tamaño de la fuente

    % Crea una tabla
    tdata = {'Paris Saint-Germain', 'Delantero', 'Francia', 'Nike', 22, '1.78'; 
             'Barcelona', 'Delantero', 'Argentina', 'Nike', 34, '1.70';
             'Manchester United', 'Delantero', 'Portugal', 'Adidas', 36, '1.87';
             'Liverpool', 'Delantero', 'Egipto', 'New Balance', 29, '1.75';
             'Bayern Munich', 'Delantero', 'Polonia', 'Adidas', 33, '1.85';
             'Real Madrid', 'Mediocampista', 'Alemania', 'Adidas', 31, '1.83';
             'Manchester City', 'Defensa', 'Inglaterra', 'Puma', 27, '1.88'};
    columnname = {'Equipo', 'Posicion', 'Origen', 'Patrocinador', 'Edad', 'Estatura'};
    columnformat = {'char', 'char', 'char', 'char', 'numeric', 'numeric'};
    t = uitable(helpFig, 'Data', tdata, 'ColumnName', columnname, 'ColumnFormat', columnformat, 'Position', [50 200 700 150]);
end

% Función para cambiar a la figura original
function switchToOriginalFig()
    % Accede a startFig desde el espacio de trabajo global
    global startFig;
    
    % Cierra la figura de inicio
    close(startFig);
    
    % Lee los datos del archivo .xlsx
    data = readtable('ChatData.xlsx', 'VariableNamingRule', 'preserve');
    % Inicializa las puntuaciones y las preguntas
    puntuaciones = zeros(height(data), 1);
    preguntas = {'¿En qué equipo juega? ', '¿En qué posición juega? ', '¿Cuál es su país de origen? ', '¿Quién es su patrocinador? ', '¿Qué edad tiene? ', '¿Qué estatura tiene?(metros) '};
    iPregunta = 1;

    % Crea una figura de la interfaz
    fig = uifigure('Name', 'ELIZA', 'Position', [500 200 400 400]);

    % Crea un botón para empezar
    startButton = uibutton(fig, 'push', 'Position', [150 200 100 50]);
    startButton.Text = 'Empezar';
    startButton.ButtonPushedFcn = @startGame;

    % Crea un panel para las preguntas y respuestas
    qaPanel = uipanel(fig, 'Position', [0 0 400 400], 'Visible', 'off');
    questionLabel = uilabel(qaPanel, 'Position', [50 350 300 30]);
    answerField = uieditfield(qaPanel, 'Position', [50 300 300 30]);

    % Crea un botón para enviar la respuesta
    submitButton = uibutton(qaPanel, 'Position', [150 250 100 30], 'Text', 'Enviar');
    submitButton.ButtonPushedFcn = @submitAnswer;

    % Función para iniciar el juego
    function startGame(src, event)
        qaPanel.Visible = 'on';
        helpButton.Visible = 'off'; % Oculta el botón de ayuda
        questionLabel.Text = preguntas{iPregunta};
    end

    % Inicializa las puntuaciones y las preguntas
    puntuaciones = zeros(height(data), 1);
    preguntas = {'¿En qué equipo juega? ', '¿En qué posición juega? ', '¿Cuál es su país de origen? ', '¿Quién es su patrocinador? ', '¿Qué edad tiene? ', '¿Qué estatura tiene? '};
    columnas = {'Equipo', 'Posición', 'Origen', 'Patrocinador', 'Edad', 'Estatura'}; % Asegúrate de que estos son los nombres correctos de las columnas
    iPregunta = 1;
    
    % Función para enviar la respuesta
    function submitAnswer(src, event)
        % Incrementa las puntuaciones basado en la respuesta del usuario
        respuesta = lower(answerField.Value);
        for i = 1:height(data)
            if strcmpi(respuesta, lower(table2array(data(i, columnas{iPregunta}))))
                puntuaciones(i) = puntuaciones(i) + 1;
            end
        end
    
        % Avanza a la siguiente pregunta o termina el juego
        iPregunta = iPregunta + 1;
        if iPregunta <= numel(preguntas)
            questionLabel.Text = preguntas{iPregunta};
            answerField.Value = '';
        else
            % Encuentra el jugador con la puntuación más alta
            maxScore = max(puntuaciones);
            matchingPlayers = find(puntuaciones == maxScore);
            
            if isempty(matchingPlayers)
                % No se encontraron coincidencias
                uialert(fig, 'No se pudo encontrar una coincidencia.', 'Fin del Juego', 'CloseFcn', @returnToStart);
            elseif numel(matchingPlayers) > 1
                % Más de un jugador coincide
                uialert(fig, 'Se encontró más de un jugador que coincide.', 'Fin del Juego', 'CloseFcn', @returnToStart);
            else
                % Un jugador coincide
                jugador = data(matchingPlayers(1), :);
                uialert(fig, ['El jugador es ' table2array(jugador(1, 'Nombre')) '.'], 'Fin del Juego', 'CloseFcn', @returnToStart);
            end
        end
    end
    
    % Función para volver a la pantalla de inicio
    function returnToStart(src, event)
        close(fig);
    end
end