#include<stdio.h>
#include<locale.h> // configuração de acentos não remover

int main(){
    setlocale(LC_ALL,NULL); // configuração de acentos não remover do main
    
    int idade;
    printf("Qual é a sua idade? ");
    scanf("%d", &idade);

    return 0;

}