docker build -t iss-tracker .

docker stop samplerunning
docker rm samplerunning

docker run --name samplerunning iss-tracker