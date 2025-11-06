```bash
#!/usr/bin/env bash
set -euo pipefail

NAMESPACE=mini-anomaly
MANIFEST_DIR="k8s"

# Expect 1 arg: image (e.g. myrepo/mini-anomaly:sha123)
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <image>"
  exit 2
fi
IMAGE="$1"

kubectl apply -f ${MANIFEST_DIR}/namespace.yaml

# Replace placeholder image in deployment and apply
kubectl -n ${NAMESPACE} set image deployment/mini-anomaly-deployment mini-anomaly=${IMAGE} --record || (
  # fallback: patch with full deployment manifest if set-image failed
  echo "set-image failed, applying deployment manifest with placeholder replacement"
  sed "s|REPLACE_IMAGE|${IMAGE}|g" ${MANIFEST_DIR}/deployment.yaml | kubectl apply -f -
)

# Apply service + ingress
kubectl apply -f ${MANIFEST_DIR}/service.yaml
if [ -f ${MANIFEST_DIR}/ingress.yaml ]; then
  kubectl apply -f ${MANIFEST_DIR}/ingress.yaml || true
fi

kubectl rollout status deployment/mini-anomaly-deployment -n ${NAMESPACE}

echo "Deployed image: ${IMAGE} to namespace: ${NAMESPACE}"