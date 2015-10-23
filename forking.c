#include <stdio.h>
#include  <sys/types.h>

int main(){
	pid_t pid1,pid2,pid3,pid4;

	pid1 = fork();
	pid2 = fork();
	pid3 = fork();
	pid4 = fork();

	switch(pid1){
		case -1:
			perror("Error al crear hijo\n");
		case 0:
			printf("Son\n");
			while(1){
				int i=0;}
			break;
		default:
			wait();
			printf("Father\n");
	}switch(pid2){
		case -1:
			perror("Error al crear hijo\n");
		case 0:
			printf("Son\n");
while(1){
                                int i=0;}

			break;
		default:
			wait();
			printf("Father\n");
	}switch(pid3){
		case -1:
			perror("Error al crear hijo\n");
		case 0:
			printf("Son\n");
while(1){
                                int i=0;}

			break;
		default:
			wait();
			printf("Father\n");
	}switch(pid4){
		case -1:
			perror("Error al crear hijo\n");
		case 0:
			printf("Son\n");
while(1){
                                int i=0;}

			break;
		default:
			wait();
			printf("Father\n");
	}
}
