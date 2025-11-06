#!/usr/bin/env bash
# usage: scripts/set-image-tag.sh <image:tag>
if [ -z "$1" ]; then
  echo "usage: $0 image:tag"
  exit 1
fi
IMAGE="$1"
sed "s|REPLACE_IMAGE|${IMAGE}|g" k8s/deployment.yaml > k8s/deployment-applied.yaml
kubectl apply -f k8s/deployment-applied.yaml