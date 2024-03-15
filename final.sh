destination_dir="service-result"
source_folder="/home/doc-bd-a1/service-result"

# Check if the destination directory exists; if not, create it
if [ ! -d "$destination_dir" ]; then
  mkdir -p "$destination_dir"
fi
CONTAINER_NAME="my-container"

docker cp $CONTAINER_NAME:"$source_folder" "$destination_dir"


docker stop $CONTAINER_NAME

docker rm $CONTAINER_NAME
