#include <stdio.h>



int main()

{

  struct Pet {

    char nome[30];

    int idade;

    char raca[50];

  };

   

  int i, j;

  struct Pet novo[3];

  struct Pet aux;

   

  for(i = 0; i < 3; i++){

    printf("Digite o nome do pet: ");

    fgets(novo[i].nome, 30, stdin);

    printf("Digite a idade do pet: ");

    scanf("%d", &novo[i].idade);

    while (getchar() != '\n');  

    printf("Digite a raça:");

    fgets(novo[i].raca, 50, stdin);

     

  }

   

  for (i= 0; i < 3; i++){

    for (j= i+1; j<3; j++ ){

      if (novo[i].idade > novo[j].idade){

        aux = novo[i];

        novo[i] = novo[j];

        novo[j] = aux;

      }

    }

  }

   

   

  for (i=0; i < 3; i++){

    printf("O nome é %s", novo[i].nome);

    printf("A idade é %d \n ", novo[i].idade);

    printf("A raça é %s \n", novo[i].raca);

  }



  return 0;

}