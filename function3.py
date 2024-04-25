def length_string (a)
 if len(a) < 3
return a
elif a[-3] == 'ing'
return a+'ily'
else
return a+'ing'
