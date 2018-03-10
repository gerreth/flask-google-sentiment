read "CONT?Dumping DB? (y/n)"
if [ "$CONT" = 'y' ]; then
  echo "Dumping::";
  docker-compose down -v
fi
echo "Bring it up::";
docker-compose up --build
