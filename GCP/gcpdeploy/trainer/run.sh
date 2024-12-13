# Define the image URI and model version
IMAGE_NAME="gcr.io/striped-graph-440017-d7/mpg"
MODEL_VERSION="v2"  
ENDPOINT_NAME="model-endpoint-v2"

# Build the Docker image with the specified version tag
docker build ./ -t ${IMAGE_NAME}:${MODEL_VERSION} -f trainer/Dockerfile

# Push the Docker image with the version tag
docker push ${IMAGE_NAME}:${MODEL_VERSION}

# Tag the image as 'latest'
docker tag ${IMAGE_NAME}:${MODEL_VERSION} ${IMAGE_NAME}:latest

# Push the Docker image with the 'latest' tag
docker push ${IMAGE_NAME}:latest

# Retrieve the image digest for the versioned image
DIGEST=$(gcloud container images describe ${IMAGE_NAME}:${MODEL_VERSION} --format="value(image_summary.fully_qualified_digest)")

echo ------++++++++++
echo $DIGEST
echo ------++++++++++

# Ensure the digest was retrieved successfully
if [ -z "$DIGEST" ]; then
  echo "Error: Failed to retrieve image digest. Ensure the image was pushed successfully."
  exit 1
fi

    
# Upload the model to Vertex AI
MODEL_ID=$(gcloud ai models upload \
    --region=us-east1 \
    --display-name=model-${MODEL_VERSION} \
    --artifact-uri=gs://stock_price_prediction_dataset/model_checkpoints/ \
    --container-image-uri=${DIGEST} \
    --format="value(name)")


# Confirm the upload
if [ $? -eq 0 ] && [ -n "$MODEL_ID" ]; then
  echo "Model uploaded successfully to Vertex AI with ID: $MODEL_ID"
else
  echo "Error: Model upload to Vertex AI failed."
  exit 1
fi

# Create endpoint if it does not already exist
ENDPOINT_ID=$(gcloud ai endpoints list \
    --region=us-east1 \
    --filter="display_name:${ENDPOINT_NAME}" \
    --format="value(name)")

if [ -z "$ENDPOINT_ID" ]; then
  echo "Creating new endpoint: ${ENDPOINT_NAME}"
  ENDPOINT_ID=$(gcloud ai endpoints create \
      --region=us-east1 \
      --display-name=${ENDPOINT_NAME} \
      --format="value(name)")
else
  echo "Using existing endpoint: ${ENDPOINT_NAME}"
fi

echo ------++++++++++------
echo $MODEL_ID
echo ------++++++++++------
echo $ENDPOINT_ID
echo ------++++++++++------

# Deploy model to the endpoint and set traffic split
gcloud ai endpoints deploy-model \
    $ENDPOINT_ID \
    --region=us-east1 \
    --model=$MODEL_ID \
    --display-name=model-${MODEL_VERSION} \
    --machine-type=n1-standard-2 \
    --endpoint=${ENDPOINT_ID} \
    --traffic-split="0=100"

# Confirm the deployment
if [ $? -eq 0 ]; then
  echo "Model deployed successfully to the endpoint."
else
  echo "Error: Model deployment failed."
  exit 1
fi
