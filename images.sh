#!/bin/bash
set -x
set -u
set -e
IMAGE_NAME= YOUR IMAGE NAME
#docker images | tac | grep "$IMAGE_NAME" | awk '{print $3}' | xargs docker rmi
docker build -t $IMAGE_NAME .
x=1
docker history -q "${IMAGE_NAME}:latest" | tac
for id in $(docker history -q "${IMAGE_NAME}:latest" | tac)
do
	docker tag -f "${id}" "${IMAGE_NAME}:step_$x"
	((x++))
done
docker push "${IMAGE_NAME}"
