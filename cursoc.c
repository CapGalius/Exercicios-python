#include<stdio.h>
#include <stdlib.h>
#include<locale.h> // configuração de acentos não remover

int main(){
    setlocale(LC_ALL,NULL); // configuração de acentos não remover do main
    system("color A"); //Texto em verde -  Saudades do Monitor CGA

    int idade;
    printf("Qual é a sua idade? ");
    scanf("%d", &idade);
    printf("A sua idade é: %d", idade);

    return 0;

}