#include <stdio.h>

#include <stdlib.h>

#include <locale.h>

 

/*

Crie um algoritmo que leia o nome,

a idade e o sexo de 10 pessoas.

Imprima o nome das pessoas que forem do sexo feminino

 e tiverem mais de 28 anos. Em C.

*/

 

#define tam 10 //Tamanho do vetor. Pode mudar de acordo com a necessidade de mais ou menos pessoas.

 

int main()

{

       setlocale(LC_ALL,NULL); //para aceitar caracteres do português

       system("color A"); //Texto em verde -  Saudades do Monitor CGA

      

       char nome[tam][100]; // Char em Array 2x2 para servir como se fosse tabela do excel.

       int idade[tam],i,sexo[tam];

       printf("Entre com 10 nomes, gêneros e idades de pessoas: ");    
       
       system("PAUSE");

       for (i=0;i<tam;i++)

       {

             printf("Entrar com o nome: ");

             scanf("%s", &nome[i]);

      

             printf("Entrar com 1 para Masc. e 2 para Fem.: ");

             scanf("%d", &sexo[i]);

      

             printf("Entrar com a idade: ");

             scanf("%d", &idade[i]);

       }

        

       for (i=0;i<tam;i++)

       {     

       if(sexo[i] == 2 && idade[i]>28)

             printf("Mulheres maiores de 28 anos cadastradas:  %s\n",  nome[i]);

       else

             i=1;

             printf("\nNão há mulheres com mais de 28 anos cadastradas.\n");

             break;

       }

      

       system("PAUSE");

       return 0;

}