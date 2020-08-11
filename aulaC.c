#include<stdio.h>
#include<locale.h> // configuração de acentos não remover

int main(){
    setlocale(LC_ALL,"Brasil"); // configuração de acentos não remover do main lembrar de setar chcp no win para 65001
    system("color 0A"); //Texto em verde -  Saudades do Monitor CGA

    printf("teste");

    return 0;

}
