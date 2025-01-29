%% *ELIZA*
%% *purpose*
%  This is an implementation of ELIZA, "The Computer Psychiatrist"
%  an early artificial intelligence program
%  Original ELIZA was written by Joseph Weizenbaum
%% *reference*
%  The basic program (.BAS) included in this distribution was from an early
%  book about artificial intelligence.  The programs have been elaborated
%  on a little bit.
%  There's a pretty good Wikipedia page about it: 
%  https://en.wikipedia.org/wiki/ELIZA
%% *history*
%  WHO   WHEN       WHY
%  ----  ---------- -----------------------------------------------------
%  mnoah 03/09/2019 To share an old AI program with the matlab community.
%% *go*
flagGo = true;

fprintf(1,'Bienvenido a ELIZA\n');
fprintf(1,'Eliza es una experta en basketball.\n');
% fprintf(1,'El programa original fue descrito por Joseph Weizenbaum en 1966.\n');
fprintf(1,'Eres un aficionado. Ingrese su cuadro de diálogo cuando se le solicite.\n');
fprintf(1,'Ingresa ''adios'' para terminar la sesion\n\n');

prompt = getGreeting();
patientSays = input(['ELIZA> ' prompt '\n  TU> '],'s');

while (flagGo)
    
    [prompt] = getTriggeredReply(patientSays);%primero revisa el xml
    if (isempty(prompt))%si el xml esta vacio
        [prompt] = getQuestionForQuestion(patientSays);%obtiene la respuesta de gqfq
    end
    if (isempty(prompt))%si aun no se obteniene respuesta
        [prompt] = fillDeadAirtime();%se intenta llenar con filldead
    end
    
    while (length(prompt) > 50)
        idxSpace = strfind(prompt,' ');
        idxSpace(idxSpace<50) = [];
        if (~isempty(idxSpace))
            disp(['ELIZA> ' prompt(1:idxSpace(1))]);
            prompt = prompt(idxSpace(1)+1:end);
        else
        end
    end
    patientSays = lower(input(['ELIZA> ' prompt '\n  TU> '],'s'));
    
    if (contains(patientSays,'adios'))
        flagGo = false;
    end
    
end

disp(['Hasta luego!']);
