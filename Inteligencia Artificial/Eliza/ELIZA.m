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

fprintf(1,'Bienvenido a Eliza\n');
fprintf(1,'Eliza es un experto en baloncesto.\n');
fprintf(1,'Este programa te brindará consejos y análisis sobre el juego.\n');
fprintf(1,'Ingresa tus consultas o comentarios en el prompt.\n');
fprintf(1,'Escribe "adiós" para finalizar tu sesión.\n\n');

prompt = getGreeting(); 
patientSays = input(['ELIZA> ' prompt '\n  YOU> '],'s');

while (flagGo)
    
    [prompt] = getTriggeredReply(patientSays);
    if (isempty(prompt))
        [prompt] = getQuestionForQuestion(patientSays);
    end
    if (isempty(prompt))
        [prompt] = fillDeadAirtime();
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
    patientSays = lower(input(['ELIZA> ' prompt '\n  Tu> '],'s'));
    
    if (contains(patientSays,'adios'))
        flagGo = false;
    end
    
end

disp(['Nos vemos Luego!']);
