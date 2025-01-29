function [strGreeting] = getGreeting(icase)

if (~exist('icase','var'))
    icase = floor(6*rand(1,1)+1);
end

switch icase
    case 1
        strGreeting = 'Hello, how may I help you?';
    case 2
        strGreeting = 'Greetings. What would you like to talk about?';
    case 3
        strGreeting = 'Good day. Please tell me your problems.';
    case 4
        strGreeting = 'What is on your mind today?';
    case 5
        strGreeting = 'Please begin when you are ready.';
    otherwise
        strGreeting = 'Hello, what is your question?';
end
  
end

