function [strReply] = You2Me(patientSays)

strReply = [];
flagReplyFinished = false;

idxCricket = strfind(patientSays, 'tu ');
if (idxCricket > 1)
    strLeft = patientSays(1:idxCricket - 1);
    strRight = patientSays(idxCricket+7:end);
    strReply = [strLeft 'yo ' strRight];
end

idxCricket = strfind(patientSays, 'tu no');
if (idxCricket > 1)
    strLeft = patientSays(1:idxCricket - 1);
    strRight = patientSays(idxCricket+7:end);
    strReply = [strLeft 'yo no' strRight];
end

idxCricket = strfind(patientSays, 'y''o');
if (idxCricket > 1)
    strLeft = patientSays(1: idxCricket - 1);
    strRight = patientSays(idxCricket+4:end);
    strReply = [strLeft 'tu' strRight];
    flagReplyFinished = true;
end

idxCricket = strfind(patientSays, 'tu');
if ((idxCricket > 4) & ~flagReplyFinished)
    strLeft = patientSays(1: idxCricket - 1);
    strRight = patientSays(idxCricket+6:end);
    strReply = [strLeft 'yo' strRight];
end
flagReplyFinished = false;

idxCricket = strfind(patientSays, ' tu ');
if (idxCricket > 1)
    strLeft = patientSays(1: idxCricket - 1);
    strRight = patientSays(idxCricket+3:end);
    strReply = [strLeft ' yo ' strRight];
    flagReplyFinished = true;
end

idxCricket = strfind(patientSays, ' yo ');
if ((idxCricket > 3) & ~flagReplyFinished)
    strLeft = patientSays(1: idxCricket - 1);
    strRight = patientSays(idxCricket+2:end);
    strReply = [strLeft ' tu ' strRight];
end

idxCricket = strfind(patientSays, ' mio ');
if (idxCricket > 3)
    strLeft = patientSays(1: idxCricket - 1);
    strRight = patientSays(idxCricket+2:end);
    strReply = [strLeft ' tu ' strRight];
end

if (isempty(strReply))
    strReply= patientSays;
end

end
