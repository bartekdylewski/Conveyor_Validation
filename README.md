# Conveyor_Validation
 app made to validate orientation of cargo in a robotic system palletizing line

 input info from controller:
 - size of cargo
 - count of cargo
 - orientation of cargo

  output info to controller:
 - correctness count 0-100
 - diagnostic info: size, position in relation to conveyor
 - is the cargo flipped on its side?

 output dependent on:
 - count of cargo
 - orientation of cargo
 - position in relation to conveyor
 - is cargo flipped on its side?

Challenge description in Polish:
"Zadanie polega na opracowaniu systemu, złożonego z odpowiednio dobranych czujników (jak np. Intel RealSense Depth Camera D435) oraz współpracującego z nimi oprogramowania, działającego na komputerze z systemem operacyjnym Windows lub Linux.
Oprogramowanie to na podstawie danych z jednego lub więcej czujników, będzie w stanie
zweryfikować, czy układ ładunków na przenośniku kompletacji opakowań w zrobotyzowanej
linii paletyzacji jest zgodny z zadanym wzorem. Kompletacja opakowań przed pobraniem przez robota polega na zebraniu określonej liczby ładunków (np. kartonów) na przenośniku,
przy czym istotna jest ilość ładunków w grupie, ich orientacja (niektóre z nich mogą być
obróco
ne o 90 stopni) oraz pozycja całej grupy względem konstrukcji przenośnika. Zakładamy, że sterownik PLC linii paletyzacji będzie wysyłał do systemu kontrolnego informacje o wymiarach ładunku, ilości ładunków w grupie (rzędzie) i ich orientacji (tj. czy są obrócone o 90 stopni, czy nie), a system będzie odsyłał wartość liczbową w zakresie np.0…100, pokazującą na ile to, co widzi na przenośniku jest zgodne z danymi otrzymanymi
z PLC (100 oznacza idealną zgodność) plus informacje diagnostyczne, takie jak zmierzone
gabaryty i pozycja grupy ładunków na przenośniku. Wykrywane powinny być również
przypadki, gdy ładunek jest przewrócony na bok. Przykładowo, jeśli formujemy grupę 3 ładunków, z których pierwsze dwa są obrócone o 90 stopni, to prawidłowy układ ładunków na przenośniku będzie wyglądał następująco: Gdyby jednak z pewnych przyczyn ostatni karton został niepotrzebnie obrócony, to układ będzie wyglądał następująco i należy go sklasyfikować jako nieprawidłowy: 
"