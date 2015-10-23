/* malloc example: random string generator*/
#include <stdio.h>      /* printf, scanf, NULL */
#include <stdlib.h>     /* malloc, free, rand */

int main ()
{
	fork();
	fork();
	fork();
  int i,n;

  char * buffer;

  printf ("How long do you want the string? ");
  scanf ("%d", &i);
  i= i * 1000 * 1000 * 1000;
  buffer = (char*) malloc (i+1);
 

  for (n=0; n<i; n++)
    buffer[n]=rand()%26+'a';
  buffer[i]='\0';

  getchar();
  getchar();
  free (buffer);

  return 0;
}
