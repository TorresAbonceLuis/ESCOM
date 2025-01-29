function [NewReply] = fillDeadAirtime()

% No keywords found
switch floor(1+8*rand(1,1))
    case 1
        NewReply = 'Continua con el debate:';
    case 2
        NewReply = 'Entiendo. Por favor, continúa.';
    case 3
        NewReply = 'No estoy seguro de entenderte completamente. ¿Puedes hacer una analogía?';
    case 4
        NewReply = 'Ahora, por favor, aclárate.';
    case 5
        NewReply = '¿Puedes expandirte más sobre eso?';
    case 6
        NewReply = ['Eso es bastante interesante. ' ...
            'Como dijo Michael Jordan: "He fallado más de 9000 tiros en mi carrera. ' ...
            'He perdido casi 300 juegos. 26 veces, se me ha confiado tomar el ' ...
            'tiro ganador y he fallado. He fracasado una y otra vez en mi vida. ' ...
            'Y es por eso que tengo éxito". ¿Hay algún parecido con lo que estás diciendo?'];
    case 7
        NewReply = '¿Estás de acuerdo con eso?';
    otherwise
        NewReply = '¿Qué te sugiere eso?';
end

end


