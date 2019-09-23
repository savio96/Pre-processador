#include <stdio.h>
#include <stdlib.h>

#define con 5
#define aux 10
//dfedvfwevwevwevbwe
int main(){

    int dia1, hora1, min1, seg1;
    int d1, h1, m1, s1;
    int dia2, hora2, min2, seg2;
    int d2, h2, m2, s2;
    int total,total1,total2;
    int dia, hora, min, seg;
    int d, h, m, s;
    int aux,aux;

    scanf("Dia %d\n", &d1);
    scanf("%d : %d : %d\n",&h1, &m1, &s1);


    scanf("Dia %d\n",&d2);
    scanf("%d : %d : %d",&h2, &m2, &s2);
    dia1 = d1 * 24 * 60 * 60;
    hora1 = h1 * 60 * 60;
    min1 = m1 * 60;
    seg1 = s1;
    total1 = dia1 + hora1 + min1 + seg1;

    dia2 = d2 * 24 * 60 * 60;
    hora2 = h2 * 60 * 60;
    min2 = m2 * 60;
    seg2 = s2;
    total2 = (dia2) + (hora2 + min2 + seg2);

    total = total2 - total1;

    dia = total / 86400;
    hora = ((total) - (dia * 86400)) / 3600;
    min = ((total) - (dia * 86400) - (hora * 3600)) / 60;
    seg = ((total) - (dia * 86400) - (hora * 3600) - (min * 60));
    printf("%d dia(s)\n", dia);
    printf("%d hora(s)\n", hora);
    printf("%d minuto(s)\n", min);
    printf("%d segundo(s)\n", seg);
    aux2=con+aux;
    return 0;
}