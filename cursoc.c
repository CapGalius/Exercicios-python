#include<stdio.h>
#include <stdlib.h>
#include<locale.h> // configura��o de acentos n�o remover

int main(){
    setlocale(LC_ALL,""); // configura��o de acentos n�o remover do main
    system("color A"); //Texto em verde -  Saudades do Monitor CGA

    int idade;
    printf("Qual � a sua idade? ");
    scanf("%d", &idade);
    printf("A sua idade �: %d", idade);

    return 0;

}
