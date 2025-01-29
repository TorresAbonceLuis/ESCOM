function [strQuestionBack] = getQuestionForQuestion(patientSays)

strQuestionBack = [];
% Check for 'Quién es' keyword
if ((strfind(patientSays, 'quien es')) == 1)
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = '¿Te gustaría saber quién es Michael Jordan?';
        case 2
            strQuestionBack = '¿Has oído hablar de LeBron James?';
        case 3
            strQuestionBack = '¿Conoces a Tim Duncan?';
        otherwise
            strQuestionBack = '¿Qué opinas de Stephen Curry?';
    end
    return
end

% Check for 'Cuál es el' keyword
if ((strfind(patientSays, 'cual es el')) == 1)
    switch floor(1+4*rand(1,1))
        case 1
            strQuestionBack = '¿Sabes cuál es el equipo de los Warriors?';
        case 2
            strQuestionBack = '¿Lo serian los Celtics?';
        case 3
            strQuestionBack = '¿Has escuchado del equipo conocido como Los Spurs?';
        otherwise
            strQuestionBack = '¿Cuál crees que es el equipo de los Lakers?';
    end
    return
end
