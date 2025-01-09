# emeliyyat sisteminde istifadeci qovluqlari vardir. Esas ana qovluq bir cox komputerde
# Users adlanir. Hemin users qovlugunun icinde ise istifadecinin alt qovlugu vardir.
# Bu alt qovluq her komputerde ferqlidir. Cunki alt qovlugun adini emeliyyat sistemini 
# qurasdiranda ozumuz adlandiririq.

# Biz hardan bilirik ki, her komputerin istifadeci qovlugunda olan alt qovlugun adi nedir ? Bilmirik.

# Bunun ucun proqram dilinde bele variable-llar movcuddur:
# $HOME, ${USER}, ${HOME}, $USER ve.s 

# Windows emeliiat sisteminde ise bu cur yazila biler:
# %HOMEPATH%, $USERNAME, ${TEMP} ve.s

# expandvars() metodu vasitesi ile, hemin qovluqlari cagirmaq mumkundur.
import os

yol1 = "$HOME"
yol2 = "$USER"
yol3 = "${HOME}"
yol4 = "${USER}"


print(   os.path.expandvars(yol1)   )
print(   os.path.expandvars(yol2)   )
print(   os.path.expandvars(yol3)   )
print(   os.path.expandvars(yol4)   )