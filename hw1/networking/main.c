#include <sys/types.h>
#include <sys/socket.h> 
#include <netinet/in.h>

int socket_desc;

socket_desc=socket(AF_INET,SOCK_STREAM,0);
if (socket_desc==-1){
	perror("Create socket");
}

// Setup socket

struct sockaddr_in address;

/* type of socket created in socket() */
address.sin_family = AF_INET;
address.sin_addr.s_addr = INADDR_ANY;
/* 7000 is the port to use for connections */
address.sin_port = htons(7000);
/* bind the socket to the port specified above */
bind(socket_desc,(struct sockaddr *)&address,sizeof(address));
