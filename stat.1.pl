.\" 1999 PTM Przemek Borys
.\" Update: Robert Luberda <robert@debian.org>, Aug 2002, fileutils 4.1.10
.\" $Id$
.TH STAT "1" "lipiec 2002" "stat (fileutils) 4.1.10" "polecenia u�ytkownika"
.SH NAZWA
stat \- drukuj status pliku lub systemu plik�w
.SH SK�ADNIA
.B stat
[\fIOPCJA\fR] \fIPLIK\fR...
.SH OPIS
.\" Add any additional description here
.PP
Wy�wietla status pliku lub systemu plik�w
.TP
\fB\-f\fR, \fB\-\-filesystem\fR
wy�wietla informacje o stanie systemu plik�w, a nie o stanie pliku
.TP
\fB\-c\fR  \fB\-\-format\fR=\fIFORMAT\fR
u�ywa podanego FORMATU zamiast formatu domy�lnego
.TP
\fB\-l\fR, \fB\-\-dereference\fR
pod��a za linkami
.TP
\fB\-t\fR, \fB\-\-terse\fR
wy�wietla informacje w zwi�z�ej postaci
.TP
\fB\-\-help\fR
wy�wietla pomoc i ko�czy dzia�anie
.TP
\fB\-\-version\fR
wy�wietla informacje o wersji i ko�czy dzia�anie
.PP
Poprawne sekwencje formatu dla plik�w (je�eli nie podano opcji \fB\-\-filesystem\fR):  
.IP
.\" doda�em pocz�tkowe spacje w liniach poni�ej - dla zwi�kszenia czytelno�ci (RL)
 %A - prawa dost�pu w formie czytelnej dla cz�owieka
 %a - prawa dost�pu �semkowo
 %b - liczba zaalokowanych blok�w
 %D - numer urz�dzenia szesnastkowo
 %d - numer urz�dzenia w systemie dziesi�tnym
 %F - typ pliku
 %f - tryb pliku szesnastkowo
 %G - nazwa grupy, kt�ra jest w�a�cicielem pliku
 %g - identyfikator grupy, kt�ra jest w�a�cicielem pliku
 %h - liczba twardych dowi�za�
 %i - numer w�z�a (inode)
 %N - nazwa pliku w apostrofach ze wskazaniem link�w symbol.
 %n - nazwa pliku
 %o - rozmiar bloku wej�cia/wyj�cia
 %s - ca�kowity rozmiar w bajtach
 %T - poboczny (minor) typ urz�dzenia szesnastkowo
 %t - g��wny (major) typ urz�dzenia szesnastkowo
 %U - nazwa w�a�ciciela pliku
 %u - identyfikator w�a�ciciela pliku
 %X - czas ostatniego dost�pu podany jako liczba sekund od epoki
 %x - czas ostatniego dost�pu
 %Y - czas ostatniej modyfikacji jako liczba sekund od epoki
 %y - czas ostatniej modyfikacji
 %Z - czas ostatniej zmiany podany jako liczba sekund od epoki
 %z - czas ostatniej zmiany
.PP
Poprawne sekwencje formatu dla system�w plik�w:
.IP
 %a - liczba wolnych blok�w dost�pnych dla nie-administrator�w
 %b - ca�kowita liczba blok�w danych w systemie plik�w
 %c - ca�kowita liczba w�z��w w systemie plik�w
 %d - liczba wolnych w�z��w w systemie plik�w
 %f - liczba wolnych blok�w w systemie plik�w
 %i - identyfikator systemu plik�w szesnastkowo
 %l - maksymalna d�ugo�� nazw plik�w
 %n - nazwa pliku
 %s - optymalny rozmiar bloku przy transferze
 %T - typ w formie czytelnej dla cz�owieka
 %t - typ szesnastkowo
.SH AUTOR
Napisane przez Michaela Meskesa.
.SH "ZG�ASZANIE B��D�W"
Prosimy zg�asza� b��dy do <bug-fileutils@gnu.org>.
.SH PRAWA AUTORSKIE
Copyright \(co 2002 Free Software Foundation, Inc.
.br
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
.SH "ZOBACZ TAK�E"
Pe�na dokumentacja programu
.B stat
jest utrzymywana w postaci podr�cznika texinfo. Je�eli programy
.B info 
i
.B stat
zosta�y poprawnie zainstalowane, to za pomoc� polecenia
.IP
.B info stat
.PP
mo�na uzyska� dost�p do pe�nej wersji podr�cznika.