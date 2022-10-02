## Build:
`
docker build -t <image-name> .
`
e.g 
`
docker build -t swetha-assignment-2 .
`

## Run:
`
docker run  -p 8888:8888 -v <local-path>:/notebooks <image-name>
`
e.g
`
docker run  -p 8888:8888 -v "$(pwd)"/notebooks:/notebooks swetha-assignment-2
`

