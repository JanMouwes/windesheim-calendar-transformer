Teachers giving this class:
% for teacher in teachers:
    - ${teacher}
% endfor
% if group_code is not "":

Group code: ${group_code}
% endif
% if subject:
    %if subject.name is not "":
Subject name: ${subject.name}
    %endif
    % if subject.code is not "":
Subject code: ${subject.code}
    % endif
% endif
