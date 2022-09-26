##Build:

docker build -t <image-name> .

##Run:

docker run <image-name>

(Default Entry point prints the contents of company.txt)

##Access Container:

docker run -it --entrypoint /bin/bash <image-name>

After running the command, you are inside the container. You can start
using it as a normal command line. e.g ls
