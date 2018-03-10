read "CONT?Container (app/redis/mysql)"
if [ "$CONT" != '' ]; then
  docker exec -it $CONT /bin/bash
else
  docker exec -it mysql /bin/bash
fi
