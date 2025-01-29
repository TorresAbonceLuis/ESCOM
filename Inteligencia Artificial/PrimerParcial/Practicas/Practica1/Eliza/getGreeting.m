function [strGreeting] = getGreeting(icase)

if (~exist('icase','var'))
    icase = floor(6*rand(1,1)+1);
end

switch icase
    case 1
        strGreeting = '¡Hola! ¿En qué puedo ayudarte relacionado con el baloncesto?';
    case 2
        strGreeting = 'Saludos. ¿Qué te gustaría discutir sobre el juego?';
    case 3
        strGreeting = 'Buen día. Cuéntame sobre tus problemas en la cancha.';
    case 4
        strGreeting = '¿Qué te preocupa hoy en el mundo del baloncesto?';
    case 5
        strGreeting = 'Por favor, comienza cuando estés listo para hablar de baloncesto.';
    otherwise
        strGreeting = '¡Hola! ¿Cuál es tu pregunta sobre el baloncesto?';
end
  
end

